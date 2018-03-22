# Nanomsg实验[转]
nanomsg实验——survey
摘要： nanomsg实验——survey survey模式是由server发出询问，client针对请求回复响应的一种模式。这种模式在分布式系统中非常有用， 可以用来做服务发现、分布式事物等分布式询问。 客户端 客户端实现比较方便，除了基础调用（创建socket、连接url）之外，就是先接收服务端
nanomsg实验——survey
survey模式是由server发出询问，client针对请求回复响应的一种模式。这种模式在分布式系统中非常有用，
可以用来做服务发现、分布式事物等分布式询问。
客户端
客户端实现比较方便，除了基础调用（创建socket、连接url）之外，就是先接收服务端询问
（例子中比较简单，服务端询问是固定的，所以没有对内容进行检查）针对询问发送响应
（例子中是发送服务端当前时间）
 
```
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <nanomsg/nn.h>
#include <nanomsg/survey.h>
 
using namespace std;
 
int main(int argc, const char **argv) {
    if(argc != 3) {
        fprintf(stderr, "usage: %s NAME URL\n", argv[0]);
        exit(-1);
    }
    const char *name = argv[1];
    const char *url = argv[2];
 
    int sock = nn_socket(AF_SP, NN_RESPONDENT);
    if(sock < 0){
        fprintf(stderr, "nn_socket fail: %s\n", nn_strerror(errno));
        exit(-1);
    }
    if(nn_connect(sock, url) < 0) {
        fprintf(stderr, "nn_connect fail: %s\n", nn_strerror(errno));
        exit(-1);
    }
 
    while(1){
        char *buf = NULL;
        int bytes = nn_recv (sock, &buf, NN_MSG, 0);
 
        if(bytes > 0) {
            printf ("CLIENT (%s): RECEIVED "%s" SURVEY REQUESTn", name, buf);
            nn_freemsg (buf);
 
            char sendBuffer[128];
            time_t rawtime;
            struct tm * timeinfo;
 
            time (&rawtime);
            timeinfo = localtime (&rawtime);
            char *timeText = asctime (timeinfo);
            int textLen = strlen(timeText);
            timeText[textLen - 1] = '';
            sprintf(sendBuffer, "[ %s ] %s", name, timeText);
            int sendSize = strlen(sendBuffer) + 1;
            int actualSendSize = nn_send(sock, sendBuffer, sendSize, 0);
 
            if(actualSendSize != sendSize) {
                fprintf(stderr, "nn_send fail, expect length %d, actual length %dn", sendSize, actualSendSize);
                continue;
            }
        }
    }
 
    nn_shutdown(sock, 0);
 
    return 0;
}
```

这里收到消息后，就简单的打印，然后将响应数据写会给服务端。
服务端
服务端有个问题，之前搜索了几个例子都不太正常。经过尝试和简单查看代码之后发现，通过nanomsg基础api，
无法获取当前有多少客户端。但是，如果当前所有连接的客户端的响应都已经收到，再次调用nn_recv之后，
会直接返回-1，表示读取失败，同时errno（通过errno函数获取）被设置为EFSM，表示当前状态机状态不正确。

```
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <unistd.h>
#include <nanomsg/nn.h>
#include <nanomsg/survey.h>
 
using namespace std;
 
const char *SURVEY_TYPE = "DATE";
 
int main(int argc, char** argv)
{
 
    if ( argc != 2 ) {
        fprintf(stderr, "usage: %s URLn", argv[0]);
        exit(-1);
    }
    const char *url = argv[1];
    int sock = nn_socket(AF_SP, NN_SURVEYOR);
    if(sock < 0) {
        fprintf (stderr, "nn_socket failed: %sn", nn_strerror (errno));
        exit(-1);
    }
 
    if(nn_bind(sock, url) < 0) {
        fprintf(stderr, "nn_bind fail: %sn", nn_strerror(errno));
        exit(-1);
    }
 
    while(1) {
        int sendSize = strlen(SURVEY_TYPE) + 1;
        int actualSendSize;
        printf ("SERVER: SENDING DATE SURVEY REQUESTn");
        if ((actualSendSize = nn_send(sock, SURVEY_TYPE, sendSize, 0)) != sendSize) {
            fprintf(stderr, "nn_send fail, expect length %d, actual length %dn", sendSize, actualSendSize);
            continue;
        }
 
        int count = 0;
        while(1) {
            char *buf = NULL;
            int bytes = nn_recv (sock, &buf, NN_MSG, 0);
            if (bytes < 0 && nn_errno() == ETIMEDOUT) break;
            if (bytes >= 0) {
                printf ("SERVER: RECEIVED "%s" SURVEY RESPONSEn", buf);
                ++count;
                nn_freemsg (buf);
            } else {
                fprintf(stderr, "nn_recv fail: %sn", nn_strerror(errno));
                break;
            }
        }
        printf("SERVER: current receive %d survey response.n", count);
        sleep(1);
    }
 
    nn_shutdown(sock, 0);
 
    return 0;
 
}
```

这里用了两个死循环，外层循环不停尝试向客户端发起询问。完成询问后，通过另外一个死循环读取所有的客户端响应，
当读取失败时退出循环。
之前找到的源码是直接判断错误是否ETIMEDOUT，经过打印会发现每次都没有超时，而是状态机错误：
 
/*  If no survey is going on return EFSM error. */
if (nn_slow (!nn_surveyor_inprogress (surveyor)))
    return -EFSM;
测试
测试和前文差不多，先启动一个server，然后再一个个启动client：

```
#!/bin/bash
 
BASE="$( cd "$( dirname "$0" )" && pwd )"
SERVER=$BASE/surveyserver
CLIENT=$BASE/surveyclient
 
URL="tcp://127.0.0.1:1234"
 
echo "start surveyserver to bind tcp: $URL"
$SERVER tcp://127.0.0.1:1234 &
 
echo "start to start surveyclient"
for((i = 0; i < 10; i++))
do
    echo "start client$i"
    $CLIENT client$i $URL &
    sleep 1
done
 
sleep 20
echo "kill all process and exit"
 
for pid in `jobs -p`
do
    echo "kill $pid"
    kill $pid
done
 
wait


输出为：
 
start surveyserver to bind tcp: tcp://127.0.0.1:1234
start to start surveyclient
start client0
SERVER: SENDING DATE SURVEY REQUEST
start client1
nn_recv fail: Operation cannot be performed in this state
SERVER: current receive 0 survey response.
start client2
SERVER: SENDING DATE SURVEY REQUEST
CLIENT (client0): RECEIVED "DATE" SURVEY REQUEST
SERVER: RECEIVED "[ client0 ] Tue Feb 17 23:32:43 2015" SURVEY RESPONSE
CLIENT (client1): RECEIVED "DATE" SURVEY REQUEST
SERVER: RECEIVED "[ client1 ] Tue Feb 17 23:32:43 2015" SURVEY RESPONSE
nn_recv fail: Operation cannot be performed in this state
SERVER: current receive 2 survey response.
start client3
SERVER: SENDING DATE SURVEY REQUEST
CLIENT (client0): RECEIVED "DATE" SURVEY REQUEST
CLIENT (client1): RECEIVED "DATE" SURVEY REQUEST
CLIENT (client2): RECEIVED "DATE" SURVEY REQUEST
...
SERVER: SENDING DATE SURVEY REQUEST
CLIENT (client0): RECEIVED "DATE" SURVEY REQUEST
CLIENT (client1): RECEIVED "DATE" SURVEY REQUEST
CLIENT (client2): RECEIVED "DATE" SURVEY REQUEST
CLIENT (client3): RECEIVED "DATE" SURVEY REQUEST
CLIENT (client4): RECEIVED "DATE" SURVEY REQUEST
CLIENT (client5): RECEIVED "DATE" SURVEY REQUEST
CLIENT (client6): RECEIVED "DATE" SURVEY REQUEST
CLIENT (client7): RECEIVED "DATE" SURVEY REQUEST
CLIENT (client9): RECEIVED "DATE" SURVEY REQUEST
CLIENT (client8): RECEIVED "DATE" SURVEY REQUEST
SERVER: RECEIVED "[ client0 ] Tue Feb 17 23:33:09 2015" SURVEY RESPONSE
SERVER: RECEIVED "[ client1 ] Tue Feb 17 23:33:09 2015" SURVEY RESPONSE
SERVER: RECEIVED "[ client2 ] Tue Feb 17 23:33:09 2015" SURVEY RESPONSE
SERVER: RECEIVED "[ client3 ] Tue Feb 17 23:33:09 2015" SURVEY RESPONSE
SERVER: RECEIVED "[ client4 ] Tue Feb 17 23:33:09 2015" SURVEY RESPONSE
SERVER: RECEIVED "[ client5 ] Tue Feb 17 23:33:09 2015" SURVEY RESPONSE
SERVER: RECEIVED "[ client6 ] Tue Feb 17 23:33:09 2015" SURVEY RESPONSE
SERVER: RECEIVED "[ client7 ] Tue Feb 17 23:33:09 2015" SURVEY RESPONSE
SERVER: RECEIVED "[ client9 ] Tue Feb 17 23:33:09 2015" SURVEY RESPONSE
SERVER: RECEIVED "[ client8 ] Tue Feb 17 23:33:09 2015" SURVEY RESPONSE
nn_recv fail: Operation cannot be performed in this state
SERVER: current receive 10 survey response.
```

从输出可以看见，每次最后一个接收完成之后，都会有一个“Operation cannot be performed in this state”
错误，也就是EFSM错误

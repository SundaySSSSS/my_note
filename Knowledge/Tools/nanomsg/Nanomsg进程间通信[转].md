# Nanomsg进程间通信[转]

nanomsg是zeromq作者重新用C语言写的消息队列：http://nanomsg.org/index.html

它提供了6种通信模式，也即所谓“扩展性协议”（运行在传输层之上）——包括一对一（pair）、多对多（bus）、发布者-订阅者（pubsub）、调查者（survey）、管道（pipeline）、请求-响应（reqrep）。

本示例提供单机进程间通信运行环境作为传输层，参考教程：http://tim.dysinger.net/posts/2013-09-16-getting-started-with-nanomsg.html。由于作者有点懒，我把代码改成能够在Linux上运行的：https://github.com/begeekmyfriend/nanomsg-tutorial
```
1. [文件] pair.c ~ 2KB     下载(21)     

#include "common.h"
#include <nanomsg/pair.h>
 
#define NODE0 "node0"
#define NODE1 "node1"
#define SOCKET_ADDR "ipc:///tmp/pair.ipc"
 
int send_name(int sock, const char *name)
{
        printf("%s: SENDING \"%s\"\n", name, name);
        int sz_n = strlen(name) + 1;
        return nn_send(sock, name, sz_n, 0);
}
 
int recv_name(int sock, const char *name)
{
        char *buf = NULL;
        int result = nn_recv(sock, &buf, NN_MSG, 0);
        if (result > 0)
        {
                printf("%s: RECEIVED \"%s\"\n", name, buf);
                nn_freemsg(buf);
        }
        return result;
}
 
int send_recv(int sock, const char *name)
{
        int to = 100;
        assert(nn_setsockopt (sock, NN_SOL_SOCKET, NN_RCVTIMEO, &to, sizeof (to)) >= 0);
        while(1)
        {
                recv_name(sock, name);
                sleep(1);
                send_name(sock, name);
        }
}
 
int node0(const char *url)
{
        int sock = nn_socket(AF_SP, NN_PAIR);
        assert(sock >= 0);
        assert(nn_bind (sock, url) >= 0);
        send_recv(sock, NODE0);
        return nn_shutdown (sock, 0);
}
 
int node1(const char *url)
{
        int sock = nn_socket(AF_SP, NN_PAIR);
        assert(sock >= 0);
        assert(nn_connect(sock, url) >= 0);
        send_recv(sock, NODE1);
        return nn_shutdown (sock, 0);
}
 
int main(int argc, char **argv)
{
        if (argc == 2 && strncmp(NODE0, argv[1], strlen(NODE0)) == 0) {
                return node0(SOCKET_ADDR);
        } else if (argc == 2 && strncmp (NODE1, argv[1], strlen (NODE1)) == 0) {
                return node1(SOCKET_ADDR);
        } else {
                fprintf (stderr, "Usage: pair %s|%s <ARG> ...\n", NODE0, NODE1);
                return 1;
        }
}
文件] pubsub.c ~ 2KB     下载(14)     

#include "common.h"
#include <nanomsg/pubsub.h>
 
#define SERVER "server"
#define CLIENT "client"
#define SOCKET_ADDR "ipc:///tmp/pubsub.ipc"
 
char *date(void)
{
        time_t raw = time(&raw);
        struct tm *info = localtime(&raw);
        char *text = asctime(info);
        text[strlen(text) - 1] = '\0';
        return text;
}
 
int server(const char *url)
{
        int sock = nn_socket(AF_SP, NN_PUB);
        assert(sock >= 0);
        assert(nn_bind (sock, url) >= 0);
 
        while (1)
        {
                char *d = date();
                int sz_d = strlen(d) + 1; // '\0' too
                printf("SERVER: PUBLISHING DATE %s\n", d);
                int bytes = nn_send(sock, d, sz_d, 0);
                assert(bytes == sz_d);
                sleep(1);
        }
 
        return nn_shutdown(sock, 0);
}
 
int client(const char *url, const char *name)
{
        int sock = nn_socket (AF_SP, NN_SUB);
 
        assert(sock >= 0);
        /* TODO learn more about publishing/subscribe keys */
        assert(nn_setsockopt (sock, NN_SUB, NN_SUB_SUBSCRIBE, "", 0) >= 0);
        assert(nn_connect (sock, url) >= 0);
 
        while (1)
        {
                char *buf = NULL;
                int bytes = nn_recv(sock, &buf, NN_MSG, 0);
                assert(bytes >= 0);
                printf("CLIENT (%s): RECEIVED %s\n", name, buf);
                nn_freemsg(buf);
        }
 
        return nn_shutdown(sock, 0);
}
 
int main(const int argc, const char **argv)
{
        if (argc == 2 && strncmp(SERVER, argv[1], strlen(SERVER)) == 0) {
                return server(SOCKET_ADDR);
        } else if (argc == 3 && strncmp (CLIENT, argv[1], strlen (CLIENT)) == 0) {
                return client(SOCKET_ADDR, argv[2]);
        } else {
                fprintf(stderr, "Usage: pubsub %s|%s <ARG> ...\n", SERVER, CLIENT);
                return 1;
        }
}
文件] reqrep.c ~ 2KB     下载(13)     

#include "common.h"
#include <nanomsg/reqrep.h>
 
#define NODE0 "node0"
#define NODE1 "node1"
#define DATE "DATE"
#define SOCKET_ADDR "ipc:///tmp/reqrep.ipc"
 
char *date(void)
{
        time_t raw = time(&raw);
        struct tm *info = localtime(&raw);
        char *text = asctime(info);
 
        text[strlen(text) - 1] = '\0';
 
        return text;
}
 
int node0(const char *url)
{
        int sz_date = strlen(DATE) + 1;
        int sock = nn_socket(AF_SP, NN_REP);
 
        assert(sock >= 0);
        assert(nn_bind(sock, url) >= 0);
 
        while (1) {
                char *buf = NULL;
                int bytes = nn_recv(sock, &buf, NN_MSG, 0);
 
                assert(bytes >= 0);
                if (strncmp(DATE, buf, sz_date) == 0) {
                        printf("NODE0: RECEIVED DATE REQUEST\n");
                        char *d = date();
                        int sz_d = strlen(d) + 1;
                        printf("NODE0: SENDING DATE %s\n", d);
                        bytes = nn_send(sock, d, sz_d, 0);
                        assert(bytes == sz_d);
                }
                nn_freemsg (buf);
        }
 
        return nn_shutdown (sock, 0);
}
 
int node1(const char *url)
{
        int sz_date = strlen(DATE) + 1;
        char *buf = NULL;
        int bytes = -1;
        int sock = nn_socket(AF_SP, NN_REQ);
 
        assert(sock >= 0);
        assert(nn_connect(sock, url) >= 0);
 
        /* Send */
        printf("NODE1: SENDING DATE REQUEST %s\n", DATE);
        bytes = nn_send (sock, DATE, sz_date, 0);
        assert(bytes == sz_date);
 
        /* Receive */
        bytes = nn_recv (sock, &buf, NN_MSG, 0);
        assert(bytes >= 0);
        printf("NODE1: RECEIVED DATE %s\n", buf);
        nn_freemsg(buf);
 
        return nn_shutdown (sock, 0);
}
 
int main (int argc, char **argv)
{
        if (argc == 2 && strncmp(NODE0, argv[1], strlen(NODE0)) == 0) {
                return node0(SOCKET_ADDR);
        } else if (argc == 2 && strncmp(NODE1, argv[1], strlen(NODE1)) == 0) {
                return node1(SOCKET_ADDR);
        } else {
                fprintf (stderr, "Usage: reqrep %s|%s <ARG> ...\n", NODE0, NODE1);
                return 1;
        }
}
文件] survey.c ~ 2KB     下载(14)     

#include "common.h"
#include <nanomsg/survey.h>
 
#define SERVER "server"
#define CLIENT "client"
#define DATE   "DATE"
#define SOCKET_ADDR "ipc:///tmp/survey.ipc"
 
char *date(void)
{
        time_t raw = time (&raw);
        struct tm *info = localtime (&raw);
        char *text = asctime (info);
        text[strlen(text)-1] = '\0';
        return text;
}
 
int server(const char *url)
{
        int sock = nn_socket(AF_SP, NN_SURVEYOR);
 
        assert(sock >= 0);
        assert(nn_bind(sock, url) >= 0);
        sleep(1); /* wait for connections */
 
        /* Send */
        printf("SERVER: SENDING DATE SURVEY REQUEST\n");
        int sz_d = strlen(DATE) + 1;
        int bytes = nn_send(sock, DATE, sz_d, 0);
        assert (bytes == sz_d);
 
        while (1) {
                /* Receive */
                char *buf = NULL;
                bytes = nn_recv(sock, &buf, NN_MSG, 0);
                if (bytes == ETIMEDOUT) {
                        break;
                }
                if (bytes >= 0) {
                        printf("SERVER: RECEIVED \"%s\" SURVEY RESPONSE\n", buf);
                        nn_freemsg (buf);
                }
        }
 
        return nn_shutdown(sock, 0);
}
 
int client(const char *url, const char *name)
{
        int sock = nn_socket(AF_SP, NN_RESPONDENT);
 
        assert(sock >= 0);
        assert(nn_connect(sock, url) >= 0);
        while (1) {
                char *buf = NULL;
                int bytes = nn_recv(sock, &buf, NN_MSG, 0);
                if (bytes >= 0) {
                        printf("CLIENT (%s): RECEIVED \"%s\" SURVEY REQUEST\n", name, buf);
                        nn_freemsg(buf);
                        char *d = date();
                        int sz_d = strlen(d) + 1; // '\0' too
                        printf("CLIENT (%s): SENDING DATE SURVEY RESPONSE\n", name);
                        int bytes = nn_send (sock, d, sz_d, 0);
                        assert(bytes == sz_d);
                }
        }
 
        return nn_shutdown(sock, 0);
}
 
int main(int argc, char **argv)
{
        if (argc == 2 && strncmp(SERVER, argv[1], strlen(SERVER)) == 0) {
                return server (SOCKET_ADDR);
        } else if (argc == 3 && strncmp(CLIENT, argv[1], strlen(CLIENT)) == 0) {
                return client (SOCKET_ADDR, argv[2]);
        } else {
                fprintf(stderr, "Usage: survey %s|%s <ARG> ...\n", SERVER, CLIENT);
                return 1;
        }
}
文件] bus.c ~ 3KB     下载(14)     

#include "common.h"
#include <nanomsg/bus.h>
 
#define NODE0_SOCKET_ADDR "ipc:///tmp/node0.ipc"
#define NODE1_SOCKET_ADDR "ipc:///tmp/node1.ipc"
#define NODE2_SOCKET_ADDR "ipc:///tmp/node2.ipc"
#define NODE3_SOCKET_ADDR "ipc:///tmp/node3.ipc"
 
int node0(void)
{
        int sock = nn_socket(AF_SP, NN_BUS);
 
        assert(sock >= 0);
        assert(nn_bind(sock, NODE0_SOCKET_ADDR) >= 0);
        sleep(1); /* wait for connections */
 
        assert(nn_connect(sock, NODE1_SOCKET_ADDR) >= 0);
        assert(nn_connect(sock, NODE2_SOCKET_ADDR) >= 0);
        sleep(1); /* wait for connections */
 
        return sock;
}
 
int node1(void)
{
        int sock = nn_socket(AF_SP, NN_BUS);
 
        assert(sock >= 0);
        assert(nn_bind(sock, NODE1_SOCKET_ADDR) >= 0);
        sleep(1); /* wait for connections */
 
        assert(nn_connect(sock, NODE2_SOCKET_ADDR) >= 0);
        assert(nn_connect(sock, NODE3_SOCKET_ADDR) >= 0);
        sleep(1); /* wait for connections */
 
        return sock;
}
 
int node2(void)
{
        int sock = nn_socket(AF_SP, NN_BUS);
 
        assert(sock >= 0);
        assert(nn_bind(sock, NODE2_SOCKET_ADDR) >= 0);
        sleep(1); /* wait for connections */
 
        assert(nn_connect(sock, NODE3_SOCKET_ADDR) >= 0);
        sleep(1); /* wait for connections */
 
        return sock;
}
 
int node3(void)
{
        int sock = nn_socket(AF_SP, NN_BUS);
 
        assert(sock >= 0);
        assert(nn_bind(sock, NODE3_SOCKET_ADDR) >= 0);
        sleep(1); /* wait for connections */
 
        assert(nn_connect(sock, NODE0_SOCKET_ADDR) >= 0);
        sleep(1); /* wait for connections */
 
        return sock;
}
 
int bus_on(int sock, const char *name)
{
        int to = 100;
        assert(nn_setsockopt(sock, NN_SOL_SOCKET, NN_RCVTIMEO, &to, sizeof(to)) >= 0);
 
        /* SEND */
        int sz_n = strlen(name) + 1;
        printf("%s: SENDING '%s' ONTO BUS\n", name, name);
        int send = nn_send(sock, name, sz_n, 0);
        assert (send == sz_n);
 
        while (1) {
                /* RECV */
                char *buf = NULL;
                int recv = nn_recv(sock, &buf, NN_MSG, 0);
                if (recv >= 0) {
                        printf("%s: RECEIVED '%s' FROM BUS\n", name, buf);
                        nn_freemsg(buf);
                }
        }
 
        return nn_shutdown(sock, 0);
}
 
int node(const char *name)
{
        int sock;
 
        if (!strcmp(name, "node0")) {
                sock = node0();
        } else if (!strcmp(name, "node1")) {
                sock = node1();
        } else if (!strcmp(name, "node2")) {
                sock = node2();
        } else if (!strcmp(name, "node3")) {
                sock = node3();
        } else {
                return -1;
        }
 
        return bus_on(sock, name);
}
 
int main(int argc, char **argv)
{
        if (argc == 2) {
                return node(argv[1]);
        } else {
                fprintf (stderr, "Usage: bus <NODE_NAME> ...\n");
                return 1;
        }
}
```

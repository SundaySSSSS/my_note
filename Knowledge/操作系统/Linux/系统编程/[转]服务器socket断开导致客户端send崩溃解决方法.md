# [转]服务器socket断开导致客户端send崩溃解决方法

原文来自：http://blog.chinaunix.net/uid-24830931-id-3786670.html
## 一、现象描述

在利用librdkafka同kafka broker通信过程中，当kafka broker意外退出时（如kill -9），librdkafka接口的sendmsg接口报出了“Program received signal SIGPIPE, Broken pipe.” 这个错误具有典型性，根据网络搜索的结果，这个一般是由于向一个被破坏的socket连接或者pipe读写数据造成的，向有经验的同事请教，他们说这种场景不会出现SIGPIPE信号，而是直接send， write， sendmsg等返回-1，同时errno会被设置成EPIPE。

实践是检验真理的唯一标准，找个例子一试便知。

## 二、例子程序
为了快速检验，从网上上借了一个简单的客户端、服务器程序，http://hi.baidu.com/dlpucat/item/97ab75c5243b8761f6c95d75，多谢原作者。

服务器端程序 server.c
```
1. #include <netinet/in.h>
2. #include <sys/types.h>
3. #include <sys/socket.h>
4. #include <stdio.h>
5. #include <stdlib.h>
6. #include <string.h>
7.  
8. #define HELLO_WORLD_SERVER_PORT 6666
9. #define LENGTH_OF_LISTEN_QUEUE 20
10. #define BUFFER_SIZE 1024
11.  
12. int main(int argc, char **argv)
13. {
14.   struct sockaddr_in server_addr;
15.   bzero(&server_addr,sizeof(server_addr));
16.   server_addr.sin_family = AF_INET;
17.   server_addr.sin_addr.s_addr = htons(INADDR_ANY);
18.   server_addr.sin_port = htons(HELLO_WORLD_SERVER_PORT);
19.  
20.   int server_socket = socket(AF_INET,SOCK_STREAM,0);
21.   if( server_socket < 0)
22.   {
23.     printf("Create Socket Failed!");
24.     exit(1);
25.   }
26.  
27.   if( bind(server_socket,(struct sockaddr*)&server_addr,sizeof(server_addr)))
28.   {
29.     printf("Server Bind Port : %d Failed!", HELLO_WORLD_SERVER_PORT);
30.     exit(1);
31.   }
32.  
33.   if ( listen(server_socket, LENGTH_OF_LISTEN_QUEUE) )
34.   {
35.     printf("Server Listen Failed!");
36.     exit(1);
37.   }
38.  
39.   while (1)
40.   {
41.     struct sockaddr_in client_addr;
42.     socklen_t length = sizeof(client_addr);
43.  
44.     int new_server_socket = accept(server_socket,(struct sockaddr*)&client_addr,&length);
45.     if ( new_server_socket < 0)
46.     {
47.       printf("Server Accept Failed!\n");
48.       break;
49.     }
50.  
51.     char buffer[BUFFER_SIZE];
52.     bzero(buffer, BUFFER_SIZE);
53.     strcpy(buffer,"Hello,World from server!");
54.     strcat(buffer,"\n");
55.     send(new_server_socket,buffer,BUFFER_SIZE,0);
56.  
57.     bzero(buffer,BUFFER_SIZE);
58.         while(1){
59.       length = recv(new_server_socket,buffer,BUFFER_SIZE,0);
60.       if (length < 0)
61.       {
62.         printf("Server Recieve Data Failed!\n");
63.         exit(1);
64.       }
65.       printf("\n%s",buffer);
66.         }
67.     close(new_server_socket);
68.   }
69.   close(server_socket);
70.   return 0;
71. }
```

客户端程序

```
1. #include <netinet/in.h>
2. #include <sys/types.h>
3. #include <sys/socket.h>
4. #include <stdio.h>
5. #include <stdlib.h>
6. #include <string.h>
7. #include <signal.h>
8. #include <errno.h>
9.  
10. #define HELLO_WORLD_SERVER_PORT 6666
11. #define BUFFER_SIZE 1024
12.  
13. int main(int argc, char **argv)
14. {
15.   if (argc != 2)
16.   {
17.     printf("Usage: ./%s ServerIPAddress\n",argv[0]);
18.     exit(1);
19.   }
20.  
21.   struct sockaddr_in client_addr;
22.   bzero(&client_addr,sizeof(client_addr));
23.   client_addr.sin_family = AF_INET;
24.   client_addr.sin_addr.s_addr = htons(INADDR_ANY);
25.   client_addr.sin_port = htons(0);
26.  
27.   int client_socket = socket(AF_INET,SOCK_STREAM,0);
28.  
29.   if( client_socket < 0)
30.   {
31.     printf("Create Socket Failed!\n");
32.     exit(1);
33.   }
34.  
35.   if( bind(client_socket,(struct sockaddr*)&client_addr,sizeof(client_addr)))
36.   {
37.     printf("Client Bind Port Failed!\n");
38.     exit(1);
39.   }
40.  
41.   struct sockaddr_in server_addr;
42.   bzero(&server_addr,sizeof(server_addr));
43.   server_addr.sin_family = AF_INET;
44.   if(inet_aton(argv[1],&server_addr.sin_addr) == 0)
45.   {
46.     printf("Server IP Address Error!\n");
47.     exit(1);
48.   }
49.   server_addr.sin_port = htons(HELLO_WORLD_SERVER_PORT);
50.   socklen_t server_addr_length = sizeof(server_addr);
51.   if(connect(client_socket,(struct sockaddr*)&server_addr, server_addr_length) < 0)
52.   {
53.     printf("Can Not Connect To %s!\n",argv[1]);
54.     exit(1);
55.   }
56.  
57.   char buffer[BUFFER_SIZE];
58.   bzero(buffer,BUFFER_SIZE);
59.   int length = recv(client_socket,buffer,BUFFER_SIZE,0);
60.   if(length < 0)
61.   {
62.     printf("Recieve Data From Server %s Failed!\n", argv[1]);
63.     exit(1);
64.   }
65.   printf("From Server %s :\t%s",argv[1],buffer);
66.  
67.   bzero(buffer,BUFFER_SIZE);
68.   strcpy(buffer,"Hello, World! From Client\n");
69.  
70.   while(1){
71.     sleep(1);
72.     int ret = send(client_socket,buffer,BUFFER_SIZE,0);
73.         if (ret == -1 && errno == EPIPE){
74.       printf("receive sigpipe\n");
75.     }
76.   }
77.  
78.   close(client_socket);
79.   return 0;
80. }

```

## 三、重现方法
step 1）编译： gcc -o server server.c
          gcc -o -g client client.c （通过gdb直接看到异常退出）

step 2）启动服务器端：./server

step 3) 启动客户端：（这里假设客户端和服务器部署在同一台服务器） gdb ./client 
(gdb) r 127.0.0.1

step 4) 观察正常运行结果：首先是客户端收到服务器端的消息：From Server 127.0.0.1 : Hello,World from server!
         然后是服务器端每隔1s收到客户端的消息： Hello, World! From Client

step 5）通过ctrl+c关闭服务器端

step 6）观察客户端结果
Program received signal SIGPIPE, Broken pipe.
0x0000003a7fcd55f5 in send () from /lib64/libc.so.6

重现了！！


## 四、解决办法
解决办法很多，也很简单。

4.1 client中忽略SIGPIPE信号

`signal(SIGPIPE, SIG_IGN);`

4.2 阻止SIGPIPE信号（后来追查，原来同事的程序框架中已经有了这种机制，所以没有经历过程序退出的问题）
```
sigset_t set;
sigemptyset(&set);
sigaddset(&set, SIGPIPE);
sigprocmask(SIG_BLOCK, &set, NULL);
```
4.3  为SIGPIPE添加信号处理函数，处理完程序继续执行

`signal(SIGPIPE, pipesig_handler);`

多种选择，总有一款适合您。


经验证测试，第2种方法可以屏蔽Broken pipe，然后通过客户端发送字节长度为-1，从而做处理

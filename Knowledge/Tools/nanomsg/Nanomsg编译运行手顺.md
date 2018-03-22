# Nanomsg编译运行手顺

## 第一步: 安装cmake
安装cmake
见cmake部分
## 第二步: 编译nanomsg
编译nanomsg链接库
在nanomsg根目录下运行
```
./configure
make
```
运行成功后会生成如下一个库, 两个链接
> libnanomsg.so
> libnanomsg.so.1.0.0
> libnanomsg.so.5.0.0
## 第三步: 编译测试程序
建立自己程序的文件夹, 例如/work/share/bus_test
将
> libnanomsg.so
> libnanomsg.so.1.0.0
> libnanomsg.so.5.0.0
拷贝到/work/share/bus_test文件夹中, 写一个测试程序,假设代码文件名为: bus_test.c, 见末尾代码片(从网上找的测试程序)
引入相关头文件, 这里根据测试程序的写法, 应建立nanomsg文件夹, 从nanomsg的源码中将nn.h和bus.h放到里面

编译, 可以使用如下命令
`gcc -o bus_test bus_test.c -L/work/share/bus_test -Wl,-rpath,/work/share/bus_test -lnanomsg`
## 第四步: 测试运行效果
开几个终端, 分别运行./bus_test node1 ./bus_test node2 ./bus_test node3即可看到效果

## 测试代码
```
	#include <stdio.h>
	#include <string.h>
	#include <assert.h>
	#include "nanomsg/nn.h"
	#include "nanomsg/bus.h"
	 
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
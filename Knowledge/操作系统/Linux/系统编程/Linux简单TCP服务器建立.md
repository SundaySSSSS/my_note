# Linux简单TCP服务器建立

代码摘自bh_server中江苏协议TCP Server
```
void startTCPServer()
{
    /* 创建socket(AF_INET: IPV4, SOCK_STREAM: tcp协议) */
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
    	dbout("TCPServerThread : create socket error\n");
    	return;
    }
    /* 调用bind函数将socket和地址 （包括ip,port）进行绑定 */
    struct sockaddr_in serveraddr;
    memset(&serveraddr, 0, sizeof(serveraddr));
    //往地址中填入ip，port，internet地址族类型
    serveraddr.sin_family = AF_INET; //IPV4
    serveraddr.sin_port = htons(ConfigGetInt(PC_CONFIG_JS_PORT));//port
    serveraddr.sin_addr.s_addr = INADDR_ANY;
    if (bind(sockfd, (struct sockaddr*)&serveraddr,
    					sizeof(serveraddr)) < 0) {
    	dbout("TCPServerThread : bind socket error, errno = %d\n", errno);
    	return;
    }

    /* 启动监听, 通知系统去接受来自客户端的连接请求 （将接受到的客户端连接放置到对应的队列中） */
    if (listen(sockfd, 1) < 0) {
    	dbout("TCPServerThread : listen socket error\n");
    	return;
    }

    while (1)
    {
    	//主控线程负责调用accept去获取客户端连接
    	int fd = accept(sockfd, NULL, NULL);	//这里不再通过accept获得套接字信息,故传入NULL
    	dbout("TCPServerThread : accept new client , fd = %d\n", fd);
    	if (fd < 0)
    	{
    		dbout("TCPServerThread : accept error\n");
    		continue;
    	}

    	/* 将accept到的文件描述符更改为无阻塞的 */
    	int flag;
    	if ((flag = fcntl(fd, F_GETFL, 0)) < 0)
    	{
    		dbout("TCPServerThread : F_GETFL error\n");
    	}
    	else
    	{
    		flag |= O_NONBLOCK;
    		if (fcntl(fd, F_SETFL, flag) < 0)
    		{
    			dbout("TCPServerThread : F_SETFL error\n");
    		}
    		else
    		{
    			dbout("TCPServerThread : set non block success\n");
    		}
    	}

    	/*
    	由于单链接限制, 不再启动子线程进行通信
    	pthread_t th;
    	int err;
    	if ((err = pthread_create(&th, NULL, th_fn, (void*)fd)) != 0)
    	{
    		dbout("TCPServerThread : pthread create error\n");
    	}
    	else
    	{
    		pthread_detach(th);
    	}
    	*/
    	th_fn((void*)fd);	//进行通信
    	dbout("TCPServerThread : a client is disconnect, try to accept another\n");
    }
}

void* th_fn(void *arg)
{
	int fd = (int)arg;
	do_service(fd);
	out_fd(fd);
	close(fd);

	return (void*)0;
}


/* 和客户端进行通信 */
void do_service(int fd)
{
	SOCKET m_TCPSock = fd;
	uint32 m_RecvHeartTime = TWDT_Get2();	//每次连接建立时,更新最后一次收到心跳包响应消息的时间
	uint32 m_RecvHeartFailCount = 0;		//将连续接收心跳包响应消息失败的次数置零

	while(m_TCPSock != INVALID_SOCKET)
	{
		//dbout("do_service : client do loop\n");
		/* 接收客户端回应 */
		if (dtask_tcp_echo(m_TCPSock, &m_RecvHeartTime) != 0)
		{
			dbout("do_service : dtask_tcp_echo return error\n");
			break;
		}

		/* 向客户端发送消息 */
		/* ... */
		usleep(10000);
	}
	dbout("do_service : client loop end\n");
}

//通过fd来获取套接字信息
void out_fd(int fd)
{
    	struct sockaddr_in addr;
    	socklen_t len = sizeof(addr);
    	//从fd中获取客户端信息,放入sockaddr_in中
    	if (getpeername(fd, (struct sockaddr*)&addr, &len) < 0) {
    		perror("getpeername error");
    		return;
    	}
    	char ip[16];
    	memset(ip, 0, sizeof(ip));
    	int port = ntohs(addr.sin_port);
    	inet_ntop(AF_INET, &addr.sin_addr.s_addr, ip, sizeof(ip));
    	dbout("out_fd: %16s(%5d) closed!\n", ip, port);
}

int dtask_tcp_echo(SOCKET fd, uint32* heart_time)
{
    int            i;
    //char           *pBuf;
    char 			pBuf[5] = {0};
    //HANDLE         hBuffer;
    int ret;

		memset(pBuf, 0, sizeof(pBuf));
		i = recv(fd, pBuf, sizeof(pBuf), MSG_NOSIGNAL);
    /* 对收到的数据进行处理 */
    /* ... */
    return(ret);
}

```

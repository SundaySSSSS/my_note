# 2_Windows网络编程基础
## TCP通信
添加引用文件
```C++
#include <stdio.h>
#include <WinSock2.h>
#pragma comment (lib, "ws2_32")
```

启动时启动WinSock
```C++
//初始化WinSock库
WSADATA wsaData;
WSAStartup(MAKEWORD(2, 2), &wsaData);
```

退出时关闭WinSock
```C++
WSACleanup();
```

简易版服务器线程
```C++
DWORD WINAPI ThreadTCPServer(LPVOID lpParameter)
{
	//创建socket
	SOCKET sLisent = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
	//填充地址结构
	struct sockaddr_in ServerAddr;
	ServerAddr.sin_family = AF_INET;
	ServerAddr.sin_addr.S_un.S_addr = inet_addr("127.0.0.1");
	ServerAddr.sin_port = htons(5678);
	//绑定
	bind(sLisent, (SOCKADDR*)&ServerAddr, sizeof(ServerAddr));
	//监听
	listen(sLisent, SOMAXCONN);
	//获取连接请求
	sockaddr_in ClientAddr;
	int nSize = sizeof(ClientAddr);
	SOCKET sClient = accept(sLisent, (SOCKADDR *)&ClientAddr, &nSize);
	//输出客户端的IP和端口号
	CString clientInfoStr;
	clientInfoStr.Format(L"Client %s:%d", inet_ntoa(ClientAddr.sin_addr),
		ntohs(ClientAddr.sin_port));
	AfxMessageBox(clientInfoStr);
	//发送消息
	char* sendMsg = "Hello Client";
	send(sClient, sendMsg, strlen(sendMsg) + 1, 0);
	//接收消息
	char recvMsg[MAXBYTE] = { 0 };
	recv(sClient, recvMsg, MAXBYTE, 0);
	CString recvMsgStr;
	recvMsgStr.Format(L"客户端消息: %s", recvMsg);
	AfxMessageBox(recvMsgStr);
	return 0;
}
```

简易版客户端线程
```C++
DWORD WINAPI ThreadTCPClient(LPVOID lpParameter)
{
	//创建socket
	SOCKET sServer = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
	//填充地址结构
	struct sockaddr_in ServerAddr;
	ServerAddr.sin_family = AF_INET;
	ServerAddr.sin_addr.S_un.S_addr = inet_addr("127.0.0.1");
	ServerAddr.sin_port = htons(5678);
	//连接服务器
	connect(sServer, (SOCKADDR*)&ServerAddr, sizeof(ServerAddr));
	//接收消息
	char szMsg[MAXBYTE] = { 0 };
	recv(sServer, szMsg, MAXBYTE, 0);
	AfxMessageBox(CString(szMsg));
	//发送消息
	strcpy(szMsg, "Hello Server");
	send(sServer, szMsg, strlen(szMsg) + 1, 0);

	return 0;
}
```

## UDP通信
简易Server
```C++

DWORD WINAPI ThreadUDPServer(LPVOID lpParameter)
{
	//创建socket
	SOCKET sServer = socket(PF_INET, SOCK_DGRAM, IPPROTO_UDP);
	//填充地址结构
	struct sockaddr_in ServerAddr;
	ServerAddr.sin_family = AF_INET;
	ServerAddr.sin_addr.S_un.S_addr = inet_addr("127.0.0.1");
	ServerAddr.sin_port = htons(5678);
	//绑定
	bind(sServer, (SOCKADDR*)&ServerAddr, sizeof(ServerAddr));
	
	//接收消息
	char szMsg[MAXBYTE] = { 0 };
	struct sockaddr_in ClientAddr;
	int nSize = sizeof(ClientAddr);
	recvfrom(sServer, szMsg, MAXBYTE, 0, (SOCKADDR*)&ClientAddr, &nSize);

	CString recvMsgStr;
	recvMsgStr.Format("客户端消息: %s", szMsg);
	AfxMessageBox(recvMsgStr);
	
	//发送消息
	char* sendMsg = "Hello Client";
	sendto(sServer, sendMsg, strlen(sendMsg) + 1, 0, (SOCKADDR*)&ClientAddr, nSize);
	
	return 0;
}
```
建议Client
```C++
DWORD WINAPI ThreadUDPClient(LPVOID lpParameter)
{
	//创建socket
	SOCKET sClient = socket(PF_INET, SOCK_DGRAM, IPPROTO_UDP);
	//填充地址结构
	struct sockaddr_in ServerAddr;
	ServerAddr.sin_family = AF_INET;
	ServerAddr.sin_addr.S_un.S_addr = inet_addr("127.0.0.1");
	ServerAddr.sin_port = htons(5678);
	
	//发送消息
	char szMsg[MAXBYTE] = { 0 };
	strcpy(szMsg, "Hello Server");
	int nSize = sizeof(ServerAddr);
	sendto(sClient, szMsg, strlen(szMsg) + 1, 0, (SOCKADDR*)&ServerAddr, nSize);
	//接收消息
	nSize = sizeof(ServerAddr);
	recvfrom(sClient, szMsg, MAXBYTE, 0, (SOCKADDR*)&ServerAddr, &nSize);

	AfxMessageBox(CString(szMsg));

	return 0;
}

```

## 非阻塞模式
设置非阻塞模式可以使用API
```C++
int WSAAsyncSelect(SOCKET s, HWND hWnd, unsigned int wMsg, long lEvent);
//s为socket
//hWnd为接收消息的窗口句柄
//wMsg为一个自定义消息, 当网络事件发生时, 向该窗口发送此消息
//lEvent: 指定应用程序感兴趣的通知码
```

## 原始套接字 自制ping命令
Ping命令依赖ICMP协议， ICMP是IP层的协议, ICMP报文封装在IP数据报内部
IP数据报 = IP首部 + ICMP报文
ICMP报文 = 8位类型 + 8位代码 + 16位校验和 + ICMP内容
代码如下:
```C++

#include "stdafx.h"
#include <stdio.h>
#include <WinSock2.h>
#pragma comment (lib, "ws2_32")

//typedef unsigned char UINT8;
//typedef unsigned short UINT16;
//typedef unsigned long UINT32;
//typedef long INT32;

struct icmp_header
{
	UINT8 icmp_type;	//消息类型
	UINT8 icmp_code;	//代码
	UINT16 icmp_checksum;	//校验和
	UINT16 icmp_id;	//用来唯一标示此请求的ID号, 通常设置为进程ID
	UINT16 icmp_sequence;	//序列号
	UINT32 icmp_timestamp;	//时间戳
};

#define ICMP_HEADER_SIZE sizeof(icmp_header)
#define ICMP_ECHO_REQUEST 0x08;
#define ICMP_ECHO_REPLY 0x00;

//计算校验和
UINT16 getSum(struct icmp_header *picmp, int len)
{
	INT32 sum = 0;
	UINT16 *pusicmp = (UINT16*)picmp;

	while (len > 1)
	{
		sum += *(pusicmp++);
		if (sum & 0x80000000)
		{
			sum = (sum & 0xffff) + (sum >> 16);
		}
		len -= 2;
	}
	if (len)
		sum += (UINT16)* (UINT8*)pusicmp;
	while (sum >> 16)
	{
		sum = (sum & 0xffff) + (sum >> 16);
	}
	return (UINT16)~sum;
}

bool MyPing(char* szDestIp)
{
	bool ret = true;
	WSADATA wsaData;
	int nTimeOut = 1000;
	char szBuff[ICMP_HEADER_SIZE + 32] = { 0 };
	icmp_header *pIcmp = (icmp_header*)szBuff;
	char icmp_data[32] = { 0 };

	WSAStartup(MAKEWORD(2, 2), &wsaData);
	//创建原始套接字
	SOCKET s = socket(PF_INET, SOCK_RAW, IPPROTO_ICMP);
	//设置接收超时
	setsockopt(s, SOL_SOCKET, SO_RCVTIMEO, (char const*)&nTimeOut, sizeof(nTimeOut));
	//设置目的地址
	sockaddr_in dest_addr;
	dest_addr.sin_family = AF_INET;
	dest_addr.sin_addr.S_un.S_addr = inet_addr(szDestIp);
	dest_addr.sin_port = htons(0);
	//构造ICMP包
	pIcmp->icmp_type = ICMP_ECHO_REQUEST;
	pIcmp->icmp_code = 0;
	pIcmp->icmp_id = (USHORT)::GetCurrentProcessId();
	pIcmp->icmp_sequence = 0;
	pIcmp->icmp_checksum = 0;
	pIcmp->icmp_timestamp = 0;
	//拷贝数据, 数据可以是任意的, 使用abc是为了和系统提供的看起来一样
	memcpy((szBuff + ICMP_HEADER_SIZE), "abcdefghijklmnopqrstuvwabcdefghi", 32);
	//计算校验和
	pIcmp->icmp_checksum = getSum((struct icmp_header*)szBuff, sizeof(szBuff));

	sockaddr_in from_addr;
	char szRecvBuff[1024];
	int nLen = sizeof(from_addr);
	sendto(s, szBuff, sizeof(szBuff), 0, (SOCKADDR*)&dest_addr, sizeof(SOCKADDR));
	recvfrom(s, szRecvBuff, MAXBYTE, 0, (SOCKADDR *)&from_addr, &nLen);

	//判断接收到的是否是目标地址
	char szReplyIp[1024] = { 0 };
	strcpy(szReplyIp, inet_ntoa(from_addr.sin_addr));
	if (strcmp(inet_ntoa(from_addr.sin_addr), szDestIp) != 0)
	{
		ret = false;
	}
	return ret;
}

int _tmain(int argc, _TCHAR* argv[])
{
	bool ret = MyPing("127.0.0.1");
	if (ret)
		printf("ping success\n");
	else
		printf("ping failed\n");
	
	getchar();
	return 0;
}
```

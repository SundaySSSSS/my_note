# 带超时的connect

## 非阻塞connect套接字的作用： 
1）完成一个connect要花费RTT时间，而RTT波动范围很大，从局域网上的几个毫秒甚至是广域网上的几秒，这段时间也许有我们要执行的其他处理工作可以执行。 
2）可以使用这个技术同事建立多个连接。 
3）许多connect的超时实现以75秒为默认值，如果应用程序想自定义一个超时时间，就是使用非阻塞的connect.
在一个非阻塞的套接字上调用connect，connect会立即返回EINPROGRESS,错误，但是已经发起的TCP三次握手继续进行。
非阻塞connect套接字实现时需要注意的细节: 
1）连接到同一主机上，connect会立即完成，我们必须处理这种情形 
2）POSIX关于select和非阻塞connect的以下两个规则: 
1)连接成功，描述符会变成可写 
2)连接建立遇到错误时，描述符变为可读可写。
## 非阻塞connect实现流程: 
一: 
1)调用fcntl把套接字设置为非阻塞 
2)调用connect，如果返回0，表示连接已经完成，如果返回-1，那么期望收到的错误是EINPROGRESS，连接建立已经 启动，但是尚未完成。
二：调用select，等待套接字变为可读可写，
三：处理超时： 
如果select返回0，超时发生，那么返回ETIMEOUT错误给调用者，并且关闭套接字，防止已经启动的三路握手继续下去。
四:检查可读或可写条件： 
如果描述符变为可读或可写，我们就调用getsockopt获取套接字的待处理错误（SO_ERROR套接字选项） 
连接成功： getsockopt返回0 
连接失败：getsockopt返回0， 并且获取相应的错误。 
五： 
恢复socket套接字状态，如果getsockopt返回的错误是非0，那么就设置errno为相应的值，函数返回-1，如果成功，就返回0

## 代码实现
和<UNIX网络编程>中的例子基本相同
``` C
int connect_nonb(int sockfd, sockaddr* addr, socklen_t len, int nsec, int usec)
{
    int flags, error = 0;
    fd_set rset, wset;
    struct timeval tv;

    //set socket nonblocking
    if((flags = fcntl(sockfd, F_GETFL, 0)) < 0) {
        return -1;
    }
    if(fcntl(sockfd, F_SETFL, O_NONBLOCK) < 0) {
        return -1;
    }

    //connect
    if(connect(sockfd, addr, len) < 0) {
        if(errno != EINPROGRESS)
        {
            fcntl(sockfd, F_SETFL, flags);
            return -1;
        }
    }
    else {//connect competed immediately
        fcntl(sockfd, F_SETFL, flags);
        return 0;
    }

    //select
    FD_ZERO(&rset);
    FD_SET(sockfd, &rset);
    wset = rset;
    tv.tv_sec = nsec;
    tv.tv_usec = usec;

    if(select(sockfd + 1, &rset, &wset, NULL, &tv) == 0) {
        //timeout
        close(sockfd);
        errno = ETIMEDOUT;
        return -1;
    }

    //check read fd set and write fd set
    if(FD_ISSET(sockfd, &rset) || FD_ISSET(sockfd, &wset)) {
        socklen_t len = sizeof(error);
        if(getsockopt(sockfd, SOL_SOCKET, SO_ERROR, &error, &len) < 0 ) {
            errno = error;
            return -1;
        }
    }

    if(error != 0) {
        errno = error;
        return -1;
    }
    if(fcntl(sockfd, F_SETFL, flags) < 0)
    {
        return -1;
    }
    return 0;
}

```
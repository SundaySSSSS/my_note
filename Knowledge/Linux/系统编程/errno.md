# errno


先`#include <errno.h>`后, 在发生错误后, 即可使用errno变量来查找错误

例如:

```
if (bind(sockfd, (struct sockaddr*)&serveraddr,
						sizeof(serveraddr)) < 0) {
	dbout("TCPServerThread : bind socket error, errno = %d\n", errno);
	return;
}
```

将errno转化为可读的字符串

```
#include <string.h>
//将errno转化为可以读懂的字符串
char *strerror(int errnum);

```

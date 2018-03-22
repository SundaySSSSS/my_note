# Linux端口重用

```
int Net::tcp_listen(unsigned short port)
{
int fd, one = 1;
struct sockaddr_in sa_in;


if ((fd = socket(PF_INET, SOCK_STREAM, 0)) < 0)
return -1;
if (setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &one, sizeof(one)) < 0) {
close(fd);
return -1;
}
set_nonblocking(fd, 0);
bzero(&sa_in, sizeof(sa_in));
sa_in.sin_family = AF_INET;
sa_in.sin_port = htons(port);
sa_in.sin_addr.s_addr = INADDR_ANY;
bind(fd, (struct sockaddr *)&sa_in, sizeof(sa_in));
listen(fd, 1024);
global->PRINTF("Listen on port:%d, fd:%d\n", port, fd);
return fd;
}
```

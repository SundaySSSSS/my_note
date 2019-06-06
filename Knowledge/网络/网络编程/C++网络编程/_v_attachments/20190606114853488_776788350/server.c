#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char** argv) {
    printf("starting server\n");
	char hello[] = "hello world";
	struct sockaddr_in sa;
	int fd = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
	if (-1 == fd) {
		perror("cannot create socket");
		exit(EXIT_FAILURE);
	}
	memset(&sa, 0, sizeof(sa));

	sa.sin_family = AF_INET;
    sa.sin_port = htons(2222);
    sa.sin_addr.s_addr = htonl(INADDR_ANY);

    if (-1 == bind(fd, (struct sockaddr*)&sa, sizeof(sa))) {
        perror("bind failed");
        close(fd);
        exit(EXIT_FAILURE);
    }
    
    printf("start listening\n");
    if (-1 == listen(fd, 10)) {
        perror("listen failed");
        close(fd);
        exit(EXIT_FAILURE);
    }

    for (;;) {
        int clientFd = accept(fd, NULL, NULL);
        if (0 > clientFd) {
            perror("accept failed");
            close(fd);
            exit(EXIT_FAILURE);
        }
        int writeSize = 0;
        int totalWrite = 0;
        while (totalWrite <  sizeof(hello)) {
            writeSize = write(clientFd, hello + totalWrite, sizeof(hello) - totalWrite);
            if (-1 == writeSize) {
                perror("write failed");
                close(clientFd);
                close(fd);
                exit(EXIT_FAILURE);
            }
            totalWrite += writeSize;
        }

        if (-1 == shutdown(clientFd, SHUT_RDWR)) {
            perror("shutdown failed");
            close(clientFd);
            close(fd);
            exit(EXIT_FAILURE);
        }
    }
}

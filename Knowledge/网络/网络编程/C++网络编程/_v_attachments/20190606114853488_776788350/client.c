#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char** argv) {
    struct sockaddr_in sa;
    int res;
    int fd = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);

    if (-1 == fd) {
        perror("cannot create socket");
        exit(EXIT_FAILURE);    
    }

    memset(&sa, 0, sizeof(sa));
    sa.sin_family = AF_INET;
    sa.sin_port = htons(2222);
    res = inet_pton(AF_INET, "127.0.0.1", &sa.sin_addr);

    if (-1 == connect(fd, (struct sockaddr*)&sa, sizeof(sa))) {
        perror("connect failed");
        close(fd);
        exit(EXIT_FAILURE);
    }

    char buffer[512];
    int totalRead = 0;
    for (;;) {
        int readSize = 0;
        readSize = read(fd, buffer + totalRead, sizeof(buffer) - totalRead);
        if (readSize == 0) {
            // read all
            break;
        } else if (readSize == -1) {
            perror("read failed");
            close(fd);
            exit(EXIT_FAILURE);
        }
        totalRead += readSize;
    }
    buffer[totalRead] = 0;
    printf("get from server: %s\n", buffer);

    (void)shutdown(fd, SHUT_RDWR);
    close(fd);
    return EXIT_SUCCESS;
}

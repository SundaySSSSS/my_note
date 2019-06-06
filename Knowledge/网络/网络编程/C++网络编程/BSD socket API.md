# BSD socket API
## 常用头文件
``` C
sys/socket.h //相关API函数和数据结构的定义
netinet/in.h    //IPv4和IPv6相关协议族需要的信息
arpa/inet.h    //处理数字从操作系统字节序到网络字节序
```

## API函数
``` C
socket()
bind()
listen()
connect()
accept()
send() recv() write() read()
close()
gethostbyname() gethostbyaddr() // IPv4专用
```

``` C
select() poll()
getsocketopt()
setsocketopt()
```

## socket编程
### 基本流程图
![socket使用流程](_v_images/20190606100034473_1250106029.png)

### server和client示例
见附件, 其中, server对每个连接的客户端发送一个固定的hello world字符串
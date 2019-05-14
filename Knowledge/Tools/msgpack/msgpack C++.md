# msgpack C++
## 消息解包
``` C++
//数据存放在如下buffer中
char* buf;
int buf_size;

msgpack::object_handle o_h = msgpack::unpack(buf, buf_size);
msgpack::object o = o_h.get();
static int data = 0;
o.convert(data);
```

## 消息打包
``` C++
typedef struct _MyStruct
{
    int a;
    MSGPACK_DEFINE(a)    //使用msgpack定义的宏,提示成员a进行序列化, 目前发现最多能序列化32个成员
}
MyStruct;
```

``` C++
msgpack::sbuffer sbuf;
MyStruct temp;    //自定义的结构体
msgpack::pack(sbuf, temp);

//取出序列化后的数据
QByteArray o(sbuf.data(), sbuf.size());
```
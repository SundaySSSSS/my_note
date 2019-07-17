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

## 例子
``` C++

#include <msgpack.hpp>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;


struct Foo
{
    int     i;
    string  str;
    // 原始指针类型，内部封装了pack_raw和pack_raw_body方法
    msgpack::type::raw_ref  data;

    MSGPACK_DEFINE(i, str, data); 
};


int main(int argc, char** argv)
{
    Foo  f;
    f.i = 4;
    f.str = "hello world";
    const char* tmp = "msgpack";
    f.data.ptr = tmp;
    f.data.size = strlen(tmp) + 1;

    msgpack::sbuffer  sbuf;
    msgpack::pack(sbuf, f);

    msgpack::unpacked  unpack;
    msgpack::unpack(&unpack, sbuf.data(), sbuf.size());

    msgpack::object  obj = unpack.get();

    Foo f2;
    obj.convert(&f2);

    cout << f2.i << ", " << f2.str << ", ";
    cout << f2.data.ptr << endl;

    return 0;
}
```
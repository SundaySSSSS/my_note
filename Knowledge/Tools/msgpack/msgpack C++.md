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

typedef struct _SVar
{
    char type;
    string data;
    MSGPACK_DEFINE(type, data);
}
SVar;

struct Foo
{
    int     i;
    string  str;
    // 原始指针类型，内部封装了pack_raw和pack_raw_body方法
    msgpack::type::raw_ref  data;

    vector<string> vecData;
    map<string,SVar> mapData;

    MSGPACK_DEFINE(i, str, data, vecData, mapData);
};


int main(int argc, char** argv)
{
    QApplication a(argc, argv);

    Foo  f;
    f.i = 4;
    f.str = "hello world";
    const char* tmp = "msgpack";
    f.data.ptr = tmp;
    f.data.size = strlen(tmp) + 1;
    f.vecData.push_back("cxy");
    f.vecData.push_back("yxc");

    SVar svar;
    svar.type = 0;
    svar.data = "data1";
    f.mapData.insert(map<string, SVar>::value_type("1", svar));

    svar.type = 99;
    svar.data = "data2";
    f.mapData.insert(map<string, SVar>::value_type("2", svar));

    msgpack::sbuffer  sbuf;
    msgpack::pack(sbuf, f);

    qDebug() << "sbuf size" << sbuf.size();

    msgpack::object_handle oh = msgpack::unpack(sbuf.data(), sbuf.size());
    msgpack::object obj = oh.get();

    Foo f2;
    obj.convert(f2);

    qDebug() << "f2: " << QString::number(f2.i) << ", " << QString::fromStdString(f2.str) << ", ";
    qDebug() << f2.data.ptr;
    qDebug() << QString::fromStdString(f2.vecData[0]) << QString::fromStdString(f2.vecData[1]);

    map<string, SVar>::iterator iter;
    for (iter = f2.mapData.begin(); iter != f2.mapData.end(); iter++)
    {
        qDebug() << QString::fromStdString(iter->first) << QString::number((iter->second).type) <<
                    QString::fromStdString((iter->second).data);
    }
    return 0;
}
```

输出结果为:
```
sbuf size 54
f2:  "4" ,  "hello world" , 
msgpack
"cxy" "yxc"
"1" "0" "data1"
"2" "99" "data2"
```
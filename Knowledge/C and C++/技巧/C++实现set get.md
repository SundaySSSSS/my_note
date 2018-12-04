# 实现set get
 
## 一、文章来由
由于c++并不能像java 的 eclipse 有自动生成 get 和 set 方法。  
如果手写是可以，但是当属性特别多的时候会非常麻烦  
但是宏定义方法可以解决
## 二、具体代码
### 2.1 非指针类型成员变量
``` C++
// PropertyBuilderByName 用于生成类的成员变量
// 并生成set和get方法
// type 为变量类型
// access_permission 为变量的访问权限(public, priavte, protected)
#define PropertyBuilderByName(type, name, access_permission)\
    access_permission:\
        type m_##name;\
    public:\
    inline void set##name(type v) {\
        m_##name = v;\
    }\
    inline type get##name() {\
        return m_##name;\
    }\
```
分析：
可以这样写的原因就是因为 #define 预处理，是在编译器编译之前执行的纯字符串替换，这里的 ##name 会直接被替换成传入的 name，所以该宏生成成员变量 m_name 由 name 决定，其访问权限由 acess_permission 指定  
另外：  
`#define语句中的#是把参数字符串化，##是连接两个参数成为一个整体。  
### 2.2 指针类型成员变量

同样的道理:

```
#define PointerPropertyBuilderByName(type, name, access_permission)\
    access_permission:\
        type* m_##name;\
    public:\
        inline void set##name(type* v){\
            m_##name = v;\
        }\
        inline type* get##name(){\
            return m_##name;\
        }\

```

### 2.3 测试代码

```
class Test
{
    PropertyBuilderByName(int, A, private)
    PointerPropertyBuilderByName(double, DBV, private)
};
int main()
{
    Test t;
    t.setA(10);
    cout << "A = " << t.getA() << endl;

    double a = 12.3445;
    t.setDBV(&a);
    cout << "DBV: " << *(t.getDBV()) << endl;

    system("pause");
    return 0;
}
```

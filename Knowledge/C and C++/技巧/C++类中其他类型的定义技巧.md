# C++类中其他类型的定义技巧

可以使用在类中typedef的方法, 减少复杂的命名:
例如

``` C++
typedef struct _DoAComplexThingParam
{
    int a;
    int b;
}
DoAComplexThingParam;

class ComplexThing
{
public:
    void setParam(DoAComplexThingParam param);
    ...
};
```

就可以写为如下形式

``` C++
class ComplexThing
{
public:
    typedef struct _Param
    {
        int a;
        int b;
    }
    Param;
    void setParam(Param param) { m_param = param; }
private:
    Param m_param;
};

ComplexThing::Param param;
param.a = 1;
param.b = 1;
ComplexThing ct;
ct.setParam(param);
```

下方的例子中, 不再需要想一个复杂的前缀命名Param, 只需使用简单的Param作为名称即可
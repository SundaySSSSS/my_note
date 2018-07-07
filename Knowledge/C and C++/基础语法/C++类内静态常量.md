# C++类内静态常量的初始化

C++内添加静态常量, 如果是整型, 可以直接在类内添加, 如:
```C++
class GeogCtrl
{
public:
    GeogCtrl();
    const static double PI = 3.14159265;    //NG!!!只有整型静态常量数据可以在类内初始化
    const static int temp = 1;    //OK
};
```

静态的非整型常量, 可以在类外初始化
```C++
class GeogCtrl
{
public:
    GeogCtrl();
    const static double PI;
    const static int temp = 1;    //OK
};

const double GeogCtrl::PI = 3.14159265; //OK
```
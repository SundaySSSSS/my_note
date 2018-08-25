# C++双冒号放函数开头
调用函数前加"::"，代表调用的是全局函数，不是类自己的成员函数
例如：

```C++
#include <iostream>
using namespace std;

void func()
{
    cout<<"global function"<<endl;
}
class A
{
public:
    int print()
    {
        ::func();
        cout<<"class A "<<endl;
    }
    void func()
    {
        cout<<"class A method"<<endl;
    }
};

int main()
{
    A a;
    a.print();
    return 0;

}
```
打印结果：
```
global function
class A
```

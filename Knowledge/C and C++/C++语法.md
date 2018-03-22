# C++语法
## 关键字
### mutable
类中, 带有const的函数不能访问非static的成员, 但如果声明为mutable, 则可以打破这个限制
声明方法:
```
class Test
{
private:
    mutable int a;
public:
    void func() const { a = 1; }    //OK!!!
};
```
### explicit
要求必须明确调用构造函数来构造对象
例如:
```
#include <iostream>
using namespace std;

class Test
{
public:
    explicit Test(int a) {}
};

int main()
{
    Test t = 10;    //编译error, 去掉explicit关键字则可以通过编译
    return 0;
}
```

## 转型
### C中的转型
1, `(int)a`
2, `int(a)`

### C++中的转型
#### const_cast<T>(expression)
常属性移除
#### dynamic_cast<T>(expression)
运行期间进行向上, 向下转型
#### reinterpret_cast<T>(expression)
重新解读转型, bit位完全不变, 只是按照新的规则去解读
#### static_cast<T>(expression)
编译器认可的静态类型转换, 可用此替代C形式的转型

## 虚继承
???



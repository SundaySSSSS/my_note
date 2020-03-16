# C++智能指针
## shared_ptr
### shared_ptr特性
shared_ptr内部使用引用计数, 当引用计数为0时, 销毁指向的对象
### 创建shared_ptr
#### 使用new创建(不推荐)
注意下面例子中直接赋值为int指针的方法是错误的(第一行)
``` C++
//shared_ptr<int> p3 = new int(1024); //error
shared_ptr<int> p3(new int(1024));
```
#### 使用make_shared创建(推荐)
shared_ptr在创建时使用`make_shared`函数, 例如:
``` C++
#include <iostream>
#include <memory>
#include <string>

using namespace std;

int main()
{
    string str = "Hello World!";
    shared_ptr<string> p1 = make_shared<string>(str);
    cout << *p1 << endl;
    return 0;
}
```

### 使用shared_ptr
shared_ptr能够向上面例子中一样使用*取值
可以使用->获取指向的结构体中的成员, 例如:
``` C++
struct s
{
    string name;
    int age;
};

shared_ptr<s> p2 = make_shared<s>();
p2->name = "caocao";
p2->age = 55;
cout << p2->name << p2->age << endl;
```

### shared_ptr作为函数参数
如果一个函数的参数是智能指针, 不要创建临时对象去传入函数
``` C++
void process(shared_ptr<int> p)
{
    (*p)++;
}

int main()
{
    shared_ptr<int> p3(new int(1024));

    process(p3);
    cout << *p3 << endl;    //正确, 输出为1025

    int* x = new int(1024);
    process(shared_ptr<int>(x));
    cout << *x << endl; //error!!! x在process结束时已经被释放

    return 0;
}
```

### 使用智能指针的基本规范
1. 不使用相同的内置指针初始化(或reset)多个智能指针
2. 不delete get()返回的指针
3. 不适用get()初始化或reset另一个智能指针
4. 如果你使用get()返回的指针, 记住当最后一个对应的智能指针被销毁后, 你的指针就变得无效了
5. 如果使用的智能指针管理的不是new分配的内存, 记得传递给它一个删除器

## unique_ptr
一个unique_ptr拥有它所指向的对象, 某一时刻只能有一个unique_ptr指向一个给定的对象
### unique_ptr的特性
unique_ptr不支持拷贝
``` C++
unique_ptr<int> up1;
*up1 = 1;

unique_ptr<int> up2;
//up2 = up1;  //error!!!
//unique_ptr<int> up3(up1);   //error

```

### 函数返回unique_ptr
``` C++
unique_ptr<int> createUnique(int i)
{
    unique_ptr<int> ret(new int(i));
    return ret;
}

int main()
{
    unique_ptr<int> up3 = createUnique(5);
    return 0;
}
```

## weak_ptr
weak_ptr是一种不控制所指向对象声明周期的智能指针, 它配合shared_ptr使用, 指向一个shared_ptr管理的对象.
weak_ptr绑定到一个shared_ptr上时, 不会增加shared_ptr的引用计数
当shared_ptr的引用计数为0时, 即使还有weak_ptr指向此对象, 此对象还是会被销毁

### 创建weak_ptr
``` C++
weak_ptr<int> wp;
wp = make_shared<int>(42);
```

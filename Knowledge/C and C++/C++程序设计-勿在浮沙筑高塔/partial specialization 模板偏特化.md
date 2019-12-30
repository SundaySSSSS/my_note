# partial specialization 模板偏特化
## 常规形式
模板的一部分参数的特殊处理, 比如有两个模板参数T和Alloc,
其中, 如果T是bool时, 特殊处理 就可以用到模板的偏特化,
如下例子
``` C++
template<typename T, typename Alloc>
class vector
{

};

template<typename Alloc>
class vector<bool, Alloc>
{

};
```

## 指针形式
如果模板参数是指针, 可以走特殊的流程
``` C++
#include <string>

template <typename T>
class C
{
public:
    C()
    {
        std::cout << "T ctor" << std::endl;
    }
};

template <typename T>
class C<T*>
{
public:
    C()
    {
        std::cout << "T* ctor" << std::endl;
    }
};

void testPartialSpecialization()
{
    C<std::string> obj1;
    C<std::string*> obj2;
}
```
执行结果为:
```
T ctor
T* ctor
```
# variadic templates(C++11)数量不确定的模板参数


C++11中, 允许数量不定的模板类型,
例如:
下面例子中, print不断打印第一个参数, 并递归调用print
当print没有参数时, 会触发无参的print, 从而终止递归
其中`sizeof...`可以返回当前不定数量模板参数的个数
``` C++

void print()
{

}

template <typename T, typename...Types>
void print(const T& firstArg, const Types&... args)
{
    std::cout << "param num = " << sizeof...(args) << "---" << firstArg << std::endl;
    print(args...);
}

void testVariadicTemplates()
{
    print(10, 22.0, "hello");
}
```

输出为:
```
param num = 2---10
param num = 1---22
param num = 0---hello
```

# specialization 模板特化
模板在实现时, 可能遇到某些特殊类型要特殊处理, 就需要模板特化

``` C++
//泛化, 所有的类型都可以使用
template <class Key>
struct hash {};

//特化, 在为char时
template<>
struct hash<char>
{
    size_t operator() (char x) const
    {
        std::cout << "char" << std::endl;
        return x;
    }
};

template<>
struct hash<int>
{
    size_t operator() (int x) const
    {
        std::cout << "int" << std::endl;
        return x;
    }
};

template<>
struct hash<long>
{
    size_t operator() (long x) const
    {
        std::cout << "long" << std::endl;
        return x;
    }
};

int main()
{

    hash<char>()(64);
    hash<int>()(128);
    hash<long>()(256);
}
```

输出为
```
char
int
long
```
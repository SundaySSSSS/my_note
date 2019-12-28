# function-like-class (仿函数)
仿函数是一个类, 行为像函数
例子如下: 

``` C++
#include <iostream>
template <class Pair>
struct select1st
{
    const typename Pair::first_type& operator()(const Pair& x) const
    {
        return x.first;
    }
};

template <class Pair>
struct select2nd
{
    const typename Pair::second_type& operator()(const Pair& x) const
    {
        return x.second;
    }
};

template <class T1, class T2>
struct pair
{
    typedef T1 first_type;
    typedef T2 second_type;

    T1 first;
    T2 second;
    pair() : first(T1()), second(T2()) {}
    pair(const T1& a, const T2& b) : first(a), second(b) {}
};

int main()
{
    pair<int, int> p;
    select1st<pair<int, int> > s1;
    select2nd<pair<int, int> > s2;
    p.first = 1;
    p.second = 2;
    std::cout << s1(p) << std::endl;
    std::cout << s2(p) << std::endl;

    return -1;
}

```
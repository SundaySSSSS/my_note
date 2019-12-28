# member template-成员模板
成员模板是类的成员函数是模板函数
``` C++

class Base1 {};
class Derived1: public Base1 {};
class Base2 {};
class Derived2: public Base2 {};

template <class T1, class T2>
struct pair
{
    typedef T1 first_type;
    typedef T2 second_type;

    T1 first;
    T2 second;
    pair() : first(T1()), second(T2()) {}
    pair(const T1& a, const T2& b) : first(a), second(b) {}

    //成员模板
    //一个构造函数, 用另一个Pair来构造本Pair, 其中T1, U1需要是继承关系, T2,U2也需要是继承关系
    template <class U1, class U2>
    pair(const pair<U1, U2>& p) : first(p.first), second(p.second) {}
};

int main()
{
    pair<Derived1, Derived2> d;
    pair<Base1, Base2> b(d);
    return 0;
}
```
# pointer-like classes 智能指针

最简单实现
``` C++
template <class T>
class shared_ptr
{
public:
    T& operator*() const
    { return *px; }

    T* operator->() const
    { return px; }

    shared_ptr(T* p) : px(p) {}

private:
    T* px;
};
```
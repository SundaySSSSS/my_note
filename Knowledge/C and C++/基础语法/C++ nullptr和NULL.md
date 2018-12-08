# C++ nullptr和NULL

NULL在C中定义为(void*)0
在C++中定义为0

在C++中, 0的定义有歧义
如下两个重载函数

```C++
void boo(int a, int* b);
void boo(int a, int b);
```

当b传入NULL时会发生歧义
故C++11后, 使用nullptr

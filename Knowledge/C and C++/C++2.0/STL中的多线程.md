# STL中的多线程
## 编译
通常需要增加c++11的支持
例如:
```
g++ -std=c++11 test.cpp -o test
```

## 最简单例子
``` C++
#include <thread>
#include <iostream>

void helloWorld() {
    std::cout << "hello world" << std::endl;
}

int main() {
    std::thread t(helloWorld);
    std::cout << "hello main thread" << std::endl;
    t.join();
    return 0;
}
```

## 多线程计算特定任务

## 


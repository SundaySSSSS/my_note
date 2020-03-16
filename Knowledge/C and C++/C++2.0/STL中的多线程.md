# STL中的多线程
## 编译
通常需要增加c++11的支持
例如:
```
g++ -std=c++11 test.cpp -o test
```

## thread
### 最简单例子
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

### 线程参数
std::thread的构造函数可以进行参数传递, 如下例:
``` C++
#include <iostream>
#include <string>
#include <thread>

using namespace std;

void foo(string str)
{
    cout << str << endl;
}

int main() {
    std::thread t(foo, "caocao");
    t.join();
    return 0;
}
```

### 类的成员函数运行到线程中
类成员函数做为线程入口时，把this做为第一个参数传递进去即可。
``` C++
#include <thread>
#include <iostream>

class Greet
{
    const char *owner = "Greet";
public:
    void SayHello(const char *name) {
        std::cout << "Hello " << name << " from " << this->owner << std::endl;
    }
};
int main() {
    Greet greet;

    std::thread thread(&Greet::SayHello, &greet, "C++11");
    thread.join();

    return 0;
}
//输出：Hello C++11 from Greet
```

### join : 等待线程执行完毕
上面例子中已经多处使用. 调用join后, 线程的函数要执行完毕前, join阻塞

### sleep
使用`std::this_thread::sleep_for`和`std::this_thread::sleep_until`函数可以实现sleep

``` C++
#include <thread>
#include <iostream>
#include <chrono>

using namespace std::chrono;

void pausable() {
    // sleep 500毫秒
    std::this_thread::sleep_for(milliseconds(500));
    // sleep 到指定时间点
    std::this_thread::sleep_until(system_clock::now() + milliseconds(500));
}

int main() {
    std::thread thread(pausable);
    thread.join();

    return 0;
}
```

## mutex
互斥锁相关内容在mutex包中进行了实现
``` C++
#include <mutex>
```

### std::mutex
#### 基本的锁定lock和解锁unlock
``` C++
std::mutex mtx;           // mutex for critical section
void print_thread_id (int id) 
{
  // critical section (exclusive access to std::cout signaled by locking mtx):
  mtx.lock();
  std::cout << "thread #" << id << '\n';
  mtx.unlock();
}
```
调用lock时, 如果此互斥锁已经被别人lock, 则会发生阻塞, 直到另一端unlock

#### try_lock
试图锁定互斥锁, 不阻塞
如果已经被锁, 则返回false, 不进行阻塞
如果没有被锁, 则会锁定互斥锁
``` C++
if (mtx.try_lock()) {   // only increase if currently not locked:
    ++counter;
    mtx.unlock();
}
```

### std::recursive_mutex
和mutex基本相同, 但是允许递归锁定, 即同一线程可以多次上锁

### 互斥锁包装器
#### std::lock_guard
``` C++
#include <thread>
#include <mutex>
#include <iostream>
 
int g_i = 0;
std::mutex g_i_mutex;  // 保护 g_i
 
void safe_increment()
{
    std::lock_guard<std::mutex> lock(g_i_mutex);
    ++g_i;
    std::cout << std::this_thread::get_id() << ": " << g_i << '\n';
    // g_i_mutex 在锁离开作用域时自动释放
}
```

#### std::unique_lock
std::unique_lock也支持std::lock_guard的功能，但是区别在于它提供跟多的成员函数使用更加灵活，并且能够和condition_variable一起使用来控制线程同步
std::unique_lock提供lock和unlock接口, 可以临时解锁
例如:
``` C++
class LogFile {
    std::mutex _mu;
    ofstream f;
public:
    LogFile() {
        f.open("log.txt");
    }
    ~LogFile() {
        f.close();
    }
    void shared_print(string msg, int id) {

        std::unique_lock<std::mutex> guard(_mu);
        //do something 1
        guard.unlock(); //临时解锁

        //do something 2

        guard.lock(); //继续上锁
        // do something 3
        f << msg << id << endl;
        cout << msg << id << endl;
    }
};
```

std::unique_lock可以在构造时指定不上锁
``` C++
std::mutex _mu;
std::unique_lock<std::mutex> guard(_mu, std::defer_lock);
```

## 原子操作
C++11中所有的原子类都是不允许拷贝的, 不允许move的
### std::atomic_flag
一个原子的布尔变量
atomic_flag有三种状态: 未初始化, clear(false), set(true)
#### 初始化
``` C++
std::atomic_flag af = ATOMIC_FLAG_INIT;
```
此时atomic_flag处于clear状态。

#### 设置为set(可以理解为true)
``` C++
af.test_and_set();
```
test_and_set函数的逻辑为: 
该函数会检测flag是否处于set状态，如果不是，则将其设置为set状态，并返回false；否则返回true。

#### clear(可以理解为置为false)
``` C++
af.clear();
```

#### 综合例子
下面代码通过10个线程，模拟了一个计数程序，第一个完成计数的会打印"win"。
``` C++
#include <atomic>    // atomic_flag
#include <iostream>  // std::cout, std::endl
#include <list>      // std::list
#include <thread>    // std::thread

void race(std::atomic_flag &af, int id, int n) {
    for (int i = 0; i < n; i++) {
    }
    // 第一个完成计数的打印：Win
    if (!af.test_and_set()) {
        printf("%s[%d] win!!!\n", __FUNCTION__, id);
    }
}

int main() {
    std::atomic_flag af = ATOMIC_FLAG_INIT;

    std::list<std::thread> lstThread;
    for (int i = 0; i < 10; i++) {
        lstThread.emplace_back(race, std::ref(af), i + 1, 5000 * 10000);    //emplace_back效果和push_back相同, 但省去了构造后复制的开销
    }

    for (std::thread &thr : lstThread) {
        thr.join();
    }

    return 0;
}
```

### std::atomic模板类
std::atomic不保证是无锁操作, std::atomic_flag保证是无锁的

``` C++
std::atomic<int> ai(0);
ai.store(1);
int i = ai.load();
```

## 条件互斥量 condition_variable
condition_variable用来阻塞一个线程或多个线程, 直到另一个线程同时修改一个共享变量, 并通知条件变量
条件变量提供了两类操作：wait和notify。这两类操作构成了多线程同步的基础。
### wait
wait是线程的等待动作，直到其它线程将其唤醒后，才会继续往下执行。下面通过伪代码来说明其用法：
``` C++
std::mutex mutex;
std::condition_variable cv;

// 条件变量与临界区有关，用来获取和释放一个锁，因此通常会和mutex联用。
std::unique_lock lock(mutex);
// 此处会释放lock，然后在cv上等待，直到其它线程通过cv.notify_xxx来唤醒当前线程，cv被唤醒后会再次对lock进行上锁，然后wait函数才会返回。
// wait返回后可以安全的使用mutex保护的临界区内的数据。此时mutex仍为上锁状态
cv.wait(lock)
```

### notify
当需要唤醒时, 执行notify_one或者notify_all

### 不考虑虚假唤醒的代码(错误代码)
``` C++
#include <iostream>
#include <condition_variable>
#include <mutex>
#include <thread>

std::mutex mutex_;
std::condition_variable condVar;

void doTheWork(){
  std::cout << "Processing shared data." << std::endl;
}

void waitingForWork(){
    std::cout << "Worker: Waiting for work." << std::endl;

    std::unique_lock<std::mutex> lck(mutex_);
    condVar.wait(lck);
    doTheWork();
    std::cout << "Work done." << std::endl;
}

void setDataReady(){
    std::cout << "Sender: Data is ready."  << std::endl;
    condVar.notify_one();
}

int main(){
  std::cout << std::endl;
  std::thread t1(waitingForWork);
  std::thread t2(setDataReady);
  t1.join();
  t2.join();
  std::cout << std::endl;
}
```

### 考虑虚假唤醒的代码(正确的方式)
#### 虚假的唤醒
接收方在发送方发出通知之前完成了任务。
这怎么可能呢？接收方对虚假的唤醒很敏感。所以即使没有通知发生，接收方也有可能会醒来。
为了保护它，我不得不向等待方法添加一个判断。

#### 虚假唤醒的原因
一般而言线程调用wait()方法后，需要其他线程调用notify,notifyAll方法后，线程才会从wait方法中返回， 而虚假唤醒(spurious wakeup)是指线程通过其他方式，从wait方法中返回。

下面是一个买票退票的操作例子，买票时，线程A买票，如果发现没有余票，则会调用wait方法，线程进入等待队列中，线程B进行退票操作，余票数量加一，然后调用notify 方法通知等待线程，此时线程A被唤醒执行购票操作。

从程序的顺序性来看没有问题，但是为什么会出现虚假唤醒呢？

因为wait方法可以分为三个操作：
（1）释放锁并阻塞
（2）等待条件cond发生
（3）获取通知后，竞争获取锁

假设此时有线程A,C买票，线程A调用wait方法进入等待队列，线程C买票时发现线程B在退票，获取锁失败，线程C阻塞，进入阻塞队列，线程B退票时，余票数量+1（满足条件2 等待条件发生），线程B调用notify方法后，线程C马上竞争获取到锁，购票成功后余票为0，而线程A此时正处于wait方法醒来过程中的第三步（竞争获取锁获取锁），当线程C释放锁，线程A获取锁后，会执行购买的操作，而此时是没有余票的

#### 代码示例1
``` C++
#include <iostream>
#include <condition_variable>
#include <mutex>
#include <thread>

std::mutex mutex_;
std::condition_variable condVar;

bool dataReady;

void doTheWork(){
  std::cout << "Processing shared data." << std::endl;
}

void waitingForWork(){
    std::cout << "Worker: Waiting for work." << std::endl;

    std::unique_lock<std::mutex> lck(mutex_);
    condVar.wait(lck,[]{return dataReady;});
    doTheWork();
    std::cout << "Work done." << std::endl;
}

void setDataReady(){
    std::lock_guard<std::mutex> lck(mutex_);
    dataReady=true;
    std::cout << "Sender: Data is ready."  << std::endl;
    condVar.notify_one();
}

int main(){
  std::cout << std::endl;

  std::thread t1(waitingForWork);
  std::thread t2(setDataReady);

  t1.join();
  t2.join();

  std::cout << std::endl;

}
```

#### 代码示例2(cppreference示例)
``` C++
#include <iostream>
#include <string>
#include <thread>
#include <mutex>
#include <condition_variable>
 
std::mutex m;
std::condition_variable cv;
std::string data;
bool ready = false;
bool processed = false;
 
void worker_thread()
{
    // 等待直至 main() 发送数据
    std::unique_lock<std::mutex> lk(m);
    cv.wait(lk, []{return ready;});
 
    // 等待后，我们占有锁。
    std::cout << "Worker thread is processing data\n";
    data += " after processing";
 
    // 发送数据回 main()
    processed = true;
    std::cout << "Worker thread signals data processing completed\n";
 
    // 通知前完成手动解锁，以避免等待线程才被唤醒就阻塞（细节见 notify_one ）
    lk.unlock();
    cv.notify_one();
}
 
int main()
{
    std::thread worker(worker_thread);
 
    data = "Example data";
    // 发送数据到 worker 线程
    {
        std::lock_guard<std::mutex> lk(m);
        ready = true;
        std::cout << "main() signals data ready for processing\n";
    }
    cv.notify_one();
 
    // 等候 worker
    {
        std::unique_lock<std::mutex> lk(m);
        cv.wait(lk, []{return processed;});
    }
    std::cout << "Back in main(), data = " << data << '\n';
 
    worker.join();
}
```
# [C++]线程安全的队列

ThreadSafeQueue.h

注意, 不应该有cpp文件, 模板类要在声明时存在实现

``` C++
#ifndef THREADSAFEQUEUE_H
#define THREADSAFEQUEUE_H

#include <QMutex>
#include "../global.h"

template<class T>
class ThreadSafeQueue
{
public:
    ThreadSafeQueue() { m_max = 20; }
    void setMax(size_t max) { m_max = max; }
    bool push(T t);
    bool pop(T& t);
    bool isEmpty();
    int32 size();
private:
    queue<T> m_queue;
    QMutex m_mutex;
    size_t m_max;
};

template<class T>
bool ThreadSafeQueue<T>::push(T t)
{
    bool ret = false;
    m_mutex.lock();
    if (m_queue.size() < m_max)
    {
        m_queue.push(t);
        ret = true;
    }
    m_mutex.unlock();
    return ret;
}

template<class T>
bool ThreadSafeQueue<T>::pop(T& t)
{
    bool ret = false;
    m_mutex.lock();
    if (m_queue.size() > 0)
    {
        t = m_queue.front();
        m_queue.pop();
        ret = true;
    }
    m_mutex.unlock();
    return ret;
}

template<class T>
bool ThreadSafeQueue<T>::isEmpty()
{
    bool ret = false;
    m_mutex.lock();
    if (m_queue.size() == 0)
        ret = true;
    m_mutex.unlock();
    return ret;
}

template<class T>
int32 ThreadSafeQueue<T>::size()
{
    int32 size = 0;
    m_mutex.lock();
    size = m_queue.size();
    m_mutex.unlock();
    return size;
}

#endif // THREADSAFEQUEUE_H

```
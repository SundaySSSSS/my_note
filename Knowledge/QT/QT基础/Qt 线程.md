# Qt 线程

## 继承QThread
```C++
class WorkerThread : public QThread
{
    Q_OBJECT
public:
    WorkerThread();
private:
    void run();
};

WorkerThread::WorkerThread() { }

void WorkerThread::run()
{
    qDebug() << "worker thread run";
}

WorkerThread m_workerThread;
m_workerThread.start();
```
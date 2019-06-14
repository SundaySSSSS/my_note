# Qt 线程

## 方法1: 继承QThread
``` Qt
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

## 方法2: 继承自QObject
基本步骤:
1. 写一个继承QObject的类，对需要进行复杂耗时逻辑的入口函数声明为槽函数
2. 此类在旧线程new出来，不能给它设置任何父对象
3. 同时声明一个QThread对象，在官方例子里，QThread并没有new出来，这样在析构时就需要调用QThread::wait()，如果是堆分配的话， 可以通过deleteLater来让线程自杀
4. 把obj通过moveToThread方法转移到新线程中，此时object已经是在线程中了
5. 把线程的finished信号和object的deleteLater槽连接，这个信号槽必须连接，否则会内存泄漏
6. 正常连接其他信号和槽（在连接信号槽之前调用moveToThread，不需要处理connect的第五个参数，否则就显示声明用Qt::QueuedConnection来连接）
7. 初始化完后调用'QThread::start()'来启动线程
8. 在逻辑结束后，调用QThread::quit退出线程的事件循环

官方例子:
``` Qt
class Worker : public QObject
{
    Q_OBJECT
 
public slots:
    void doWork(const QString &parameter) {
        QString result;
        /* ... here is the expensive or blocking operation ... */
        emit resultReady(result);
    }
 
signals:
    void resultReady(const QString &result);
};
 
class Controller : public QObject
{
    Q_OBJECT
    QThread workerThread;
public:
    Controller() {
        Worker *worker = new Worker;
        worker->moveToThread(&workerThread);
        connect(&workerThread, &QThread::finished, worker, &QObject::deleteLater);
        connect(this, &Controller::operate, worker, &Worker::doWork);
        connect(worker, &Worker::resultReady, this, &Controller::handleResults);
        workerThread.start();
    }
    ~Controller() {
        workerThread.quit();
        workerThread.wait();
    }
public slots:
    void handleResults(const QString &);
signals:
    void operate(const QString &);
};
```
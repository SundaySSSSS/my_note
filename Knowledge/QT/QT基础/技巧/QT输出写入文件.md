# QT输出写入文件

## 新版本方法:
在QT的新版本中, 使用API `QtMessageHandler qInstallMessageHandler(QtMessageHandler handler)`注册回调函数
例如: (官方文档的例子)

``` C++
#include <qapplication.h>
#include <stdio.h>
#include <stdlib.h>

void myMessageOutput(QtMsgType type, const QMessageLogContext &context, const QString &msg)
{
    QByteArray localMsg = msg.toLocal8Bit();
    switch (type) {
    case QtDebugMsg:
        fprintf(stderr, "Debug: %s (%s:%u, %s)\n", localMsg.constData(), context.file, context.line, context.function);
        break;
    case QtInfoMsg:
        fprintf(stderr, "Info: %s (%s:%u, %s)\n", localMsg.constData(), context.file, context.line, context.function);
        break;
    case QtWarningMsg:
        fprintf(stderr, "Warning: %s (%s:%u, %s)\n", localMsg.constData(), context.file, context.line, context.function);
        break;
    case QtCriticalMsg:
        fprintf(stderr, "Critical: %s (%s:%u, %s)\n", localMsg.constData(), context.file, context.line, context.function);
        break;
    case QtFatalMsg:
        fprintf(stderr, "Fatal: %s (%s:%u, %s)\n", localMsg.constData(), context.file, context.line, context.function);
        abort();
    }
}

int main(int argc, char **argv)
{
    qInstallMessageHandler(myMessageOutput);
    QApplication app(argc, argv);
    ...
    return app.exec();
}
```

## 老版本方法: + 写入时间, 写入文件
在QT老版本中, 使用API `qInstallMsgHandler(myMessageOutput);`注册qDebug的回调函数, 例如:

``` C++
#include "mainwindow.h"
#include <QApplication>
#include<QTextCodec>
#include<QMutex>
#include"../CommComponent/CGlobal.h"
#include<time.h>
#include<QFile>
#include<QTextStream>

void myMessageOutput(QtMsgType type, const char *msg)
{
    static QMutex mutex;
    QMutexLocker locker(&mutex);

    QString strFileLog = "debug.log";
    //QString strText = QString("(%1:%2:%3)%4").arg (context.file).arg (context.line).arg (context.function).arg (msg);
    QString strText = QString(msg);


    switch (type) {
    case QtDebugMsg:
        //根据不同的动态库来写log
        if(strText.startsWith (DEBUG_CONTROL_ONE__LOG))
        {
            strFileLog = "Debug_Control_One.log";
        }
        else if(strText.startsWith (DEBUG_TASK_PLANNING_LOG))
        {
            strFileLog = "Debug_Task_Planning.log";
        }
        else if(strText.startsWith (DEBUG_DEVICE_MONITOR_LOG))
        {
            strFileLog = "Debug_Device_Monitor.log";
        }
        else if(strText.startsWith (DEBUG_TCP_LOG))
        {
            strFileLog = "Debug_TCP.log";
        }
        else
        {
            strFileLog = "Debug_Other.log";
        }
        break;
    case QtWarningMsg:
        //根据不同的动态库来写log
        if(strText.startsWith (WARNING_CONTROL_ONE__LOG))
        {
            strFileLog = "Warning_Control_One.log";
        }
        else if(strText.startsWith (WARNING_TASK_PLANNING_LOG))
        {
            strFileLog = "Warning_Task_Planning.log";
        }
        else if(strText.startsWith (WARNING_DEVICE_MONITOR_LOG))
        {
            strFileLog = "Warning_Device_Monitor.log";
        }
        else if(strText.startsWith (WARNING_TCP_LOG))
        {
            strFileLog = "Warning_TCP.log";
        }
        else
        {
            strFileLog = "Warning_Other.log";
        }
        break;
    case QtCriticalMsg:
        //根据不同的动态库来写log
        if(strText.startsWith (CRITICAL_CONTROL_ONE__LOG))
        {
            strFileLog = "Critical_Control_One.log";
        }
        else if(strText.startsWith (CRITICAL_TASK_PLANNING_LOG))
        {
            strFileLog = "Critical_Task_Planning.log";
        }
        else if(strText.startsWith (CRITICAL_DEVICE_MONITOR_LOG))
        {
            strFileLog = "Critical_Device_Monitor.log";
        }
        else if(strText.startsWith (CRITICAL_TCP_LOG))
        {
            strFileLog = "Critical_TCP.log";
        }
        else
        {
            strFileLog = "Critical_Other.log";
        }
        break;
        //崩溃信息
    case QtFatalMsg:
        strFileLog = "Fatal.log";
        break;
    }

    time_t now;
    struct tm*tm_now;
    time(&now);
    tm_now = localtime(&now);

    QString strNow = QString::number(tm_now->tm_year+1900) + "-"
            + QString::number(tm_now->tm_mon+1) + "-"
            + QString::number(tm_now->tm_mday) + " "
            + QString::number(tm_now->tm_hour)+ ":"
            + QString::number(tm_now->tm_min) + ":"
            + QString::number(tm_now->tm_sec);

    // 写文件
    QFile file("log/" + strFileLog);
    // 日志文件大于10M，文件要删除
    if(file.size () > 10000500)
    {
        file.remove ();
    }
    file.open (QIODevice::WriteOnly | QIODevice::Append);
    QTextStream stream(&file);
    stream.setCodec("UTF-8");
    stream << QString("[%1]%2").arg (strNow,strText) << "\r\n";
    file.flush ();
    file.close ();
}

int main(int argc, char *argv[])
{
    QTextCodec::setCodecForCStrings(QTextCodec::codecForName("UTF_8"));
    QTextCodec::setCodecForLocale(QTextCodec::codecForName("UTF_8"));
    QTextCodec::setCodecForTr(QTextCodec::codecForName("UTF_8"));
    QApplication a(argc, argv);
    qInstallMsgHandler(myMessageOutput);
    MainWindow w;
    w.show();
    
    return a.exec();
}

```
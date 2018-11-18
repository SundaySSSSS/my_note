# QT下使用boost
下载并解压boost
加入放到了如下位置
`E:\Develop\Lib\boost_1_67_0`

在pro文件中加入一行`INCLUDEPATH += E:\Develop\Lib\boost_1_67_0`

就可以正常使用boost了
例如:
```C++
#include "mainwindow.h"
#include <QApplication>
#include <QDebug>
#include <boost/timer.hpp>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    boost::timer tmr;
    qDebug() << tmr.elapsed_max() / 3600 << "h" << endl;
    qDebug() << tmr.elapsed_min() << "s" << endl;
    qDebug() << tmr.elapsed() << "S" << endl;
    return a.exec();
}

```
# QT获取程序路径

## 获取程序路径
获取程序所在路径，QCoreApplication 类里就实现了相关的功能：

`QString QCoreApplication::applicationDirPath()`

比如我们有一个程序在：

`C:/Qt/examples/tools/regexp/regexp.exe`

那么 `qApp->applicationDirPath() `的结果是：

`C:/Qt/examples/tools/regexp`

## 当前工作目录
QDir 提供了一个静态函数 currentPath() 可以获取当前工作目录，函数原型如下：

QString QDir::currentPath()
1
如果我们是双击一个程序运行的，那么程序的工作目录就是程序所在目录。

如果是在命令行下运行一个程序，那么运行程序时在命令行的哪个目录，那个目录就是当前目录。
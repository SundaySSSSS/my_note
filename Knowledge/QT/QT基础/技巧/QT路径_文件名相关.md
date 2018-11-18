# QT路径_文件名相关
## 获取程序相关位置
``` C++
QCoreApplication::applicationDirPath();    //获取当前exe所在路径
QDir::currentPath();        //获取当前路径
```

## 获取文件路径中的文件名
``` C++
//获取路径中的文件名
QDir dir = QDir(path);
QString fileName = dir.dirName();
```
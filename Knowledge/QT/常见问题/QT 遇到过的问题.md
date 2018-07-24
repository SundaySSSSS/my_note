# QT 遇到过的问题

## 使用Qt Creater网络编程，出现error: undefined reference to `_imp__WSAStartup@8
原因是socket库的编译链接问题。

解决办法：
错误原因：因为没有链接socket库ws2_32.lib。因此要链接该库
总结：所有运用到WinSock2的程序在编译连接时都要用的该库

在项目的pro文件中追加
```
LIBS += -lpthread libwsock32 libws2_32
```

## 出现The .pro file could not be parsed
通常重启Qt Create可以复归, 但一段时间后再次重现
通常是pro文件的格式出了问题, 去掉多余的空格之类的试试
可按照如下方向进行排查
```
方法一：
把SOURCES HEADERS 参数中的 “\” 都去掉变成下边这样

SOURCES += main.cpp       mainwindow.cpp     hintdialog.cpp
HEADERS  += mainwindow.h     hintdialog.h
1
2
1
2
方法二：
注意SOURCES HEADERS 参数中新加文件前空格数是否为4 的倍数。不是的话，一定显示“The .pro file could not be parsed”
```
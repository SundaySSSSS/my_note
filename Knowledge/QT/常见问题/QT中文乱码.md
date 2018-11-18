# QT中文乱码

如果出现中文乱码问题, 可以考虑在出现中文字符串的文件中加入如下代码:(utf-8为例)
```C++
#pragma execution_character_set("utf-8")
```

之后, 再显示中文就正常了
```C++
QMessageBox message(QMessageBox::Information, "通知", "串口打开成功");
message.exec();
```
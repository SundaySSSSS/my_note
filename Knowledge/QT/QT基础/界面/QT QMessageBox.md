# QT QMessageBox
```C++
QMessageBox message(QMessageBox::Information, "Title", "Content");
message.exec();
```
备注：
这里我们使用的是exec()函数，而不是show()，因为这是一个模态对话框，需要有它自己的事件循环，否则的话，我们的对话框会一闪而过
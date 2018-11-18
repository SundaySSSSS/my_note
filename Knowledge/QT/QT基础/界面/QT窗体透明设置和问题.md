# QT窗体透明设置和问题

```C++
//背景透明
this->setAttribute(Qt::WA_TranslucentBackground);
//设置无边框
this->setWindowFlags(Qt::FramelessWindowHint);
```

如果要注册热键, 必须要在setAttribute(Qt::WA_TranslucentBackground)之后, 否则会导致透明色变成黑色, 原因未知

如:
```C++
    //背景透明
    this->setAttribute(Qt::WA_TranslucentBackground);
    //设置无边框
    this->setWindowFlags(Qt::FramelessWindowHint);

    //注册热键必须在setAttribute(Qt::WA_TranslucentBackground)之后, 否则会导致透明色变成黑色
    m_HotKeyShow = GlobalAddAtom(TEXT("showSyaringan")) - 0xC00;	//获得唯一ID()
    if (!RegisterHotKey((HWND)this->winId(), m_HotKeyShow, MOD_CONTROL, 0))
    {
        QMessageBox message(QMessageBox::Information, "警告", "注册全局热键失败");
        message.exec();
    }
```

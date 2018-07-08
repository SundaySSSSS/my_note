# QT 注册热键

## 基础知识
注册热键使用API: `RegisterHotKey`
卸载热键使用API: `UnregisterHotKey`
QT中截获windows原生消息, 可以重写方法: `nativeEvent`

## 代码示例
h文件
```C++
#ifndef SYARINGANWIDGET_H
#define SYARINGANWIDGET_H

#include <windows.h>
#include <QWidget>
#include <QDebug>
#include <QMessageBox>

namespace Ui {
class SyaringanWidget;
}

class SyaringanWidget : public QWidget
{
    Q_OBJECT

public:
    explicit SyaringanWidget(QWidget *parent = 0);
    ~SyaringanWidget();

private:
    Ui::SyaringanWidget *ui;
    ATOM m_HotKeyShow;
    bool nativeEvent(const QByteArray &eventType, void *message, long *result) override;
};

#endif // SYARINGANWIDGET_H

```

cpp文件
```C++
#include "SyaringanWidget.h"
#include "ui_SyaringanWidget.h"
#include <WinUser.h>
#include "windows.h"

SyaringanWidget::SyaringanWidget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::SyaringanWidget)
{
    ui->setupUi(this);
    //HotKeyId的合法取之范围是0x0000到0xBFFF之间，而GlobalAddAtom函数得到的值在0xC000到0xFFFF之间，所以减掉0xC000来满足调用要求。
    m_HotKeyShow = GlobalAddAtom(TEXT("getMousePoint")) - 0xC00;	//获得唯一ID()
    if (!RegisterHotKey((HWND)this->winId(), m_HotKeyShow, MOD_CONTROL,  VK_F1))
    {
        QMessageBox message(QMessageBox::Information, "Title", "Content");
        message.exec();
    }
}

SyaringanWidget::~SyaringanWidget()
{
    delete ui;
    UnregisterHotKey((HWND)this->winId(), m_HotKeyShow);
    GlobalDeleteAtom(m_HotKeyShow);
}

bool SyaringanWidget::nativeEvent(const QByteArray &eventType, void *message, long *result)
{
    if (eventType == "windows_generic_MSG")
    {
        MSG *msg = (MSG *)message;
        if (msg->message == WM_HOTKEY)
        {
            if (msg->wParam == m_HotKeyShow)
                qDebug() << "hot key pressed";
            return true;
        }
        else
            return QWidget::nativeEvent(eventType, message, result);
    }
    else
        return false;
}

```
# 4_QT_嵌入桌面的窗口
## 用到的知识
1, QWindow
2, 找到桌面窗体的方法FindWindowEx
3, QPainter

## 代码
定义:
注意继承的是QWindow, 不需要ui文件
```C++
#pragma once

#include <QWindow>
#include <QBackingStore>
#include <QEvent>
#include "ui_Syaringan.h"

class Syaringan : public QWindow
{
	Q_OBJECT

public:
	Syaringan(QWindow *parent = Q_NULLPTR);

	bool event(QEvent* e);

private:
	QBackingStore store;
};

```

实现
```C++
#include <windows.h>
#include <QPainter>
#include <QImage>
#include <QDesktopWidget>
#include "Syaringan.h"

static HWND g_workerw = 0;

static BOOL CALLBACK EnumWndCallback(HWND tophandle, LPARAM topparamhandle)
{
	HWND p = FindWindowEx(tophandle, 0, L"SHELLDLL_DefView", 0);
	if (p != 0)
	{
		g_workerw = FindWindowEx(0, tophandle, L"WorkerW", 0);
	}
	return true;
}


Syaringan::Syaringan(QWindow *parent)
	: QWindow(parent), store(this)
{
	HWND hwndProgram = FindWindow(L"Progman", L"Program Manager");
	SendMessageTimeout(hwndProgram, 0x052c, 0, 0, SMTO_NORMAL, 1000, 0);
	EnumWindows(EnumWndCallback, 0);

	if (g_workerw == 0)
	{
		abort();
	}
	QWindow *windowDesktop = QWindow::fromWinId((WId)g_workerw);

	this->setParent(windowDesktop);

	//将窗口全屏
	QDesktopWidget w;
	QRect rectFullDesktop = w.availableGeometry();
	this->setGeometry(rectFullDesktop);
}

bool Syaringan::event(QEvent* e)
{
	if (e->type() == QEvent::Expose || e->type() == QEvent::Resize)
	{
		QImage image("C:/Desktop/20186610215E4.jpg");
		QRect rect(QPoint(0, 0), this->size());
		store.resize(this->size());
		store.beginPaint(rect);
		
		QPainter painter(store.paintDevice());
		painter.fillRect(rect, Qt::white);
		
		painter.drawImage(0, 0, image);
		store.endPaint();
		store.flush(rect);
	}
	return QWindow::event(e);
}
```
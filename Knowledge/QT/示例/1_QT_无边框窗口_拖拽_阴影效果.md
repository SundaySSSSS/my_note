# QT进阶示例
## 无边框窗口
### 实现无边框
建立工程时, 窗口的基类选择QWidget
在QWidget为基类的派生类中, 加入代码
`this->setWindowFlags(Qt::FramelessWindowHint);`
完整代码如下
``` C++
#include "widget.h"
#include "ui_widget.h"

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
    this->setWindowFlags(Qt::FramelessWindowHint);
}

Widget::~Widget()
{
    delete ui;
}
```

### 实现窗口拖拽
窗口拖拽需要覆盖QWidget的三个虚函数
``` C++
void mouseMoveEvent(QMouseEvent *event);
void mousePressEvent(QMouseEvent *event);
void mouseReleaseEvent(QMouseEvent *event);
```

在cpp文件中, 添加坐标计算逻辑
``` C++
void Widget::mousePressEvent(QMouseEvent *event)
{
    QWidget::mousePressEvent(event);
    QPoint screenPos = event->globalPos(); //鼠标相对于整个屏幕的坐标
    QPoint windowPos = this->geometry().topLeft();  //窗口左上角的位置
    this->mouseDragPos = screenPos - windowPos; //鼠标点在窗口中的位置, 利用向量减法可以计算得出
}

void Widget::mouseMoveEvent(QMouseEvent *event)
{
    QWidget::mouseMoveEvent(event);
    QPoint screenPos = event->globalPos(); //在移动中, 获取鼠标相对于整个屏幕的坐标
    QPoint windowPos = screenPos - this->mouseDragPos;
    this->move(windowPos);
}

void Widget::mouseReleaseEvent(QMouseEvent *event)
{
    QWidget::mouseReleaseEvent(event);
    this->mouseDragPos = QPoint();  //放开鼠标时, 重置鼠标拖拽点
}
```

### 实现窗口阴影
外层的Widget不能直接设置阴影, 这里采用的方法为:
将外层的Widget设置为透明, 在窗口中建立一个Widget, 设置阴影特效
具体步骤如下:
1, 在ui设计师界面中拖入一个Widget
2, 新建阴影特效, 赋予拖入的Widget
3, 将背景Widget透明化

核心代码如下:
``` C++
//阴影效果
QGraphicsDropShadowEffect *shadow = new QGraphicsDropShadowEffect();
shadow->setBlurRadius(5);
shadow->setColor(Qt::black);
shadow->setOffset(0);
ui->shadowWidget->setGraphicsEffect(shadow);
// 将主窗口设置为透明
this->setAttribute(Qt::WA_TranslucentBackground);
```





# QT学习笔记
## QT creator中各个文件的作用
.pro 类似于一个工程文件, 用于生成makefile文件
.ui MVC模式中的V(View), 规定了QT工程的外观
## 手动写一个QT工程
第一步: 建立main.cpp
写入如下内容:
``` C++
#include "mainwindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	MainWindow w;
	w.show();

	return a.exec();
}
```
第二步: qmake -project
执行此过程后, 会生成 .pro文件
第三步: qmake
执行此过程后, 会生成makefile文件
第四步: make

## QT的基本类结构
所有类都继承自QObject, 一些自己写的类也需要继承自这个类. 
QObject类只有一个属性: objectName
所有 可见类都继承自QWidget类, QWidget类继承自QObject
所有跟外观相关的属性都可以从QWidget中找到, 例如坐标, 颜色等
字体颜色相关内容可以在styleSheet中找到
## QT Designer
### 改变风格 - styleSheet属性
改变一个控件的风格, 可以使用其父类QWidget的styleSheet属性
注意, 添加颜色时, 需要点击下拉三角指定添加什么颜色(背景色, 字体颜色等), 否则无法确认
## 布局中的问题
### 布局中的占位控件
在做水平和垂直布局时, 有时并不合适, 可以使用Spacers控件.Spacer类似一个弹簧, 放在两个控件之间, 起到占位的作用
### 改变布局的策略
如果想要让布局按照自己的需求变更, 可以修改布局的父类, QWidget中的sizePolicy相关属性
其中的"水平策略", "垂直策略"规定了在控件进行组合时, 优先改变哪个, 那些固定不变
###  改变布局中各控件所占得比例
在Layouts相关类中, 有LayoutStretch属性, 决定了各个控件所占的比例
如果有三个控件, LayoutStretch如果为2,1,2. 表示第一个控件占五分之二, 第二个控件占五分之一, 等
## 窗体大小的控制
### 不允许改变窗体大小
把QWidget父类中的maximumSize中的宽高设置为minimumSize中的一致
这样启动程序后, 鼠标移动到窗体边缘, 已经无法改变窗体大小
在Windows和Linux上, 最大化的按钮会消失, 但Mac有bug, 还是有最大化按钮

# 信号与槽机制
## 绑定槽函数的几种方法
### 1, 手动绑定
#### 声明槽函数
声明槽函数时, 需要使用关键字"slot"
例如:
``` C++
private slots:  // 槽函数
    void login();
    void closeThis();
```

#### 绑定信号和槽函数
connect(谁发出信号, 发出的什么信号, 谁接受信号, 执行的槽函数);
例如:
``` C++
connect(this->ui->btnLogin, SIGNAL(clicked(bool)), this, SLOT(login()));
connect(this->ui->btnCancel, SIGNAL(clicked(bool)), this, SLOT(closeThis()));
```

#### 解除槽函数的绑定
disconnect()参数和connect完全相同

### 2, GUI点击方式绑定
在ui中, 右键点击, 选择"转到槽", 接下来按照提示一步一步来即可
完成后, 会自动生成一个槽函数
这种方法不需要调用connect进行绑定
这种方式是按照固定的规则生成槽函数, 在编译时, 将这种命名的函数进行特殊的解析, 当做槽函数
也就是如果自己写一个函数, 并按照这种规则进行命名, 编译器仍然会把它当做槽函数
### 3, 使用GUI槽编辑器(Signals Slots Editor)
在QT Designer中间, 下方的Signals Slots Editor中进行添加即可
这种方式只能绑定系统的槽函数
并且在代码中没有任何体现
故不推荐此种方法

# QT的Debug
## 打印到控制台
``` C++
#incldue <QDebug>
qDebug() << "something";
```

# 部分控件用法记录
## QLineEdit
### placeholderText属性
类似于提示文本, 在QLineEdit中浅灰色显示, 输入任何文本后立刻隐藏
### clearButtonEnabled属性
是否显示一键清除所有输入信息的按钮, bool类型
##  QComboBox
### 添加条目
直接双击, 在弹出的对话框中添加即可
## QTableView
需要用到的头文件:
``` C++
#include <QStandardItem>
#include <QStandardItemModel>
```

定义数据模型
``` C++
QStandardItemModel* model;
```

向模型中添加表头
``` C++
	model = new QStandardItemModel;
    //设置表头
    model->setHorizontalHeaderItem(0, new QStandardItem("姓名"));
    model->setHorizontalHeaderItem(1, new QStandardItem("学号"));
    model->setHorizontalHeaderItem(2, new QStandardItem("性别"));
    model->setHorizontalHeaderItem(3, new QStandardItem("年龄"));
    model->setHorizontalHeaderItem(4, new QStandardItem("院系"));
    model->setHorizontalHeaderItem(5, new QStandardItem("兴趣"));
    this->ui->tableView->setModel(model);
```

填入表格内容
``` C++
//向表格第一行, 第5列(都是从0开始计数)填入字符串"足球"
this->model->setItem(1, 5, new QStandardItem("足球"));
```

# 界面中的抽象概念
## QButtonGroup 按钮组
许多按钮可以组成一个按钮组, 一旦组成按钮组后, 就可以通过遍历等方法获取到按钮
### 在QT Designer中设置按钮组
选中要组成一组的按钮, 右键->指定到按钮组, 如果没有已经存在的按钮组, 可以新建
这样, 选中的按钮已经处于一个组中, 可以找到该组, 改变名称, 属性等
备注: 如果不想让组内成员互斥(选中一个, 另外一个就不能选中), 可以修改QButtonGroup的exclusive属性
### 使用代码方式设置按钮组
参考帮助手册即可
### QButtonGroup 方法
#### buttons()
返回组内所有的按钮列表, 返回类型为QList<QAbstractButton*> list
#### checkedButton()
如果组内互斥, 可以使用此方法选中当前被选中的按钮, 返回QAbstractButton类型
# 文件操作
## 基本操作
``` C++
void writeToFile(QString str)
{
   QFile file("stu.txt");
    if (!file.open(QIODevice::Append | QIODevice::Text))
    {   //打开失败
        QMessageBox::critical(this, "错误", "文件打开失败, 信息没有保存", "确定");
        return;
    }
    QTextStream out(&file);
    out << str;
    file.close();
}
```

## 备注:
在mac系统中, 如果写文件时不带路径, 则会默认写到程序包中, 
可以在生成的app文件中右键, 选择显示包内容, 在里面能找到操作的文件
# 多窗口
## 添加窗体
在工程上右键, 添加新文件, 模板选择[QT], [QT设计师界面类], 选择窗口模板, 填写类名即可
## 显示窗体
``` C++
MainWindow w;
//w.show(); 这个函数非阻塞
w.exec();//模态视图(除了w以外的窗口都没有响应)
```
如果使用show()函数, 要保证此后窗体对象不会销毁

## show和exec的使用规则
如果弹出窗体不完成, 主界面不想让用户使用, 推荐使用exec
如果弹出窗体后, 主界面还想让用户使用, 推荐使用show
# 菜单栏
## 添加菜单项
主窗体是默认有一个菜单栏的, 直接在[在这里输入]中双击输入内容即可
## 绑定菜单项的信号与槽
### 方法1, connect绑定
用之前的connect方法, 绑定triggered信号即可
### 方法2, 使用Action Editor
在QT Designer中间下方, 有个Action Editor
里面已经把所有菜单项添加进去了
直接在上面右键[转到槽]即可

# 资源
## 使用方法
### 1, 创建资源文件
引用外部资源时, 可以创建QT资源文件
右键创建文件-> QT中的Qt Resource File
完成后, 会产生一个qrc的文件
### 2, 打开资源文件
正常双击在Mac和Linux上是无法打开的, 可以在此文件上右键->Open In Editor
### 3, 添加前缀
前缀就类似于一个分类器, 不同类别的资源放在各个前缀中
前缀必须以/开头, 表示QT的根目录
### 4, 添加资源
再选择添加文件, 添加对应的资源
QT要求资源必须位于工程文件夹内
### 5, 使用资源
使用时, 按照如下规则引用:
冒号 + 前缀 + 资源
例如:
`:/bg/pic/grand.png`
其中前缀名为bg
资源名为`/pic/grand.png`

# 2D绘图
## 整体框架
QGraphicsView容器 -> QGraphicsScene场景 -> QGraphicsItem图元
## 使用方法
### 1, 创建一个QGraphicsView的派生类
具体步骤如下:
#### 1, 在工程上右键, 添加一个C++的类, 让基类指定为QObject.
这一步是必要的, 基类为QObject可以获得信号与槽的能力
这样, 在创建的类中, 会存在一行Q_OBJECT的宏定义, 而手动添加此行是不行的
#### 2, 在新添加的类中, 把基类改成QGraphicsScene
不能通过手动添加Q_OBJECT来获得信号与槽的能力, 原因未知, 必须通过IDE产生的才有效
#### 3, 添加一个图元的派生类
QGraphicsItem图元类是一个虚基类, 有8种派生类
QGraphicsEcllipseItem 椭圆图元
QGraphicsLineItem 线图元
QGraphicsPathItem 曲线图元
QGraphicsPixmapItem 像素图元
QGraphicsPolygonItem 多边形图元
QGraphicsRectItem 矩形图元
QGraphicsSimpleTextItem 文本标签图元
QGraphicsTextItem 文本浏览器图元

在工程上右键, 添加一个基类为QGraphicsPixmapItem的类(这里以QGraphicsPixmapItem为例)
命名为myItem, 既定义了一个自己的图元类



# QT QVariant

QVariant类及QVariant与自定义数据类型转换的方法
这个类型相当于是Java里面的Object，它把绝大多数Qt提供的数据类型都封装起来，起到一个数据类型“擦除”的作用。比如我们的 table单元格可以是string，也可以是int，也可以是一个颜色值，那么这么多类型怎么返回呢？于是，Qt提供了这个QVariant类型，你可以把这很多类型都存放进去，到需要使用的时候使用一系列的to函数取出来即可。比如你把int包装成一个QVariant，使用的时候要用 QVariant::toInt()重新取出来。这里需要注意的是，QVariant类型的放入和取出必须是相对应的，你放入一个int就必须按int取出，不能用toString(), Qt不会帮你自动转换。
数据核心无非就是一个 union，和一个标记类型的type：传递的是整数 123，那么它union存储整数123，同时type标志Int；如果传递字符串，union存储字符串的指针，同时type标志QString。
QVariant 属于 Qt 的Core模块，属于Qt的底层核心之一，ActiveQt、QtScript、QtDeclarative等都严重依赖于QVariant。
 
QVariant 可以保存很多Qt的数据类型，包括QBrush、QColor、QCursor、QDateTime、QFont、QKeySequence、 QPalette、QPen、QPixmap、QPoint、QRect、QRegion、QSize和QString，并且还有C++基本类型，如 int、float等。QVariant还能保存很多集合类型，如QMap<QSTRING, QVariant>, QStringList和QList。item view classes，数据库模块和QSettings都大量使用了QVariant类，，以方便我们读写数据。

## 基本用法
QVariant也可以进行嵌套存储，例如
```
QMap<QString, QVariant> pearMap;
pearMap["Standard"] = 1.95;
pearMap["Organic"] = 2.25;

QMap<QString, QVariant> fruitMap;
fruitMap["Orange"] = 2.10;
fruitMap["Pineapple"] = 3.85;
fruitMap["Pear"] = pearMap;
```

QVariant被用于构建Qt Meta-Object，因此是QtCore的一部分。当然，我们也可以在GUI模块中使用，例如
```
QIcon icon("open.png");
QVariant variant = icon;
// other function
QIcon icon = variant.value<QIcon>();
```
我们使用了value()模版函数，获取存储在QVariant中的数据。这种函数在非GUI数据中同样适用，但是，在非GUI模块中，我们通常使用toInt()这样的一系列to...()函数，如toString()等。

## 自定义QVariant存储类型
　　如果你觉得QVariant提供的存储数据类型太少，也可以自定义QVariant的存储类型。被QVariant存储的数据类型需要有一个默认的构造函数和一个拷贝构造函数。为了实现这个功能，首先必须使用Q_DECLARE_METATYPE()宏。通常会将这个宏放在类的声明所在头文件的下面(Q_DECLARE_METATYPE(MyClass)宏的位置：头文件，类声明后)：

如
```C++
//要使用一个自定义类型可用于QVariant中只需要在类声明的后面加上:Q_DECLARE_METATYPE(), 
struct MyClass
{
QString name;
int age;
}
Q_DECLARE_METATYPE(MyClass)
```

这样我们的类就可以像QMetaType::Type类一样使用没什么不同,有点不同的是使用方法上面只能这样使用.

```C++
MyClass myClass;
QVariant v3 = QVairant::fromValue(myClass);
//
v2.canConvert<MyClass>();
MyClass myClass2 = v2.value<MyClass>();
```

例如：
```C++
Q_DECLARE_METATYPE(BusinessCard)

//然后我们就可以使用：

BusinessCard businessCard;
QVariant variant = QVariant::fromValue(businessCard);
// ...
if (variant.canConvert<BusinessCard>()) {
     BusinessCard card = variant.value<BusinessCard>();
     // ...
}
```

## QVariant与自定义数据类型转换的方法
### 自定类型 -> QVariant
```C++
struct MyStruct
{
    int a;
    char b[10];
};
MyStruct stu;

Q_DECLARE_METATYPE(MyStruct)
```
在程序初始化中，给结构体初始化并存储到QComboBox的data域中：
```C++
bzero(&stu, sizeof(MyStruct)); //stu就是上面声明的全局变量
//赋初值
stu.a = 100;
strcpy(stu.b,"Hello./n");
//类型转换
QVariant v;
QString ss = QString("%1").arg(stu.b);
v.setValue(stu);
//保存到控件data中
ui->cboTest->addItem(ss, v);
ui->cboTest->addItem("aadkjf", 0);
```

### 自定类型 -> QVariant
读取的时候反过来处理，如下：
```C++
QVariant v;
//从控件data域取得variant对象
v = ui->cboTest->itemData(0);
//转换为自定义的结构体实例
MyStruct s = v.value<MyStruct>();
printf("value=%d:%s/n",s.a, s.b);
```
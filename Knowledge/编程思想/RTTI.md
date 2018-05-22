# RTTI[转]
全称为: Run-Time Type Identification
自从1993年Bjarne Stroustrup 提出有关C++ 的RTTI功能之建议﹐以及C++的异常处理(exception handling)需要RTTI；最近新推出的C++ 或多或少已提供RTTI。 然而，若不小心使用RTTI，可能会导致软件弹性的降低

## 什么是RTTI
在C++ 环境中﹐头文件(header file) 含有类之定义(class definition)亦即包含有关类的结构资料(representational information)。但是﹐这些资料只供编译器(compiler)使用﹐编译完毕后并未留下来﹐所以在执行时期(at run-time) ﹐无法得知对象的类资料﹐包括类名称、数据成员名称与类型、函数名称与类型等等。例如﹐两个类Figure和Circle﹐其之间为继承关系。
若有如下指令:
```C++
Figure *p;
p = new Circle();
Figure &q = *p;
```
在执行时, p指向一个对象. 但欲得知此对象之类资料, 就有困难了。同样欲得知q 所参考(reference) 对象的类资料﹐也无法得到。RTTI(Run-Time Type Identification)就是要解决这困难﹐也就是在执行时﹐您想知道指针所指到或参考到的对象类型时﹐该对象有能力来告诉您。随着应用场合之不同﹐所需支持的RTTI范围也不同。最单纯的RTTI包括﹕
- 类识别(class identification)──包括类名称或ID。
- 继承关系(inheritance relationship)──支持执行时期的「往下变换类型」(downward casting)﹐亦即动态变换类型(dynamic casting) 。

在对象数据库存取上﹐还需要下述RTTI:
- 对象结构(object layout) ──包括属性的类型、名称及其位置（position或offset）。
- 成员函数表(table of functions)──包括函数的类型、名称、及其参数类型等。
其目的是协助对象的I/O 和持久化(persistence) ﹐也提供调试讯息等。

若依照Bjarne Stroustrup 之建议. C++ 还应包括更完整的RTTI:
- 能得知类所实例化的各对象 。
- 能参考到函数的源代码。
- 能取得类的有关在线说明(on-line documentation) 。
其实这些都是C++ 编译完成时所丢弃的资料﹐如今只是希望寻找个途径来将之保留到执行期间。然而, 要提供完整的RTTI, 将会大幅提高C++ 的复杂度!

## RTTI可能伴随的副作用
RTTI最主要的副作用是﹕程序员可能会利用RTTI来支持其「复选」(multiple-selection)方法﹐而不使用虚函数(virtual function)方法。
虽然这两种方法皆能达到多态化(polymorphism) , 但使用复选方法, 常导致违反著名的「开放╱封闭原则」(open/closed principle) 。反之﹐使用虚函数方法则可合乎这个原则. 
Circle和Square皆是由Figure所派生出来的子类﹐它们各有自己的draw()函数。当C++ 提供了RTTI﹐就可写个函数如下﹕
```C++
void drawing( Figure *p )
{
    if( typeid(*p).name() == "Circle" )
      ((Circle*)p) -> draw();
    if( typeid(*p).name() == "Rectangle" )
      ((Rectangle*)p) -> draw();
}
```
虽然drawing() 函数也具有多型性, 但它与Figure类体系的结构具有紧密的相关性。当Figure类体系再派生出子类时, drawing() 函数的内容必须多加个if指令。因而违反了「开放/封闭原则」, 如下:
很显然地﹐drawing() 函数应加以修正.
想一想﹐如果C++ 并未提供RTTI﹐则程序员毫无选择必须使用虚函数来支持drawing() 函数的多型性。于是程序员将draw()宣告为虚函数﹐并写drawing() 如下﹕
```C++
void drawing(Figure *p)
{ 
    p->draw();
}
```
如此﹐Figure类体系能随时派生类﹐而不必修正drawing() 函数。亦即, Figure体系有个稳定的接口(interface), drawing() 使用这接口﹐使得drawing() 函数也稳定﹐不会随Figure类体系的扩充而变动。这是封闭的一面。而这稳定的接口并未限制Figure体系的成长, 这是开放的一面。因而合乎「开放╱封闭」原则, 软件的结构会更具弹性, 更易于随环境而不断成长。

## RTTI的常见的使用场合
一般而言﹐RTTI的常见使用场合有四﹕
- 异常处理(exceptions handling)
- 动态转类型(dynamic casting) 
- 模块集成
- 对象I/O
1.异常处理── 大家所熟悉的C++ 新功能﹕异常处理﹐其需要RTTI﹐如类名称等。
2.动态转类型── 在类体系(class hierarchy) 中﹐往下的类型转换需要类继承的RTTI。
3.模块集成── 当某个程序模块里的对象欲跟另一程序模块的对象沟通时﹐应如何得知对方的身分呢? 知道其身分资料﹐才能呼叫其函数。一般的C++ 程序﹐常见的解决方法是──在源代码中把对方对象之类定义（即存在头文件里）包含进来, 在编译时进行连结工作。然而, 像目前流行的主从(Client-Server) 架构中﹐客户端(client)的模块对象﹐常需与主机端(server)的现成模块对象沟通﹐它们必须在执行时沟通﹐但又常无法一再重新编译。于是靠标头文件来提供的类定义资料, 无助于执行时的沟通工作. 只得依赖RTTI了.
4.对象I/O ── C++ 程序常将其对象存入数据库﹐未来可再读取之。对象常内含其它小对象﹐因之在存入数据库时﹐除了必须知道对象所属的类名称﹐也必须知道各内含小对象之所属类﹐才能完整地将对象存进去。储存时﹐也将这些RTTI资料连同对象内容一起存入数据库中。未来读取对象时﹐可依据这些RTTI资料来分配内存空间给对象。

## RTTI从哪里来?
上述谈到RTTI的用途, 以及其副作用。这众多争论, 使得RTTI的标准迟迟未呈现出来。也导致各C++ 开发环境提供者﹐依其环境所需而以各种方式来支持RTTI﹐且其支持RTTI的范围也所不同。 目前常见的支持方式包括﹕ 
- 由类库提供RTTI──例如﹐Microsoft 公司的Visual C++环境。
- 由C++ 编译器(compiler)提供──例如﹐Borland C++ 4.5 版本。
- 由源代码产生器(code generator)提供──例如Bellvobr系统。
- 由OO数据库的特殊预处理器(preprocessor)提供──例如Poet系统。
- 由程序员自己加上去。
这些方法皆只提供简单的RTTI﹐其仅为Stroustrup先生所建议RTTI内涵的部分集合而已。相信不久的将来, 会由C++ 编译器来提供ANSI标准的RTTI

## 程序员自己提供的RTTI 
通常程序员自己可提供简单的RTTI﹐例如提供类的名称或识别(TypeID)。最常见的方法是﹕为类体系定义些虚函数如Type_na() 及Isa() 函数等。请先看个例子﹕
```C++
class Figure { };
class Rectangle : public Figure { };
class Square : public Rectangle
{
    int data;
public:
    Square() { data=88; }
    void Display() { cout << data << endl; }
};

void main()
{
    Figure *f = new Rectangle();
    Square *s = (Square *)f;
    s -> Display();
}
```

这时s 指向Rectangle 之对象﹐而s->Display()呼叫Square::Display() ﹐将找不到data值。若在执行时能利用RTTI来检查之﹐就可发出错误讯息。于是, 自行加入RTTI功能:
```C++
class Figure
{
public:
  virtual char* Type_na() { return "Figure"; }
  virtual int Isa(char* cna) { return !strcmp(cna, "Figure")? 1:0; }
};

class Rectangle:public Figure
{
public:
  virtual char* Type_na() { return "Rectangle"; }
  virtual int Isa(char* cna)  { return !strcmp(cna, "Rectangle")?1 : Figure::Isa(cna); }
  static Rectangle* Dynamic_cast(Figure* fg) { return fg -> Isa(Type_na())?(Rectangle*)fg : 0; }
};

class Square:public Rectangle
{
int data;
public:
Square() { data=88; }
  virtual char* Type_na() { return "Square"; }
  virtual int Isa(char* cna) { return !strcmp(cna, "Rectangle")? 1 : Rectangle::Isa(cna); }
  static Square* Dynamic_cast(Figure *fg)  { return fg->Isa(Type_na())? (Square*)fg : 0; }
  void Display() { cout << "888" << endl; }
};
```

虚函数Type_na() 提供类名称之RTTI﹐而Isa() 则提供继承之RTTI﹐用来支持「动态转类型」函数──Dynamic_cast()。例如:
```C++
Figure *f = new Rectangle();
cout << f -> Isa("Square") << endl;
cout << f -> Isa("Figure") << endl;
```

这些指令可显示出﹕f 所指向之对象并非Square之对象﹐但是Figure之对象（含子孙对象）。再如:
```C++
Figure *f;
Square *s;
f = new Rectangle();
s = Square == Dynamic_cast(f);
if(!s)
    cout << "dynamic_cast error!!" << endl;
```
此时, 依RTTI来判断出这转类型是不对的

## 类库提供RTTI
由类库提供RTTI是最常见的﹐例如Visual C++的MFC 类库内有个CRuntimeClass 类﹐ 其内含简单的RTTI。请看个程序:
```C++
class Figure:public CObject
{
    DECLARE_DYNAMIC(Figure);
};
class Rectangle : public Figure
{
    DECLARE_DYNAMIC(Rectangle);
};
class Square : public Rectangle
{
    DECLARE_DYNAMIC(Square);
    int data;
public:
    void Display() { cout << data << endl; }
    Square() { data=88; }
};
IMPLEMENT_DYNAMIC(Figure, CObject);
IMPLEMENT_DYNAMIC(Rectangle, Figure);
IMPLEMENT_DYNAMIC(Square, Rectangle);
```
Visual C++程序依赖这些宏(Macor) 来支持RTTI。现在就看看如何使用CRuntimeClass类吧﹗如下﹕
```C++
CRuntimeClass *r;
Figure *f = new Rectangle();
r = f->GetRuntimeClass();
cout << r->m_psClassName << endl;
```
这就在执行时期得到类的名称。Visual C++的类库仅提供些较简单的RTTI──类名称、对象大小及父类等。至于其它常用的RTTI如──数据项的类型及位置(position)等皆未提供。

## C++编译器提供RTTI
由C++ 语言直接提供RTTI是最方便了﹐但是因RTTI的范围随应用场合而不同﹐若C++语言提供所有的RTTI﹐将会大幅度增加C++ 的复杂度。目前﹐C++ 语言只提供简单的RTTI﹐例如Borland C++ 新增typeid()操作数以及dynamic_cast<T*>函数样版。请看个程序﹕

现在看看如何使用typeid()操作数
```C++
Figure *f = new Square();
const typeinfo ty = typeid(*f);
cout << ty.name() << endl;
```
这会告诉您: f 指针所指的对象﹐其类名称是Square。
再看看如何使用dynamic_cast<T*>
```C++
Figure *f; Square *s;
f = new Rectangle();
s = dynamic_cast<Sqiare *>(f);
if(!s)
    cout << "dynamic casting error!!" << endl;
```
在执行时﹐发现f 是不能转为Square *类型的。如下指令:
```C++
Figure *f; Rectangle *r;
f = new Square();
r = dynamic_cast<Rectangle *>(f);
if(r) r->Display();
```
这种类型转换是对的。

## RTTI与虚函数表
在C++ 程序中﹐若类含有虚函数﹐则该类会有个虚函数表（Virtual Function Table﹐ 简称VFT ）。为了提供RTTI﹐C++ 就将在VFT 中附加个指针﹐指向typeinfo对象﹐这对象内含RTTI资料.
由于该类所实例化之各对象﹐皆含有个指针指向VFT 表﹐因之各对象皆可取出typeinfo对象而得到RTTI。例如﹐
```C++
Figure *f1 = new Square();
Figure *f2 = new Square();
const typeinfo ty = typeid(*f2);
```
其中`typeid(*f2)`的动作是﹕
1.取得f2所指之对象。
2.从对象取出指向VMF 之指针﹐经由此指针取得VFT 表。
3.从表中找出指向typeinfo对象之指针﹐经由此指针取得typeinfo对象。
这typeinfo对象就含有RTTI了。经由f1及f2两指针皆可取得typeinfo对象. 所以 `typeid(*f2) == typeid(*f1)`

## 总结
RTTI是C++ 的新功能。过去﹐C++ 语言来提供RTTI时﹐大多依赖类库来支持﹐但各类库使用的方法有所不同﹐使得程序的可移植性(portability) 大受影响。然而﹐目前C++ 也只提供最简单的RTTI而已﹐可预见的未来﹐当大家对RTTI的意见渐趋一致时﹐C++ 将会提供更完整的RTTI﹐包括数据项和成员函数的类型、位置(offset)等资料﹐使得C++ 程序更井然有序﹐易于维护。




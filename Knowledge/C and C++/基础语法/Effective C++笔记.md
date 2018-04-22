# Effective C++笔记

## 习惯C++
### 1, 视C++为一个语言联邦
可以视C++由四部分组成:
C
Object-Oriented C++ (面向对象C++)
Template C++ (泛型)
STL
每个部分有自己的规约

### 2, 尽量以const, enum, inline替换#define
原因:
1, 报错时编译器报出的是经过预处理后的错误信息, 宏定义已经被替换, 不好定位错误
2, #define的带参数的宏有很多问题, 不如用inline函数替换

### 3, 尽可能使用const

### 4, 确定对象被使用前已先被初始化

## 构造/析构/赋值运算

### 5, 了解C++默默编写并调用哪些函数
如果定义一个类
```C++
class Empty() {};
```
C++或默默添加构造函数, copy构造函数, 析构函数, =运算符重载
如:
```C++
class Empty()
{
public:
    Empty() { ... }
    Empty(const Empty& rhs) { ... }
    ~Empty() { ... }
    Empty& operator=(const Empty& rhs) { ... }
};
```

### 6, 若不想使用编译器自动生成的函数, 就要明确拒绝
拒绝方法:
将 构造函数, copy构造函数, 析构函数, =运算符重载 定义为私有, 并且不实现

### 7, 为多态基类声明virtual析构函数
如果不声明为virtual, 则在派生对象经由基类指针删除时, 行为未定义!!!
故, 带多态性质的基类应该有一个virtual析构函数

### 8, 别让异常逃离析构函数
如果析构中发生异常, 可以:
方案一: 终止程序
方案二: 吞下异常, 记录日志, 继续运行, 但要承担此风险

### 9, 绝不要在构造和析构中调用virtual函数
基类在构造和析构时, 调用virtual不会调用派生类的, 只会调用基类的, 会引出未定义行为

### 10, 令operator=返回一个reference to *this
例如:
```C++
class Temp
{
public:
    Temp& operator=(const Temp& rhs)
    {
        ...
        return* this;
    }
};
```
这只是个协议, 无强制性. 但推荐如此

### 11, 在operator=中处理"自我赋值"
自我赋值例如: `Temp t; t = t;`
需要在operator=中加入"证同测试", 例如
```C++
class Widget
{
private:
    Bitmap* pb;    //一个Bitmap资源
public:
    Widget& operator = (const Widget& rhs);
};

Widget& Widget::operator = (const Widget& rhs)
{
    if (this == &rhs) return *this;//如果是自我赋值, 什么也不做

    delete pb;
    pb = new Bitmap(*rhs.pb);
    return *this;
}
//也可以用以下实现
Widget& Widget::operator = (const Widget& rhs)
{
    Bitmap* pOrig = pb;
    pb = new Bitmap(*rhs.pb);    //保证不使用被删除的资源
    delete pOrig;
    return *this;
}
```

### 12, 复制对象时勿忘其每一个成分
自己写拷贝构造函数, 如果忘记复制某个成分, 编译器不会发出任何警告
需要复制的对象有:
所有local成员变量
调用所有基类中的拷贝构造进行复制

## 资源管理
### 13, 以对象管理资源
1, 获得资源后立刻放进管理对象(managing object)中
2, 管理对象利用析构函数确保资源被释放
可以使用智能指针来管理资源
例如shared_ptr和auto_ptr, 推荐前者. 因为copy行为比较直观, 若选择auto_ptr, 复制动作会使被复制物指向NULL

### 14, 在资源管理类中小心coping行为
在发生复制时, 可以采取:
1, 禁止复制
2, 施行引用计数法

### 15, 在资源管理类中提供对原始资源的访问
现存的API往往要求访问原始资源, 资源管理类需要提供访问方法
最好要求用户主动调用访问原始资源的接口

### 16, 成对使用new和delete时要采用相同的形式
`int* a = new int[100];`要和`delete[] a;`配套

### 17, 以独立语句将new出来的对象放入智能指针中
独立语句可以保证此语句执行完, new的对象一定已经存在
而在复合语句中, 当先后顺序无法保证时, 可能导致引用空资源

## 设计与声明
### 18, 让接口容易被正确使用, 不易被误用
限制类型, 束缚对象值, 等方法可以防止客户传入错误的参数
使用智能指针可以防止资源泄漏

### 19, 设计class犹如设计type

### 20, 函数参数最好用 常引用 替换 值传递
1, 为了减少调用拷贝构造带来的性能损失
2, 值传递不会产生多态, 当传入派生类对象时, 会发生对象切割, 强制切割成基类对象

### 21, 必须返回对象时, 不要妄想返回引用
1, 会发生引用指代不存在的对象, 例如:
```C++
const Rational& operator*(const Rational& lhs, const Rational& rhs)
{
    Rational result(lhs.n * rhs.n, lhs.d * rhs.d);    //计算分数...
    return result;    //!!!错误, 函数调用结束后, result不再存在, 返回的引用也会失去意义
}
```
2, 返回的对象难以删除
```C++
const Rational& operator*(const Rational& lhs, const Rational& rhs)
{
    Rational* result = new Rational(lhs.n * rhs.n, lhs.d * rhs.d);    //计算分数...
    return *result;    //!!!警告, 函数返回的result指向的资源难以删除
}
```

### 22, 将成员变量声明为private
成员变量就应该是private的!

### 23, 最好用non-member, non-friend函数替换member函数
例如: 一个网页浏览器类
```C++
class WebBrowser
{
    void clearCache();
    void clearHistory();
    void removeCookies();
};
```
当用户想要清除所有信息时, 最好使用如下方式:
```C++
void clearBrowser(WebBrowser &wb)
{
    wb.clearCache();
    wb.clearHistory();
    wb.removeCookies();
}
```
而不是制造一个功能相同的成员函数, 或用友元实现

### 24, 若所有参数都需要类型转换, 请使用non-member函数
目前还一知半解

### 25, 写出不抛出异常的swap函数
当`std::swap`对自定义的类型效率不高时, 可以提供一个自己的特化swap, 并保证不抛出异常

## 实现
### 26, 尽可能延后变量定义出现的时间
在变量非用不可的时候, 再去定义它
否则, 可能因为提前退出而白白构造没有被使用的变量
比如:
```C++
string func(int a)
{
    string result;
    if (a == 0)
        return;    //如果程序再此退出, 则result就白构造了
    result = "123";
    return result;
}
```

### 27, 尽量少做转型
1, 尽量不做转型
2, 尽量用C++风格的转型

### 28, 避免返回handles指向对象的内部成分
可能破坏封装, 导致const仅仅是个谎言
```C++
class Point
{
public:
    Point(int x, int y);
    void setX(int newVal);
    void setY(int newVal);
};

struct RectData
{
    Point ulhc;//upper left hand corner
    Point lrhc;//lower right hand corner
};

class Rectangle
{
private:
    std::tr1::shared_ptr<RectData> pData;
public:
    Point& upperLeft() const { return pData->ulhc; }
};

const Rectange rec(Point(0, 0), Point(100, 100));
rec.upperLeft().setX(50);    //!!!通过const方法upperLeft最终修改了矩形坐标
```

### 29, 努力实现"异常安全"
异常安全是指:
在抛出异常时, 不会发生以下行为:
1, 不泄漏任何资源
2, 不允许引用非法资源

"异常安全"提供如下三个保证之一
1, 基本承诺: 如果异常抛出, 程序内的任何事物仍然在有效状态下. 没有任何对象或数据结构被破坏. 但程序的状态不能保证
2, 强烈保证. 如果异常被抛出, 程序状态不改变. 即如果调用成功, 则完全成功, 如果调用失败, 则回复到调用函数之前的状态
3, 不抛出异常保证. 承诺不会抛出任何异常

### 30, 透彻理解inline
1, inline只是向编译器发出申请. 编译器不保证进行内联
2, 将大多数inline限制在小型的, 被频繁调用的函数上

### 31, 将文件间的编译依存关系降至最低
由于C++天生在类声明中存在太多细节(各种成员变量定义等)
依赖于声明式, 不依赖于定义式
可用的手段:
#### 实现类和提供接口类分离
实现类(下例为PersonImpl)和提供接口的类(Person)分离, 只对外暴露提供接口的类(Person)
例如:
```C++
class PersonImpl;    //Person实现类
class Date;
class Address;

class Person
{
public:
    Person(const string& name, const Date& birthday, const Address& addr);
    string getName();
    string getDate();
    string getAddress();
private:
    std::tr1::share_ptr<PersonImpl> pImpl;    //PersonImpl是真正实现功能的类
};
```

#### 构造抽象类作为接口
接口
```C++
class Person
{
public:
    virtual ~Person();
    virtual string getName() = 0;
    virtual string getDate() = 0;
    virtual string getAddress() = 0;
    static std::tr1::shared_ptr<Person> create(const string& name, const Date& birthday, const Address &addr);
};
```

实体
```C++
class RealPerson: public Person
{
public:
    RealPerson(const string& name, const Date& birthday, const Address& addr): theName(name), theBirthDate(birthday), theAddress(addr) {  }
    virtual ~RealPerson() {  }
    string getName() const { ... }
    string getDate() const { ... }
    string getAddress() const { ... }
private:
    stirng theName;
    Date theBirthDate;
    Address theAddress;
};
```

实现接口Person中的create的方法
```C++
static std::tr1::shared_ptr<Person> Person::create(const string& name, const Date& birthday, const Address &addr)
{
    return std::tr1::shared_ptr<Person>(new RealPerson(name, birthday, addr);
}
```

客户使用方法
```C++
int main(int argc, char* argv[])
{
    Date dateOfBirth;
    Address address;
    
    std::tr1::shared_ptr<Person> pp(Person::create(name, dateOfBirth, address));
    cout << pp->getName() << endl << pp->getDate() << endl << pp->getAddress() << endl;
    return 0;
}
```

## 继承与面向对象设计
### 32, 确定你的public继承是is-a的关系
仔细辨认is-a关系, 很容易把不是is-a的关系看做is-a
比如, 如果让矩形Rectange是正方形Square的基类, 表面上看问题不大
但是, 如果有如下方法:
```C++
void makeBigger(Rectange& rect)
{
    int old_height = rect.height;
    rect.width += 10;    //增加了宽度
    assert(old_height == rect.height);    //发生问题
}
```
当出入的为square的引用时, assert异常, 因为正方形宽高保持一致, 不能单独增加一边

### 33, 避免覆盖继承而来的名称
派生类中的名字会覆盖基类的名字, 即使它们参数不同

### 34, 区分接口继承和实现继承
参考一个例子:
```C++
class Shape
{
public:
    virtual void draw() const = 0;
    virtual void error(const std::string& msg) { std::cout<<msg<<std::endl; };
    int objectId() const;
};
class Rectangle: public Shape { ... };
class Eclipse: public Shape { ... };
```
纯虚函数 - 只继承函数的接口, 例如上面的`draw`函数
非纯虚函数 - 继承接口, 并继承实现, 例如上面的`error`函数, 可以由派生类实现一个error函数, 也可以缺省使用Shape的
非虚函数 - 不打算在派生类中有不同的行为, 例如Shape中的`objectId`

### 35, 考虑virtual函数以外的其他选择
一种思路是使用 非虚函数实现类似virtual的效果
例如:
```C++
class GameCharacter
{
public:
    int healthValue() const
    {
        int retVal = doHealthValue();    //此函数是虚的
        return retVal;
    }
private:
    virtual int doHealthValue() const
    {
        ...
    }
};
```
外界调用`healthValue`来实现多态
此方法仅供参考

### 36, 绝不重新定义继承而来的非virtual函数
显然如此

### 37, 绝不重新定义继承而来的默认值
```C++
class Shape
{
public:
    virtual void draw(int a = 3) const = 0;
};

class Rectangle: public Shape
{
    //void draw(int a = 5); // <------- 不推荐
    void draw(int a);
};
```
如果在Rectangle中将draw的默认参数改为5, 则
```
Shape *p = new Rectangle();
p->draw();
```

`p->draw();`中的a被设置为了3

### 38, 通过组合实现has-a和is-implemented-in-term-of(根据某物实现出)
显然如此

### 39, 明智而审慎的地使用private继承
private继承: 基类中的任何成员, 在派生类中都不可访问

private不意味着is-a的关系!!!
编译器不会把派生类的对象 转换为 一个基类对象 !!!!(和public继承不同)

private实际体现的是一种is-implemented-in-term-of(根据某物实现出)的关系
而这种关系是可以通过组合来实现的
故组合是可以替代私有继承的

private继承可以重新定义继承而来的virtual函数, 来协助某个类的实现, 见下面条款中的例子

### 40, 明智而审慎的使用多重继承
多重继承可能从多个基类中继承相同的名称, 从而导致歧义
    解决方法: 明确指定需要哪个`derived.BASE1::ambiguityFunction()`

Java和C#中存在接口, C++可以用抽象类来实现接口的功能, 
C++可以通过多继承来继承多个接口

强烈不推荐让继承关系出现"可怕的菱形继承关系", 除非真的必要

多重继承的正当用法:
1, public继承某个Interface class
2, private继承某个协助实现的class
如下例:
一个接口
```C++
class IPerson
{
public:
    virtual ~IPerson();
    virtual string getName() const = 0;
    virtual string getBirthDate() const = 0;
};
```

一个协助实现的类
```C++
class PersonInfo
{
public:
    explicit PersonInfo(int pid);
    virtual ~PersonInfo();
    virtual const string theName() const;
    virtual const string theBirthDate() const;
    virtual const string valueDelimOpen() const;    //返回括号的开始
    virtual const string valueDelimClose() const;    //返回括号的结束
};
```

最终真正使用的实体类
```C++
class CPerson: public IPerson, private PersonInfo
{
public:
    explicit CPerson(int pid) : PersonInfo(pid) {  }
    virtual string getName() const { return PersonInfo::theName(); }
    virtual string birthDate() const
    {
        return valueDelimOpen() +  PersonInfo::theBirthDate() + valueDelimClose();
    }
private:
    const string valueDelimOpen() const { return "["; }
    const string valueDelimClose() const { return "]"; }
};
```

## 模板和泛型编程
### 41, 了解隐式接口和编译期多态
C++中, 除了使用对象引用, 指针, 还可以使用模板来实现多态
对于模板而言, 接口是隐式的, 多态发生在编译期间
```C++
template<typename T>
void doProcessing(T& w)
{
    if (w.size() > 10 && w != someNastyWidget)
    {
        T temp(w);
        temp.normalize();
        temp.swap(w);
    }
}
```
上例中, T需要存在的接口有: size, normalize, swap, 要支持 !=运算等等
故接口是隐式的, 没有被明确列出
而模板的多态也是在编译期间的, 如果使用了不支持上面接口的对象, 则会在编译时报错

### 42, 了解typename的双重意义
1, 第一重意义: 声明模板
在声明模板时, class关键字和typename关键字的意义完全相同
如下两句意义完全相同
```C++
template<class T> class Temp;
template<typename T> class Temp;
```
2, 指明嵌套从属类型名称
例如:
```C++
template<typename C>
void print2nd(const C& container)
{
    if (container.size() >= 2)
    {
        typename C::const_iterator iter(container.begin()); //如果不加typename, 会报错
        ...
    }
}
```
上面不加typename关键字将无法通过编译, 因为默认情况, `C::const_iterator`会被解释为成员, 而非类型

### 43, 学习处理模板化基类内名称
如果基类是模板类, 则它的派生类中无法直接调用基类的方法, (因为那时编译器并不知道继承什么样的类), 可以通过`this->`来调用基类的成员

### 44, 将与参数无关的代码抽离templates
Templates生成多个class和多个函数, 所以任何template代码都不该与某个造成膨胀的template参数产生依赖关系

### 45, 运用成员函数模板接受所有兼容类型

### 46, 需要类型转换时, 请为模板定义非成员函数

### 47, 请使用traits classes表现类型信息

### 48, 认识template元编程

## 定制new和delete
### 49, 了解new_handler的行为
C++允许在new抛出异常前, 执行用户指定的错误处理函数, 即new_handler
C++原型为: 
```C++
namespace std
{
    typedef void (*new_handler) ();
    new_handler set_new_handler(new_handler p) throw();
}
```
使用`new_handler`的方法
```C++
void outOfMem()
{
    cerr << "Unable to satisfy request for memory\n" << endl;
    abort();
}

int main()
{
    set_new_handler(outOfMem);
    int* pBigDataArray = new int[100000000L];
}
```

当operator new无法满足内存申请时, 它会不断调用`new_handler`函数直到找到足够的内存
故一个好的`new_handler`需要做一下事情
1, 让更多内存可用
2, 如果自己搞不出更多内存, 使用`set_new_handler`来注册一个能搞定的new_handler函数
3, 实在搞不定, 卸载`new_handler`(让`set_new_handler(NULL)`). 使C++抛出异常
4, 抛出`bad_alloc`, 这样的异常不会被operator new捕获, 因此会被传播到内存索取处
5, 不返回, 调用abort或exit

### 50, 了解new和delete的合理替换时机
合适替换new和detele?
1, 检测运行错误时(很多内存泄露检测软件即使用此方法)
2, 用以强化效能. 比如, 特殊场景, 基本只用小内存块, 就可以改造算法, 让new小内存很快, 及时new大内存慢一点也无所谓了
3, 为了收集统计数据

### 51, 编写new和delete时要遵守规则
1, operator new中应该含有一个无穷循环, 在其中尝试分配内存, 如果无法满足要求, 调用new_handler.
2, operator new要能处理0 bytes申请
3, delete要在输入NULL指针时什么也不做

### 52, 写了placement new也要写placement delete

### 53, 不要忽视编译器警告
理应如此

### 54, 让自己熟悉包括TR1在内的标准程序库
TR1期Technical Report 1 , 是一份分档, 宣告了C++11的到来

### 55, 让自己熟悉boost
boost是一个社群, 致力于免费, 开源的C++程序开发
但boost很难安装, 用起来问题多多....


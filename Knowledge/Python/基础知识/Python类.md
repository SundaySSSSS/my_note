# Python类

## 类的定义
```
class ClassName:
	#构造方法
	def __init__(self):
		pass
	def func(self):
		pass
```
## 继承
```
#定义父类
class Parent:
	def hello(self):
		print("parent function")

#子类的方法会覆盖父类的方法
class Child1(Parent):
	def hello(self):
		print("child function")

#直接继承父类的方法
class Child2(Parent):
	pass

p = Parent()
p.hello()
c1 = Child1()
c1.hello()
c2 = Child2()
c2.hello()
```
## 调用父类的方法
```
import random as r
class Fish:
	def __init__(self):
		self.x = r.randint(0, 10)
		self.y = r.randint(0, 10)
		
class Shark(Fish):
	def __init__(self):
		#调用父类的方法
		Fish.__init__(self)
		#等价于上面的
		super().__init__()
		self.z = r.randint(0, 10)
		
fish = Fish()
shark = Shark()
```

## 多重继承
```
class Base1:
        def func1(self):
                print("I am base1")

class Base2:
        def func2(self):
                print("I am base2")

class C(Base1, Base2):
        pass

c = C()
c.func1()
c.func2()
```

## 组合（一个类中有其他类的对象）
```
class Student:
        def __init__(self, num):
                self.num = num

class Teather:
        def __init__(self, num):
                self.num = num

class ClassRoom:
        def __init__(self, stu_num, tea_num):
                self.student = Student(stu_num)
                self.teather = Teather(tea_num)

        def print_num(self):
                print("教室里总共有%d个学生，%d个教师" % (self.student.num, self.teather.num))

cr = ClassRoom(10, 1)
cr.print_num()
```
#小tips：如果属性的名字和方法名字相同，属性会覆盖方法

## 一些相关BIF

### issubclass(class, classinfo)
```
#检查class 是不是classinfo的子类（自身认为是自身的子类）
class A:
	pass
class B(A):
	pass
class C:
        def __init__(self, x = 10):
                self.x = x

print(issubclass(B, A))
print(issubclass(B, B))
print(issubclass(B, object))
#上面的都返回True
```

### isinstance(object, classinfo)
```
#检查object是不是classinfo的一个对象
b1 = B()
print(isinstance(b1, B))
print(isinstance(b1, A))
print(isinstance(b1, C))
```
### hasattr(object, name)
```
#测试object中有没有叫做name的属性名
c1 = C()
print(hasattr(c1, 'x'))
```
### getattr(object, name[, default])
```
#得到object的属性的值
print(getattr(c1, 'x'))
print(getattr(c1, 'y', '找不到！'))
```
### setattr(object, name, value)
```
#设置object中名字为name的属性的值为value，如果没有这个属性，则会新建一个。。。
setattr(c1, 'y', 'this is y')
print(getattr(c1, 'y', '找不到！'))
```
### delattr
```
#删除属性
delattr(c1, 'y')
print(getattr(c1, 'y', '找不到！'))
```
### property(fget=None, fset=None, fdel=None, doc=None)
```
#通过属性来设置属性
class C:
        def __init__(self, size = 10):
                self.size = size
        def getSize(self):
                return self.size
        def setSize(self, value):
                self.size = value
        def delSize(self):
                del self.size
        #生成一个属性x，用getSize来取得它的值，用setSize来设定值，用delSize来删除
        x = property(getSize, setSize, delSize)
                
c1 = C()
print(c1.getSize())
print(c1.x)
c1.x = 18
print(c1.getSize())
```

## 构造方法

### `__init(self[, ...])`
在对象实例化的时候，会调用__init__方法，init方法一定返回None
但是，__init__并不是在实例化时第一个被调用的方法，第一个为__new__

### `__new__(cls[, ...])`
这是在实例化时第一个被调用的方法，通常返回此类的对象，很少重写该方法
例子
```
#CapStr继承str类，功能为变大写。str是不可修改的，所以要
class CapStr(str):
        def __new__(cls, string):
                string = string.upper()
                return str.__new__(cls, string)

a = CapStr("it is a __new__ test")
print(a)
```

## 析构方法
```
#__del__(self)
#对象销毁时自动被调用，通常不需要主动调用，通常在系统垃圾回收时自动被调用
#例子：
class C:
        def __init__(self):
                print("init")
        def __del__(self):
                print("del")

c1 = C()
c2 = c1
c3 = c1
del c3
print("after del c3")
del c2
print("after del c2")                
del c1
print("after del c1")
```

## 运算符重载
### 算数运算的重载
__add__(self, other)
__sub__(self, other)
__mul__(self, other)   乘法
__truediv__(self, other)       真除行为/
__floordiv__(self, other)      整数除法//
__mod__(self, other)   取模运算 %
__pow__(self, other)   指数运算**
#例子
```
class NewInt(int):
        def __add__(self, other):
                return int.__add__(self, other)
        def __sub__(self, other):
                return int.__add__(self, other)

a = NewInt(3)
b = NewInt(5)
print(a + b)
```

小心下面这种无限递归的错误使用
```
class Try_int(int):
        def __add__(self, other):
                return self + other
        def __sub__(self, other):
                return self - other

a = Try_int(3)
b = Try_int(5)
print(a + b)
```

报复一下社会, 将加法重载为减法
```
class int(int):
        def __add__(self, other):
                return int.__sub__(self, other)

a = int('5')
b = int('3')
print(a + b)
```

### 反运算
#例子，a + b调用时，如果a没有__add__时，就会调用b的反运算__radd__
```
class Nint(int):
        def __radd__(self, other):
                return int.__sub__(self, other)

a = Nint(5)
b = Nint(3)
print(a + b)
#8
print(1 + b)
#2
#这里1没有__add__方法，于是调用了b的__radd__方法，所以为2
```

反运算通常为正常运算前面加r
例子：__add__, __radd__

### 增量赋值的重载+= -= *= /= //= ...
`__iadd__(self, other)`
`__isub__(self, other)`等

### 一元操作
`__neg__(self)`
`__abs__(self)`等

### `__str__`和`__repr__`
例如:
```
class A:
        def __str__(self):
                return 'I am A!!!'

a = A()
print(a)
class B():
        def __repr__(self):
                return "I am B!!!"

b = B()
print(b)
```

## 综合实例
做一个计时器
```
import time as t
class MyTimer:
        def __init__(self):
                self.unit = ['年', '月', '天', '小时', '分', '秒']
                self.prompt = '未开始计时'
                self.offset = []
                self.start_time = 0
                self.stop_time = 0
                
        def __str__(self):
                return self.prompt

        def __add__(self, other):
                prompt = "总共运行了:"
                result = []
                for index in range(6):
                        result.append(self.offset[index] + other.offset[index])
                        if result[index]:
                                prompt += str(result[index]) + self.unit[index]
                return prompt

        __repr__ = __str__
        
        #开始计时
        def start(self):
                self.start_time = t.localtime()
                print('计时开始')
        #结束时间
        def stop(self):
                self.stop_time = t.localtime()
                self._calc()
                print('计时结束')
        #内部方法，计算运行时间
        def _calc(self):
                self.offset = []
                self.prompt = '总共运行了：'
                #localtime得到一个结构体，前六个数据记录了年月日时分秒
                for index in range(6):
                        self.offset.append(self.stop_time[index] - self.start_time[index])
                        if self.offset[index] != 0:
                                self.prompt += str(self.offset[index]) + self.unit[index]
```
## 属性访问
#__getattr__(self, name)        用户试图获取一个不存在的属性时的行为
#__getattribute__(self, name)   类的属性被访问时的行为
#__setattr__(self, name, value) 一个属性被设置时的行为
#__delattr__(self, name)        一个属性被删除时的行为
#参考下面的例子
```
class C:
        def __getattr__(self, name):
                print("__getattr__")

        def __getattribute__(self, name):
                print("__getattribute__")
                return super().__getattribute__(name)
        
        def __setattr__(self, name, value):
                print("__setattr__")
                return super().__setattr__(name, value)
        
        def __delattr__(self, name):
                print("__delattr__")
                return super().__delattr__(name)
        
c = C()
c.x
c.x = 1
c.x
```

## 描述符，将某种特殊类型的类的实例指派给另一个类的属性
`__get__(self, instance, owner)` 用于访问属性，它返回属性
`__set__(self, instance, value)` 在属性分配操作中调用，不返回任何内容
`__delete__(self, instance) `    控制删除操作，不返回任何内容
例子
```
class MyDecriptor:
        def __get__(self, instance, owner):
                print("getting...", self, instance, owner)
        def __set__(self, instance, value):
                print("setting...", self, instance, value)
        def __delete__(self, instance):
                print("deleting", self, instance)

class Test:
        x = MyDecriptor()

test = Test()
test.x
#getting... <__main__.MyDecriptor object at 0x03350470> <__main__.Test object at 0x03350490> <class '__main__.Test'>
test.x = 100
#setting... <__main__.MyDecriptor object at 0x03430470> <__main__.Test object at 0x03430490> 100
del test.x
#deleting <__main__.MyDecriptor object at 0x033C3470> <__main__.Test object at 0x033C3490>

class MyProperty:
        def __init__(self, fget=None, fset=None, fdel=None):
                self.fget = fget
                self.fset = fset
                self.fdel = fdel

        def __get__(self, instance, owner):
                return self.fget(instance)
        def __set__(self, instance, value):
                self.fset(instance, value)
        def __delete__(self, instance):
                self.fdel(instance)

class C:
        def __init__(self):
                self._x = None
        def getX(self):
                return self._x
        def setX(self, value):
                self._x = value
        def delX(self):
                del self._x
        #使用x来干预_x
        x = MyProperty(getX, setX, delX)

c = C()
c.x = 'this is x'
print(c.x)
print(c._x)

```

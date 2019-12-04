# Python闭包
## 定义
如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包(closure).
``` python
def ExFunc(n):
    sum=n
    def InsFunc():
        return sum+1
    return InsFunc

myFunc=ExFunc(10)
myFunc()
myAnotherFunc=ExFunc(20)
myAnotherFunc()

```
结果为： 11，21
ExFunc函数只是返回了内嵌函数InsFunc的地址，在执行InsFunc函数时将会由于在其作用域内找不到sum变量而出 错。而在函数式语言中，当内嵌函数体内引用到体外的变量时，将会把定义时涉及到的引用环境和函数体打包成一个整体（闭包）返回

``` python
>>>def addx(x):  
>>>    def adder(y): return x + y  
>>>    return adder  
>>> c =  addx(8)  
>>> type(c)  
<type 'function'>  
>>> c.__name__  
'adder'  
>>> c(10)  
18  
```

## 作用
闭包主要是在函数式开发过程中使用。以下介绍两种闭包主要的用途。

### 用途1
当闭包执行完后，仍然能够保持住当前的运行环境。
比如说，如果你希望函数的每次执行结果，都是基于这个函数上次的运行结果。我以一个类似棋盘游戏的例子来说明。假设棋盘大小为50*50，左上角为坐标系原点(0,0)，我需要一个函数，接收2个参数，分别为方向(direction)，步长(step)，该函数控制棋子的运动。棋子运动的新的坐标除了依赖于方向和步长以外，当然还要根据原来所处的坐标点，用闭包就可以保持住这个棋子原来所处的坐标。

``` python
origin = [0, 0]  # 坐标系统原点
legal_x = [0, 50]  # x轴方向的合法坐标
legal_y = [0, 50]  # y轴方向的合法坐标
def create(pos=origin):
    def player(direction,step):
        # 这里应该首先判断参数direction,step的合法性，比如direction不能斜着走，step不能为负等
        # 然后还要对新生成的x，y坐标的合法性进行判断处理，这里主要是想介绍闭包，就不详细写了。
        new_x = pos[0] + direction[0]*step
        new_y = pos[1] + direction[1]*step
        pos[0] = new_x
        pos[1] = new_y
        #注意！此处不能写成 pos = [new_x, new_y]，原因在上文有说过
        return pos
    return player

player = create()  # 创建棋子player，起点为原点
print player([1,0],10)  # 向x轴正方向移动10步
print player([0,1],20)  # 向y轴正方向移动20步
print player([-1,0],10)  # 向x轴负方向移动10步
```

输出为
```
[10, 0]
[10, 20]
[0, 20]
```
### 用途2
闭包可以根据外部作用域的局部变量来得到不同的结果，这有点像一种类似配置功能的作用，我们可以修改外部的变量，闭包根据这个变量展现出不同的功能。比如有时我们需要对某些文件的特殊行进行分析，先要提取出这些特殊行。
``` python
def make_filter(keep):
    def the_filter(file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        filter_doc = [i for i in lines if keep in i]
        return filter_doc
    return the_filter
```
如果我们需要取得文件"result.txt"中含有"pass"关键字的行，则可以这样使用例子程序
``` python
filter = make_filter("pass")
filter_result = filter("result.txt")
```
以上两种使用场景，用面向对象也是可以很简单的实现的，但是在用Python进行函数式编程时，闭包对数据的持久化以及按配置产生不同的功能，是很有帮助的。
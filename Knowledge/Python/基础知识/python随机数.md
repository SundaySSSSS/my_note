# Python中的random模块
Python中的random模块用于生成随机数。下面介绍一下random模块中最常用的几个函数。

`random.random`
`random.random()`用于生成一个0到1的随机符点数: 0 <= n < 1.0

random.uniform
　　random.uniform的函数原型为：random.uniform(a, b)，用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。如果a > b，则生成的随机数n: a <= n <= b。如果 a <b， 则 b <= n <= a。

print random.uniform(10, 20)  
print random.uniform(20, 10)  
#---- 结果（不同机器上的结果不一样）  
#18.7356606526  
#12.5798298022  
print random.uniform(10, 20) print random.uniform(20, 10) #---- 结果（不同机器上的结果不一样） #18.7356606526 #12.5798298022
random.randint
　　random.randint()的函数原型为：random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b

print random.randint(12, 20)  #生成的随机数n: 12 <= n <= 20  
print random.randint(20, 20)  #结果永远是20  
#print random.randint(20, 10)  #该语句是错误的。下限必须小于上限。  
print random.randint(12, 20) #生成的随机数n: 12 <= n <= 20 print random.randint(20, 20) #结果永远是20 #print random.randint(20, 10) #该语句是错误的。下限必须小于上限。
random.randrange
　　random.randrange的函数原型为：random.randrange([start], stop[, step])，从指定范围内，按指定基数递增的集合中 获取一个随机数。如：random.randrange(10, 100, 2)，结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效。

random.choice
　　random.choice从序列中获取一个随机元素。其函数原型为：random.choice(sequence)。参数sequence表示一个有序类型。这里要说明 一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence。有关sequence可以查看python手册数据模型这一章。下面是使用choice的一些例子：

print random.choice("学习Python")   
print random.choice(["JGood", "is", "a", "handsome", "boy"])  
print random.choice(("Tuple", "List", "Dict"))  
print random.choice("学习Python") print random.choice(["JGood", "is", "a", "handsome", "boy"]) print random.choice(("Tuple", "List", "Dict"))
random.shuffle
　　random.shuffle的函数原型为：random.shuffle(x[, random])，用于将一个列表中的元素打乱。如:

p = ["Python", "is", "powerful", "simple", "and so on..."]  
random.shuffle(p)  
print p  
#---- 结果（不同机器上的结果可能不一样。）  
#['powerful', 'simple', 'is', 'Python', 'and so on...']  
p = ["Python", "is", "powerful", "simple", "and so on..."] random.shuffle(p) print p #---- 结果（不同机器上的结果可能不一样。） #['powerful', 'simple', 'is', 'Python', 'and so on...']
random.sample
　　random.sample的函数原型为：random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
slice = random.sample(list, 5)  #从list中随机获取5个元素，作为一个片断返回  
print slice  
print list #原有序列并没有改变。  
 

 
```
随机整数：
>>> import random
>>> random.randint(0,99)
21

随机选取0到100间的偶数：
>>> import random
>>> random.randrange(0, 101, 2)
42

随机浮点数：
>>> import random
>>> random.random()
0.85415370477785668
>>> random.uniform(1, 10)
5.4221167969800881

随机字符：
>>> import random
>>> random.choice('abcdefg&#%^*f')
'd'

多个字符中选取特定数量的字符：
>>> import random
random.sample('abcdefghij',3) 
['a', 'd', 'b']

多个字符中选取特定数量的字符组成新字符串：
>>> import random
>>> import string
>>> string.join(random.sample(['a','b','c','d','e','f','g','h','i','j'], 3)).r
eplace(" ","")
'fih'

随机选取字符串：
>>> import random
>>> random.choice ( ['apple', 'pear', 'peach', 'orange', 'lemon'] )
'lemon'

洗牌：
>>> import random
>>> items = [1, 2, 3, 4, 5, 6]
>>> random.shuffle(items)
>>> items
[3, 2, 5, 6, 4, 1]
```


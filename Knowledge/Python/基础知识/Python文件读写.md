# Python文件读写
## 1.open
使用open打开文件后一定要记得调用文件对象的close()方法。比如可以用try/finally语句来确保最后能关闭文件。

file_object = open('thefile.txt')
try:
     all_the_text = file_object.read( )
finally:
     file_object.close( )

注：不能把open语句放在try块里，因为当打开文件出现异常时，文件对象file_object无法执行close()方法。

## 2.读文件
读文本文件
```
input = open('data', 'r')
#第二个参数默认为r
input = open('data')
```

读二进制文件
```
input = open('data', 'rb')
```
读取所有内容
```
file_object = open('thefile.txt')
try:
     all_the_text = file_object.read( )
finally:
     file_object.close( )
```

读固定字节
```
file_object = open('abinfile', 'rb')
try:
    while True:
         chunk = file_object.read(100)
        if not chunk:
            break
         do_something_with(chunk)
finally:
     file_object.close( )
```

读每行
```
list_of_all_the_lines = file_object.readlines( )
```
如果文件是文本文件，还可以直接遍历文件对象获取每行：
```
for line in file_object:
     process line
```

## 3.写文件
写文本文件
```
output = open('data', 'w')
```

写二进制文件
```
output = open('data', 'wb')
```

追加写文件
```
output = open('data', 'w+')
```

写数据
```
file_object = open('thefile.txt', 'w')
file_object.write(all_the_text)
file_object.close( )
```

写入多行
```
file_object.writelines(list_of_text_strings)
```
注意，调用writelines写入多行在性能上会比使用write一次性写入要高。

## 4.文件进阶操作
### file函数
在处理日志文件的时候，常常会遇到这样的情况：日志文件巨大，不可能一次性把整个文件读入到内存中进行处理，例如需要在一台物理内存为 2GB 的机器上处理一个 2GB 的日志文件，我们可能希望每次只处理其中 200MB 的内容。
在 Python 中，内置的 File 对象直接提供了一个 readlines(sizehint) 函数来完成这样的事情。以下面的代码为例：
```
file = open('test.log', 'r')sizehint = 209715200   # 200Mposition = 0lines = file.readlines(sizehint)while not file.tell() - position < 0:       position = file.tell()       lines = file.readlines(sizehint)
```
每次调用 readlines(sizehint) 函数，会返回大约 200MB 的数据，而且所返回的必然都是完整的行数据，大多数情况下，返回的数据的字节数会稍微比 sizehint 指定的值大一点（除最后一次调用 readlines(sizehint) 函数的时候）。通常情况下，Python 会自动将用户指定的 sizehint 的值调整成内部缓存大小的整数倍。

file在python是一个特殊的类型，它用于在python程序中对外部的文件进行操作。在python中一切都是对象，file也不例外，file有file的方法和属性。下面先来看如何创建一个file对象：
```
file(name[, mode[, buffering]])
```
file()函数用于创建一个file对象，它有一个别名叫open()，可能更形象一些，它们是内置函数。来看看它的参数。它参数都是以字符串的形式传递的。name是文件的名字。
mode是打开的模式，可选的值为r w a U，分别代表读（默认） 写 添加支持各种换行符的模式。用w或a模式打开文件的话，如果文件不存在，那么就自动创建。此外，用w模式打开一个已经存在的文件时，原有文件的内容会被清空，因为一开始文件的操作的标记是在文件的开头的，这时候进行写操作，无疑会把原有的内容给抹掉。由于历史的原因，换行符在不同的系统中有不同模式，比如在 unix中是一个\n，而在windows中是‘\r\n’，用U模式打开文件，就是支持所有的换行模式，也就说‘\r’ '\n' '\r\n'都可表示换行，会有一个tuple用来存贮这个文件中用到过的换行符。不过，虽说换行有多种模式，读到python中统一用\n代替。在模式字符的后面，还可以加上+ b t这两种标识，分别表示可以对文件同时进行读写操作和用二进制模式、文本模式（默认）打开文件。
buffering如果为0表示不进行缓冲;如果为1表示进行“行缓冲“;如果是一个大于1的数表示缓冲区的大小，应该是以字节为单位的。

file对象有自己的属性和方法。先来看看file的属性。
```
closed #标记文件是否已经关闭，由close()改写 
encoding #文件编码 
mode #打开模式 
name #文件名 
newlines #文件中用到的换行模式，是一个tuple 
softspace #boolean型，一般为0，据说用于print
```
### file的读写方法：
```
F.read([size]) #size为读取的长度，以byte为单位 
F.readline([size]) 
#读一行，如果定义了size，有可能返回的只是一行的一部分 
F.readlines([size]) 
#把文件每一行作为一个list的一个成员，并返回这个list。其实它的内部是通过循环调用readline()来实现的。如果提供size参数，size是表示读取内容的总长，也就是说可能只读到文件的一部分。 
F.write(str) 
#把str写到文件中，write()并不会在str后加上一个换行符 
F.writelines(seq) 
#把seq的内容全部写到文件中。这个函数也只是忠实地写入，不会在每行后面加上任何东西。
```
### file的其他方法：
```
F.close() 
#关闭文件。python会在一个文件不用后自动关闭文件，不过这一功能没有保证，最好还是养成自己关闭的习惯。如果一个文件在关闭后还对其进行操作会产生ValueError 
F.flush() 
#把缓冲区的内容写入硬盘 
F.fileno() 
#返回一个长整型的”文件标签“ 
F.isatty() 
#文件是否是一个终端设备文件（unix系统中的） 
F.tell() 
#返回文件操作标记的当前位置，以文件的开头为原点 
F.next() 
#返回下一行，并将文件操作标记位移到下一行。把一个file用于for ... in file这样的语句时，就是调用next()函数来实现遍历的。 
F.seek(offset[,whence]) 
#将文件打操作标记移到offset的位置。这个offset一般是相对于文件的开头来计算的，一般为正数。但如果提供了whence参数就不一定了，whence可以为0表示从头开始计算，1表示以当前位置为原点计算。2表示以文件末尾为原点进行计算。需要注意，如果文件以a或a+的模式打开，每次进行写操作时，文件操作标记会自动返回到文件末尾。 
F.truncate([size]) 
#把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置。如果size比文件的大小还要大，依据系统的不同可能是不改变文件，也可能是用0把文件补到相应的大小，也可能是以一些随机的内容加上去。
```

# shell脚本笔记

## 变量

### 变量规则

#### 1, 赋值:
`myname=CXY`
中间不可有空格

变量内容有空格或单双引号:
```
myname="cao xin yu"
myname='cao xin yu'
myname="cxy'name"
myname='name:"cxy"'
```

变量中有变量:
```
myfname=cao
myname="$myfname xinyu"
myname=${myfname}xinyu
myname="$myfname"xinyu
```

#### 2, 取消变量设定:
`unset 变量名称`
例如
`unset myname`

#### 3, 变量中的转义符:\
```
myname=cao\ xin\ yu\'name
echo $myname
cao xin yu'name
```
#### 4, 调用其他指令``
```
	kernel_version=`uname -r`
	kernel_version=$(uname -r)
```

### 变量查看方法
查看环境变量的方法: `env`
查看所有所有变量(包括环境变量和自定义变量):`set`

### 通过用户输入初始化变量

```
read myname
让用户输入内容,将这一内容放入myname变量中
选项-p 可以添加提示内容.
选项-t 可以添加计时(超时后此指定被废弃):

read -p "Please input your name" myname -t 30 myname
```

### 变量类型的声明

```

declare [-aixr] variable 
	选项不参数： 
	-a  ：将后面名为 variable的变量量定义成为数组 (array) 类型 
	-i  ：将后面名为 variable的变量定义成为整数数字 (integer) 类型 
	-x  ：用法与export 一样，就是将后面的 variable 变成环境变量； 
	-r  ：将变量设定成为 readonly 类型，该变量不可被更改内容，也不能 unset
	

变量的默认类型为字符串

```

### 数组变量

```
定义方法1:
	var[1]=array1
	var[2]=array2
	
	echo ${var[1]}, ${var[2]}
定义方法2:
	var={array1 array2}

```

## 特殊变量

```
$n    n取值为非负整数, 意义和argv[n]相同, 既进程启动参数|
$?	    前一命令执行后的退出状态, 通常0为成功, 非零为失败
$$	    当前shell的进程号
$!	    前一个后台命令的进程号
```

## 基础输入输出
```
基础输入输出:(read, echo)

#!/bin/bash
read -p "Please input your name :" yourname
echo -e "\nOn!, you are $yourname !"

```

## 日期的使用(date)

```
#!/bin/bash
#the script will create three empty files, which named by user's input and date command

read -p "Please input file name: " fileuser
filename=${fileuser:-"filename"}
date1=$(date --date='2 days ago' +%Y%m%d)
date2=$(date --date='1 days ago' +%Y%m%d)
date3=$(date +%Y%m%d)
file1=${filename}${date1}
file2=${filename}${date2}
file3=${filename}${date3}

touch "$file1"
touch "$file2"
touch "$file3"


```

## 数值计算

```
数值计算var=$((运算内容))

#/bin/bash

read -p "Please input first number: " firstnum
read -p "Please input second number: " secondnum
result=$(($firstnum+$secondnum))
echo "$firstnum + $secondnum = $result"
result=$(($firstnum-$secondnum))
echo "$firstnum - $secondnum = $result"
result=$(($firstnum*$secondnum))
echo "$firstnum * $secondnum = $result"
result=$(($firstnum/$secondnum))
echo "$firstnum / $secondnum = $result"
result=$(($firstnum%$secondnum))
echo "$firstnum % $secondnum = $result"
```

## 条件控制
### if条件控制:
基本语法:

```
if condition1
then
	doSomething
elif condition2
then
	doSomething
else
	doSomething
fi
```

简单实例:
```
[写法1]
if cat test.txt ; then
	echo "cat success"
else
	echo "cat failed"
fi
[写法2]
if cat test.txt
then
	echo "cat success"
else
	echo "cat failed"
fi

#当cat test.text执行成功时, 打印cat success
#否则打印cat failed
```
注意:
在使用写法1时, 注意要写分号
if语句通常和test一起使用

## test的使用
```
具体参见<Shell编程24学时教程>
test使用分为三类:
1, 文件测试
2, 字符串测试
3, 数字测试

测试字符串相等:
test string1 = string2
或 [ string1 = string2 ]
注意[后和]前都有空格, =两侧也有空格

简单例子:
TEST_VER="root"

if [ "$TEST_VER" = "root" ]; then
    echo "string same"
else
    echo "string different"
fi

if test "$TEST_VER" = "123root" ; then
    echo "string same"
else
    echo "string different"
fi

```




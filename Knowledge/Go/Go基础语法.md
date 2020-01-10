# Go基础语法

## Go的纪律
Go严格区分大小写
Go一行不能写两条语句
Go中import的包没有使用, 不能编译通过. 声明但不使用的变量也不能编译通过
Go中package语句和import的语句之间不能有全局变量定义

## 变量
变量只能以下划线和字母开头, 只能由字母, 数字, 下划线构成(和C一样)

go语言中的变量必须先声明再使用
go语言中局部变量声明后必须使用, 否则编译不过去
全局变量可以声明后不使用

### 常规声明
``` go
var 变量名 类型
var name string
var age int
```
### 声明变量的同时赋值
``` go
var s1 string = "name"
```
### 变量类型推导
不指定类型, 由编译器自行推到变量的类型来完成初始化
``` go
var s = "name"
var age = 18
```
### 简短变量声明
只能在函数内部使用, 不能在全局使用
``` go
s := "varvarvar" //相当于var s = "varvarvar"
```
### 匿名变量
匿名变量用一个下划线_表示, 表明不关心此变量
匿名变量不会占用命名空间, 不会分配内存
``` go
func foo() (int, string) {
	return 10, "name"
}

func testAnonymousVar() {
	var x int
	x, _ = foo()
	fmt.Println(x)
}
```
### 批量声明
``` go
var (
    name string
    age int
    isOk bool
)
```

## 常量
在运行期间不会改变的量
常量定义之后不能修改
### 基本用法
``` go
const pi = 3.14159265
```
### 批量声明
``` go
const (
    statusOK = 200
    notFound = 404
)

const (
    n1 = 100
    n2 //没有指明值, 则和上一行一致, 即为100
    n3 //同上
)
```

### 常量计数器iota
iota是go语言中的常量计数器, 只能在常量表达式中使用
iota在const关键字出现时将被重置为0, const中每新增**一行**,iota将计数一次
可以定义类似枚举的东西
``` go
const (
    a = iota // 0, 会自动增加, 类似枚举
    b // 1
    c // 2
    d // 3
)

//插队情况
const (
    a1 = iota //0
    a2 = 100    //100
    a3 = iota //2    由于const出现时,iota才被重置为0, 故这里不会被重置
    a4 //3
)

//多变量声明在一行的情况
//const中每新增一行,iota将计数一次
const (
    b1, b2 = iota + 1, iota + 2    //b1 = 1, b2 = 2
    b3, b4 = iota + 1, iota + 2    //b3 = 2, b4 = 3
)

//定义数量级
const (
    _ = iota
    KB = 1 << (10 * iota)
    MB = 1 << (10 * iota)
    GB = 1 << (10 * iota)
)
```

## 数据类型
### bool
bool类型只有true和false两个值.
默认为false
不允许将整型强制转换为布尔类型
布尔类型不能参与数值运算, 也无法与其他类型进行转换

### int8 int16 int32 int64
### uint8 uint16 uint32 uint64
### int uint
在32位操作系统上是int32/uint32, 64位操作系统上是int64/uint64

### float32 float64
float32的最大值被定义在`math.MaxFloat32`中
```
f := 1.23456 //f的类型会默认为float64
f32 := float32(1.23456)    //float32类型的
```

### complex64 complex128
``` Go
var x complex64 = 6 + 2i
```

### uintptr
无符号整型, 用于存放一个指针

### string
go语言的字符串的内部实现使用UTF-8编码, 只能用双引号来表示
``` go
s1 := "hello"
```
单引号表示的是字符
``` go
c1 := 'h'
c2 := '好'
```
一个字符'A'占一个字节
一个utf8编码的汉字'好'一般占3个字节
``` go
c1 := '好'
c2 := 'h'
fmt.Printf("%T\n", c1) //结果为int32
fmt.Printf("%T\n", c2) //结果为int32
```

#### 转义字符
```
\r 回车(返回行首)
\n 换行
\t 制表符
\' 单引号
\" 双引号
\\ 反斜杠
```

#### 多行的字符串
用点表示多行字符串, 注意不是单引号
``` go
s1 := `
		明月几时有
		把酒问青天
		不知天上宫阙
		今夕是何年	
	`
fmt.Println(s1)
```

#### 字符串常用操作
``` go
len(str) //求长度
+ 或 fmt.Sprintf    //拼接字符串
strings.Split //分割
strings.contains //判断是否包含
strings.HasPrefix //前缀判断
strings.HasSuffix //后缀判断
strings.Index()  或 strings.LastIndex() //子串出现的位置
strings.Join(a[]string, sep string) //join操作
```
例子
``` go

//字符串长度
s2 := "hello世界"
fmt.Printf("%s len %d\n", s2, len(s2))

for _, c := range s2 {
	fmt.Printf("%c \n", c)
} 
//输出结果:
//hello世界 len 11
//h
//e
//l
//l
//o
//世
//界


//字符串拼接
s3 := " world"
fmt.Printf(s2 + s3 + "\n")
s4 := fmt.Sprintf("%s%s\n", s2, s3)
fmt.Println(s4)

//分割字符串
s5 := "D:\\Develop\\go\\bin"
ret := strings.Split(s5, "\\")
fmt.Println(ret) //[D: Develop go bin]

//包含判定
fmt.Println(strings.Contains(s5, "D")) //true

//前缀后缀判定
fmt.Println(strings.HasPrefix(s5, "D:"))  //true
fmt.Println(strings.HasSuffix(s5, "bin")) //true

s6 := "abcdefg"
fmt.Println(strings.Index(s6, "bc"))     //1
fmt.Println(strings.LastIndex(s6, "de")) //3

//拼接
fmt.Println(strings.Join(ret, "\\")) //D:\Develop\go\bin

```

#### 字符串的修改
字符串不能直接修改, 如下代码会报错
``` go
//错误!!!
str := "白萝卜"
str[0] = '红'
```
如果需要修改, 要先强制转换为rune切片
``` go
str := "白萝卜"
//str[0] = '红'
temp := []rune(str)
temp[0] = '红'
fmt.Println(string(temp))
```

### rune和byte
go中字符有两种类型, uint8或者byte类型, 代表ASCII码中的一个字符
rune类型代表一个UTF-8字符, rune实际是一个int32

### array slice
array是静态数据, 定义之后大小不可变
``` Go
var x[10]int //array
x[8] = 10
fmt.Printf("%v", x) //%v表示打印值, 数据会被打印所有元素

//或者:
x := [3]int{0, 1, 2}
```
slice是动态数组, 大小可变
``` Go
var x []int
```
slice可以用一个已经定义好的array生成
``` Go
x := [5]int{0, 1, 2, 3, 4}
y := x[1:3]    //前闭后开区间, y的值为1, 2
```


### map

## 进制
``` go
func testHexOct() {
	var a int = 10
	fmt.Printf("%d\n", a)
	fmt.Printf("%b\n", a) //二进制打印
	var b int = 077       //八进制
	fmt.Printf("%o\n", b) //八进制打印
	var c int = 0xff      //十六进制
	fmt.Printf("%x\n", c) //十六进制打印
}
```

## fmt Print
```
%d 十进制
%b 二进制
%o 八进制
%x 十六进制
%T 打印类型 例如 fmt.Printf("%T\n", a) 可能打印出int
%f 打印浮点数
%s 打印字符串
%v 打印值, 万能 
fmt.Printf("字符串: %s\n", s)  //输出为  字符串: Hello 世界
fmt.Printf("字符串: %#V\n", s) //输出为  字符串: "Hello 世界"
```

## 流程控制
### if

### for
### switch
### goto

## 关键字
### package 
go 通过package来组织

``` Go
package main
```

### var
定义一个int类型的变量, 名为x
``` Go
var x int
x = 1
```

简短声明方法, Go可以自行推断类型
``` Go
y := "cxy"
```

``` Go
y, z = "C", "C++"
```
这种自行推断的方式, 不能用于函数以外. (全局变量不能这么用)

## const
``` Go
const PI = 3.14159265
const hello string = "cxy"
```

## =和:=
:=是变量声明
如果变量已经被声明, 则只会被赋值
例如:
``` go
a, b := 1, 2
b, c := 3, 4
```
a, b, c结果为1,3,4
=是一个变量赋值操作

## 变量在内存中的位置
变量放到堆中或者栈中, 不是由用var和new声明变量的方式决定的, 而是通过编译器来选择的.

## 丢弃不必要的值
使用_
例如:
``` go
_, ok = m[key]
```

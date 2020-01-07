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
``` go
const (
    a = iota // 0, 会自动增加, 类似枚举
    b // 1
    c // 2
    d // 3
)
```

## 数据类型
### bool
### rune
### byte
### int8 int16 int32 int64
### uint8 uint16 uint32 uint64
### float32 float64
### string
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
### complex64 complex128
``` Go
var x complex64 = 6 + 2i
```


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

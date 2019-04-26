# Go基础语法

## Go的纪律
Go严格区分大小写
Go一行不能写两条语句
Go中import的包没有使用, 不能编译通过. 声明但不使用的变量也不能编译通过
Go中package语句和import的语句之间不能有全局变量定义

## 数据类型
### bool
### rune
### byte
### int8 int16 int32 int64
### uint8 uint16 uint32 uint64
### float32 float64
### string
### array slice
``` Go
var x[10] int //array
x[8] = 10
fmt.Printf("%v", x) //%v表示打印值, 数据会被打印所有元素


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

## #const
``` Go
const PI = 3.14159265
const hello string = "cxy"
```



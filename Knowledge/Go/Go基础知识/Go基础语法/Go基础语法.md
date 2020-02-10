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
``` go
func testMap() {
	var m1 map[string]int //定义了一个key为string类型, value为int类型的map
	//m1["曹操"] = 1          //崩溃, 因为map尚未初始化, 是nil
	m1 = make(map[string]int, 10) //10为估计的容量, 可以自动扩容, 但尽量提前估算好容量
	m1["曹操"] = 1
	m1["刘备"] = 2
	fmt.Println(m1) //map[刘备:2 曹操:1]
	value, ok := m1["孙权"]
	if !ok {
		fmt.Println("孙权不在map中")
	} else {
		fmt.Println(value)
	}

	//遍历
	for k, v := range m1 {
		fmt.Println(k, v)
	}
	//曹操 1
	//刘备 2

	//删除
	delete(m1, "刘备") //map[曹操:1]
	fmt.Println(m1)

	//删除不存在的key
	delete(m1, "孙权") //不做任何操作
}
```

### 自定义类型
两种方式:
1: `type myInt int`在main包中定义的新类型
2: `type yourInt int`, 只会在代码中出现, 编译完成后不会有此类型
测试代码如下
```go
type myInt int
type yourInt = int

func testType() {
	var n myInt
	n = 100
	fmt.Printf("%T\n", n) //main.myInt

	var m yourInt
	m = 200
	fmt.Printf("%T\n", m) //int
}
```
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
``` go
func testIf() {
	age := 8
	if age > 18 {
		fmt.Println("men")
	} else if age > 5 {
		fmt.Println("boy")
	} else {
		fmt.Println("baby")
	}
}
```
### for
#### 基本模式
``` go
    for i := 0; i < 10; i++ {
		fmt.Print(i)
	}
```
#### 变种形式
``` go
	j := 5
	for ; j < 10; j++ {
		fmt.Print(j)
	}
```

``` go
	fmt.Println()
	var k = 5
	for k < 10 {
		fmt.Print(k)
		k++
	}
```
#### 死循环
``` go
    //死循环
	for {

		break //终止死循环
	}
```

#### for range循环
``` go
    //for range
	s := "hello"
	for i, v := range s {
		fmt.Printf("%d, %c\n", i, v)
	}
```

#### 控制for循环
##### break
使用后跳出for循环, 和C相同
##### continue
使用后继续下一次循环, 和C相同

### switch
#### 常规switch
``` go
var i = 3
switch i {
case 1:
	fmt.Println("a")
case 2:
	fmt.Println("b")
case 3:
	fmt.Println("c")
default:
	fmt.Println("z")
}
```
#### case多个值
``` go
var n = 2
switch n {
case 1, 3, 5, 7, 9:
	fmt.Println("奇数")
case 2, 4, 6, 8:
	fmt.Println("偶数")
}
```

#### fallthrough
不推荐使用, 可以执行下一个case
``` go
var m = 3
switch m {
case 3:
	fmt.Print("3")
	fallthrough
case 4:
	fmt.Print("4")
}
//输出为34
```
### goto
不推荐使用
``` go
func testGoto() {
	fmt.Println("111")
	goto end
	fmt.Println("222")
end:
	fmt.Println("end")
}
```

## 运算符
### 算数运算符
+-*/%
%为取余
和C相同

### ++ -- 不是运算符
++ -- 在go中是单独的语句
不能放在=的右边
```
a = a--
b = b++
```

### 关系运算符
``` go
==
>=
<=
!=
>
<
```

### 逻辑运算符
&& 与
|| 或
! 非

### 位运算符
``` go
& 按位与
| 按位或
^ 异或
<< 左移
>> 右移
```

### 赋值运算符
``` go
=
+=
-+
*=
/=
%=
<<=
>>=
&=
|=
^=
```

## 数组
和C的数组一样, 定义后大小不能变, 必须存放同一种类型的数据
### 定义数组
``` go
var a1 [3]bool
```

### 初始化
如果数组不初始化, 则默认元素都是零值
#### 常规初始化
``` go
var a1 [3]bool
a1 = [3]bool{true, false, true}
fmt.Println(a1)
```

#### 根据初始值自动推断数组的长度
``` go
a100 := [...]int{0, 1, 2, 3, 4, 5}
fmt.Println(a100)
```

#### 部分赋值
``` go
//前两个元素为1, 2, 后面的默认
a3 := [5]int{1, 2}
fmt.Println(a3)
//[1 2 0 0 0]

//第0个元素为4, 第3个元素为2, 其余默认
a4 := [5]int{0: 4, 3: 2}
fmt.Println(a4)
//[4 0 0 2 0]
```

### 数组的遍历
``` go
    names := [...]string{"Tom", "Jerry", "Ben"}
    //方法一
	for i := 0; i < len(names); i++ {
		fmt.Println(names[i])
	}
	//Tom
	//Jerry
	//Ben
    
    //方法二
	for i, v := range names {
		fmt.Println(i, v)
	}
	//0 Tom
	//1 Jerry
	//2 Ben
```

### 多维数组
#### 初始化多维数组
``` go
    //多维数组
	var a11 [3][2]int
	a11 = [3][2]int{
		[2]int{1, 2},
		[2]int{3, 4},
		[2]int{5, 6},
	}
	fmt.Println(a11)
	//[[1 2] [3 4] [5 6]]

```
#### 遍历多维数组
``` go
    //多维数组的遍历
	for _, v := range a11 {
		fmt.Println(v)
		for _, v2 := range v {
			fmt.Println(v2)
		}
	}
	//[1 2]
	//1
	//2
	//[3 4]
	//3
	//4
	//[5 6]
	//5
	//6
```

## 切片(slice)
### 切片的定义和创建
#### 常规创建
``` go
    var s1 []int    //定义一个存放int类型的切片
	var s2 []string //定义一个存放string类型的切片
	fmt.Println(s1, s2)
	fmt.Println(s1 == nil) //true, 没有开辟内存空间
	fmt.Println(s1 == nil) //true, 没有开辟内存空间
	//初始化
	s1 = []int{1, 2, 3}
	s2 = []string{"地球", "太阳系", "银河系", "宇宙"}
	fmt.Println(s1, s2)
	fmt.Println(s1 == nil) //false
	fmt.Println(s1 == nil) //false
```
#### 使用make创建
``` go
//make()函数创建切片
ss1 := make([]int, 5, 10)    //创建一个容量为10, 长度为5的切片
fmt.Printf("%v, %d, %d", ss1, len(ss1), cap(ss1)) //[0 0 0 0 0], 5, 10
```
### 切片的长度和容量
``` go
//长度和容量
fmt.Printf("len(s1):%d, cap(s1):%d\n", len(s1), cap(s1))
```

### 由数组得到切片
``` go
	//由数组得到切片
	a1 := [...]int{1, 2, 3, 4, 5, 6, 7}
	s3 := a1[0:4]   //获取第0到第4个元素(包含第0个, 不包含第4个元素)生成切片
	fmt.Println(s3) //[1 2 3 4]
	s4 := a1[:4]
	fmt.Println(s4) //[1 2 3 4]
	s5 := a1[3:]
	fmt.Println(s5) //[4 5 6 7]
	s6 := a1[:]
	fmt.Println(s6) //[1 2 3 4 5 6 7]
```
### 由切片得到切片
``` go
    //切片再切片
	s7 := s6[2:]
	fmt.Println(s7)
```
###  切片的底层
切片指向了一个底层数组
切片的长度就是它元素的个数
切片的容量是底层数组从切片的第一个元素到最后一个元素的数量
![](_v_images/20200116132920476_1310.png =514x)

![](_v_images/20200116133012869_798.png =554x)

``` go
//切片底层
ss2 := []int{1, 2, 3}
ss3 := ss2
fmt.Println(ss2, ss3) //[1 2 3] [1 2 3]
ss3[0] = 100
fmt.Println(ss2, ss3) //[100 2 3] [100 2 3] ss2和ss3指向同一块内存
```
### 切片的本质
切片就是一个框, 框柱了一块连续的内存
切片属于引用类型, 真正的数据都是保存在底层数组里的

### 追加元素append
``` go
//切片append
ss4 := []string{"地球", "太阳系", "银河系"}
fmt.Println(len(ss4), cap(ss4)) //3 3
ss4 = append(ss4, "宇宙")         //append追加元素, 原来的底层数组放不下的时候, go底层就会把底层数组换一个
fmt.Println(len(ss4), cap(ss4)) //4 6
ss5 := []string{"月球", "水星", "金星"}
ss4 = append(ss4, ss5...)       //...表示拆开切片, 将一个切片追加到另一个切片后面
fmt.Println(len(ss4), cap(ss4)) //7 12
```

### 复制切片copy
``` go
//切片copy
aa1 := []int{1, 3, 5}
aa2 := aa1
var aa3 = make([]int, 3, 3)
copy(aa3, aa1)             //复制, 改变aa1中的值不会再改变aa3中的值
fmt.Println(aa1, aa2, aa3) //[1 3 5] [1 3 5] [1 3 5]
aa1[0] = 100
fmt.Println(aa1, aa2, aa3) //[100 3 5] [100 3 5] [1 3 5]
```

## 指针
### 基本用法
``` 
&取地址
* 根据地址取值
```

具体用法:
``` go
n := 18
p := &n
fmt.Println(p)        //0xc000010840
fmt.Printf("%T\n", p) //*int

fmt.Println(*p) //18

//定义指针类型
var a *int
a = p
fmt.Println(*a) //18
*a = 100
fmt.Println(*a) //100
```
### new关键字
``` go
//new申请地址
c := new(int)
*c = 200
fmt.Println(*c) //200
```

取址可能崩溃, 如下例会导致崩溃
``` go
var b *int //nil
*b = 100   //报错
```

### make关键字
make和new一样, 也是用于分配内存, 但只用于切片(slice), map和chan的内存的创建, 而且它返回的类型就是这三个类型本身, 而不是他们的指针.
因为这三种类型本身就是引用类型

## map
map是一个无序的基于key-value的数据结构, map在Go语言中是引用类型
### 定义和取值
``` go
var m1 map[string]int //定义了一个key为string类型, value为int类型的map
//m1["曹操"] = 1          //崩溃, 因为map尚未初始化, 是nil
m1 = make(map[string]int, 10) //10为估计的容量, 可以自动扩容, 但尽量提前估算好容量
m1["曹操"] = 1
m1["刘备"] = 2
fmt.Println(m1) //map[刘备:2 曹操:1]
value, ok := m1["孙权"]
if !ok {
	fmt.Println("孙权不在map中")
} else {
	fmt.Println(value)
}
```

### 遍历
``` go
    //遍历
	for k, v := range m1 {
		fmt.Println(k, v)
	}
	//曹操 1
	//刘备 2
```

### 删除
``` go
//删除
delete(m1, "刘备") //map[曹操:1]
fmt.Println(m1)

//删除不存在的key
delete(m1, "孙权") //不做任何操作
```

## 函数
### 基本用法
``` go
//函数
//函数的定义
func sum(a int, b int) (ret int) {
	return a + b
}

//没有返回值的函数
func f1(a int, b int) {
	fmt.Println(a, b)
}

//没有参数但有返回值
func f2() int {
	return 3
}

//参数可以命名, 也可以不命名
//下面的函数返回值提前命名为了ret, 可以直接return
func sum2(x int, y int) (ret int) {
	ret = x + y
	return
}

//多个返回值
func f3() (int, int) {
	return 1, 2
}

//参数类型可以简写
func f4(x, y int) int {
	return x + y
}

//可变长参数
//可变长参数必须放在最后
func f5(x int, y ...int) {
	fmt.Println(x)
	fmt.Println(y)
}

func testFunc() {
	fmt.Println(sum(1, 2))
	f1(1, 2)
	fmt.Println(sum2(2, 3)) //5
	f3()
	f5(1, 2, 3, 4, 5)
	//1
	//[2 3 4 5]
}
```
go语言中没有默认参数这个概念

### defer
#### defer的基本概念
defer将它后面的语句延迟到函数即将返回的时候再执行
``` go
func testDefer() {
	fmt.Println("begin")
	defer fmt.Println("defer content")
	fmt.Println("end")
}

//打印顺序为:
//begin
//end
//defer content
```
#### 多个defer
如果一个函数中有多个defer, 则最后defer的内容最先执行
``` go
func testMultiDefer() {
	fmt.Println("begin")
	defer fmt.Println("1111")
	defer fmt.Println("2222")
	defer fmt.Println("3333")
	fmt.Println("end")
}

//begin
//end
//3333
//2222
//1111
```

#### defer的底层实现
在go语言中, return并不是一个操作, 它分为两步:
1, 返回值 = x
2, 调用RET指令
而defer语句的执行时机就在两步之间

### 函数类型
可以定义函数类型
``` go
func testFuncType() {
	pFunc := sum
	fmt.Printf("%T\n", pFunc) //func(int, int) int
}
```

函数的参数可以是函数类型
``` go
//函数的参数可以是函数类型
func func11(x func(int, int) int) {
	fmt.Println(x(1, 2))
}

func testFuncType2() {
	func11(func1)
	//3
}
```

函数的返回值可以是函数类型
``` go
func testFuncType3() func(int, int) int {
	ret := func(a int, b int) int {
		return a + b
	}
	return ret
}
```

### 匿名函数
``` go
func testNoNameFunc() {
	f1 := func(x, y int) {
		fmt.Println(x + y)
	}
	f1(1, 2) //3

	//如果定义函数后立即执行, 可以简写为立即执行函数
	func(a, b int) {
		fmt.Println(a + b)
	}(1, 2) //3
}
```

## 闭包Closure
### 闭包是什么
闭包是一个函数, 这个函数包含了外部作用域的一个变量
闭包 = 函数 + 外部变量的引用

### 例子
``` go

func makeSuffixFunc(suffix string) func(string) string {
	return func(name string) string {
		if !strings.HasSuffix(name, suffix) { //如果不以suffix为后缀, 则增加此后缀
			return name + suffix
		}
		return name
	}
}

func testClosure() {
	jpgFunc := makeSuffixFunc(".jpg")
	txtFunc := makeSuffixFunc(".txt")
	fmt.Println(jpgFunc("test")) //test.jpg
	fmt.Println(txtFunc("test")) //test.txt
}

```

## panic和recover
go1.12版本中没有异常机制, 但是使用panic/recover可以处理错误.
panic可以在任何地方引发, 但recover只有在defer调用的函数中有效
``` go
func testPanic() {
	defer func() {
		err := recover()
		fmt.Println("恢复处理", err)
	}()
	panic("出现了严重的错误!!!!!")
	fmt.Println("111")
}
```
注意:
recover必须配合defer使用
defer一定要在可能引发panic的语句之前定义

## 内置函数
close :主要用来关闭channel
len
new : 返回的是指针
make : 返回引用类型, 比如chan, map, slice
append
panic和recover

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

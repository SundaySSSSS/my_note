# Go Vs C++

## typedef 
### 用法
``` C++
typedef int int32
```

``` go
type Speed float32
type Dist float32
```
 
 ### 区别
 在go中, 被定义为不同类型的相同类型变量不能相互比较
 如上面的Speed和Dist是不能相互比较的, 但是可以强制类型转换
## printf
go中使用fmt.Printf
go中追加%b打印二进制
go中在%后使用[1]表示再次使用第一个操作数
go中%后的#表示%o, %x, %X输出时添加0x, 0或0X的前缀
``` go
o := 0666
fmt.Printf("%d %[1]o %#[1]o\n", o)
```
结果为:
```
438 666 0666
```
%q打印带单引号的字符
```go
ascii := a
fmt.Print("%d %[1]c %[1]q\n", ascii)     //97 a 'a'
```

go追加%g来打印浮点数
go追加%e来使用科学计数法进行打印
go也支持%f

go中%t打印布尔类型
go中%T打印类型

## 枚举
``` C++
enum {
    Sunday
    Monday
    Tuesday
    Wednesday
    Thursday
    Friday
    Saturday
};
```

``` go
const (
    a = 1
    b
    c = 2
    d
)
fmt.Println(a, b, c, d) // "1 1 2 2"
```

### 区别
go自动继承上面的量的值, 不自然递增

### go特性: iota
``` go
type Weekday int
const (
    Sunday Weekday = iota
    Monday
    Tuesday
    Wednesday
    Thursday
    Friday
    Saturday
)
```
则Sunday是0, 后面依次为1, 2, 3...

也可以使用一个包含iota的表达式, 如
``` go
type Flags uint
const (
    FlagUp Flags = 1 << iota // is up
    FlagBroadcast // supports broadcast access capability
    FlagLoopback // is a loopback interface
    FlagPointToPoint // belongs to a point-to-point link
    FlagMulticast // supports multicast access capability
)
```
则依次按照1左移0位, 1位...填充枚举的值

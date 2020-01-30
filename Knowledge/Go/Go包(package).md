# Go包(package)

只有main包才能编译成为一个可执行文件

## 导入包
### 导入单个包
``` go
import "fmt"
```
一个文件夹下只能有一个包, 同样一个包的文件不能在多个文件夹下
包名可以和文件夹名不一致, 包名不能包含-符号
包名和文件夹名不一致时, 可以声明包名, 例如"路径/002calc"一个名为calc的包可以如下引入:
``` go
import calc "路径/002calc"
```

### 导入多个包
导入多个包
``` go
import (
    "fmt"
    "pkg1"
)
```

### 匿名导入包
如果只希望导入包, 而不使用包内部的数据时, 可以使用匿名导入包
``` go
import _ "包的路径"
```
匿名导入包与其他导入的包一样都会被编译到可以执行文件中

## 包的公有和私有
包中的标志符如果首字母小写, 则表示私有, 只能在这个包中使用
如果首字母大写, 其他包也可以使用

## init函数
### init函数的调用时机
每个包中都可以写一个init函数, 在包被导入时执行, 不能主动调用init函数
``` go
func init() {
    //do something
}
```
执行顺序:
全局声明->init()->main()
在init之前, 全局声明的变量已经被赋值

基本测试代码
``` go
package main

import "fmt"

func init() {
	fmt.Println("init")
}

func main() {
	fmt.Println("main")
}
```
打印结果为:
```
init
main
```

### 多个包连锁导入的情况
如果main包导入A, A导入B, B导入C
则init的执行顺序为C.init, B.init, A.init, main.init
如图
![](_v_images/20200123121103206_29856.png =502x)
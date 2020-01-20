# Go接口(interface)
## 基本概念
接口是一种类型
内部定义了方法
只要实现了接口内部方法的变量都是接口类型(多态)

## 基本使用方法
``` go
package main

import (
	"fmt"
)

//定义一个接口
type notifier interface {
	notify()
}

type user struct {
	name string
	email string
}

func (u *user) notify() {
	fmt.Printf("Send user e-mail to %s<%s>\n", u.name, u.email)
}

func main() {
	u := user{"cxy", "sxinyus@126.com"}
	sendNotification(&u)
}

func sendNotification(n notifier) {
	n.notify()
}

```

## 通过接口实现多态
``` go
package main

import (
	"fmt"
)

//定义一个接口
type notifier interface {
	notify()
}

//普通用户
type user struct {
	name string
	email string
}

//管理员
type admin struct {
	name string
	email string
}

//普通用户和管理员都实现notify接口
func (u *user) notify() {
	fmt.Printf("Send user e-mail to %s<%s>\n", u.name, u.email)
}

func (a *admin) notify() {
	fmt.Printf("Sending admin e-mail to %s<%s>\n", a.name, a.email)
}

func main() {
	u := user{"cxy", "sxinyus@126.com"}
	sendNotification(&u)
	a := admin{"zlp", "zlp@163.com"}
	sendNotification(&a)
}

func sendNotification(n notifier) {
	n.notify()
}

```

## 空接口
没有必要起名字, 通常定义为如下形式
``` go
interface {}
```
空接口通常有如下应用
### 空接口作为函数的参数
空接口可以实现接收任意类型的函数参数
``` go
func show(a interface{}) {
	fmt.Printf("type: %T value:%v\n", a, a)
}

//空接口
func main() {
	show(false) //type: bool value:false
	show(nil)   //type: <nil> value:<nil>
	show("abc") //type: string value:abc
}
```
### 空接口作为map的值
使用空接口可以实现保存任意值的字典
``` go
//空接口
func main() {
	var m1 map[string]interface{}
	m1 = make(map[string]interface{}, 16)
	m1["name"] = "曹操"
	m1["age"] = 50
	fmt.Println(m1) //map[age:50 name:曹操]
}
```

## 判断空接口的类型的方法-类型断言
### 指定类型断言
基本形式如下, 可以判定当前的空接口是哪种类型
`接口变量名.(类型名)`
具体例子如下
``` go
func assertInterface(a interface{}) {
	str, ok := a.(string)
	if !ok {
		fmt.Println("不是字符串")
	} else {
		fmt.Println("是字符串", str)
	}
}

func main() {
	name := "曹操"
	assertInterface(name)
}

```

### 返回类型后再判定
基本形式如下, 可以返回类型
`接口变量名.(type)`

``` go
func assertAllInterfaceType(a interface{}) {
	switch t := a.(type) {
	case string:
		fmt.Println("这是一个字符串", t)
	case int:
		fmt.Println("这是一个int", t)
	default:
		fmt.Println("不知道是什么鬼类型")
	}
}

//空接口
func main() {
	name := "曹操"
	assertAllInterfaceType(name) //这是一个字符串 曹操
}
```

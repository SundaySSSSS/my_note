# Go多态
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
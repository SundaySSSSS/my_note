# Go接口(interface)
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


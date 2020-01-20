# Go结构体
## 结构体定义
``` go
package main

import "fmt"

type person struct {
	name  string
	age   int
	hobby []string
}

func main() {
	var p person
	p.name = "曹操"
	p.age = 50
	p.hobby = []string{"梦中杀人", "xxx"}
	fmt.Println(p)
}

```

## 匿名结构体
通常用于临时的场景, 用过之后不再使用
``` go
//匿名结构体
var s struct {
	x int
	y int
	z int
}
s.x = 1
s.y = 2
s.z = 3
fmt.Println(s)
```

## 结构体的初始化
``` go
    //方法1  : 通过key-value初始化
	var p1 = person{
		name:   "曹操",
		gender: "男",
	}
	fmt.Println(p1)
	//方法2   : 通过值列表的方式初始化
	var p2 = person{
		"孙权",
		"男",
	}
	fmt.Println(p2)
```
## 备注
结构体是通过值传递的(go函数都是通过值传递的, 同C)
``` go
type person struct {
	name, gender string
}

func f(x person) {
	x.gender = "女" //修改的是副本
}

func main() {
	var p person
	p.name = "曹操"
	p.gender = "男"
	f(p)
	fmt.Println(p) //{曹操 男}
}
```
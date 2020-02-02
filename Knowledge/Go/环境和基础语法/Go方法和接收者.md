# Go方法和接收者
## 方法 + 值接收者
方法是作用于特定类型的函数, 类似于C++的成员函数
例如:
``` go
type person struct {
	name  string
	age   int
	hobby []string
}

//person的方法, 接收者表示的是调用该方法的具体类型的变量
//多用类型名首字母小写表示, 不推荐this和self
func (p person) eat() {
	fmt.Println(p.name, "说: ", "食之无味弃之可惜")
}

func main() {
	var p person
	p.name = "曹操"
	p.age = 50
	p.hobby = []string{"梦中杀人", "xxx"}
	fmt.Println(p)

	p.eat() //曹操 说:  食之无味弃之可惜
}
```
## 指针接收者
注意, 
`func (p person) eat() {...`
中, p是值传递, 修改p中的值不会影响到原来的p
如果要修改p, 使用指针接收者的形式:
``` go
func (p *person) eat() {
    ...
}
```

具体的例子:
``` go
package main

import "fmt"

type person struct {
	name   string
	age    int
	hobby  []string
	hungry bool
}

func (p person) eat() {
	fmt.Println(p.name, "说: ", "食之无味弃之可惜")
	p.hungry = false //不会改变原来的hungry, 是值传递
}

func (p *person) eatGood() {
	fmt.Println(p.name, "说", "好吃")
	p.hungry = false //会起作用
}

func main() {
	var p person
	p.name = "曹操"
	p.age = 50
	p.hobby = []string{"梦中杀人", "xxx"}
	p.hungry = true //饿了
	fmt.Println(p)

	p.eat()               //曹操 说:  食之无味弃之可惜
	fmt.Println(p.hungry) //true
	p.eatGood()
	fmt.Println(p.hungry) //false
}
```

## 给任何类型添加方法
``` go

type myInt int

func (m myInt) hello() {
	fmt.Println("我是一个int!!!!")
}

func main() {
	m := myInt(100)
	m.hello()
}
```
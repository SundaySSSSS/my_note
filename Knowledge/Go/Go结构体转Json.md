# Go结构体转Json
## 结构体 -> Json
可以通过json包中的Marshal方法
例如:
``` go
package main

import (
	"encoding/json"
	"fmt"
)

type person struct {
	Name string //注意 : 必须大写, 否则json包无法访问到此节点
	Age  int    //同上
}

func main() {
	p1 := person{
		Name: "曹操",
		Age:  50,
	}
	b, err := json.Marshal(p1)
	if err != nil {
		fmt.Printf("marshal failed, err: %v\n", err)
		return
	}
	fmt.Println(string(b)) //{"Name":"曹操","Age":50}
}
```

如果想结构体转出来的json节点不是大写字母开头, 可以在结构体成员后面追加
``` go
type person struct {
	Name string `json:"name" db:"name" ini:"name"` //在json中解释为name, 数据库(db)中解释为name, ini文件中也解释为name
	Age  int
}

func main() {
	p1 := person{
		Name: "曹操",
		Age:  50,
	}
	b, err := json.Marshal(p1)
	if err != nil {
		fmt.Printf("marshal failed, err: %v\n", err)
		return
	}
	fmt.Println(string(b)) //{"name":"曹操","Age":50}
}
```

## Json -> 结构体
``` go
    //反序列化
	str := `{"name":"孙权", "age":18}`
	var p2 person
	json.Unmarshal([]byte(str), &p2)
	fmt.Printf("%#v\n", p2) //main.person{Name:"孙权", Age:18}
```
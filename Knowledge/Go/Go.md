# Go
## 安装
在网站下载
`https://studygolang.com/`
直接安装即可, mac下默认安装在`/usr/local/go`

如果下载的是压缩包, 则解压后,bin目录下的go就是执行脚本的东西

## Hello World
``` go
package main //打一个包
import "fmt" //引入一个包

func main() {
	fmt.Println("hello, world")
}
```

## 编译
如果go文件为hello.go
则在命令行可以直接`go build hello.go`
windows下会出现exe, linux,mac下会出现可执行的hello文件.

也可以使用`go run hello.go`来执行, 使用类似脚本的形式.不推荐.

## 注意事项
Go严格区分大小写
Go一行不能写两条语句
Go中import的包没有使用, 不能编译通过. 声明但不使用的变量也不能编译通过

## 转义字符(escape char)
\t \n \
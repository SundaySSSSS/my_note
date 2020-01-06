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

## GOPATH
GOPATH是一个需要手动配置的环境变量, 用于存放外接导入的包
可以通过命令`go env`进行查看
要设置gopath， 在linux中， 
```
export GOPATH='~/Develop/gopath'
```
在windows下， 设置一个名为GOPATH的环境变量, 变量值为路径即可(go会自动创建一个GOPATH环境变量, 修改它的值即可)

推荐在gopath中新建三个目录:
bin - 存放编译后的二进制文件
pkg
src - 源码
推荐把gopath下的bin目录加入环境变量PATH下(windows下)

设置完成后, 可以在命令行输入`go env`
出现如下类似内容, 其中GOPATH已经被设置好, GOROOT为go的安装目录
```
C:\Users\root>go env
set GO111MODULE=
set GOARCH=amd64
set GOBIN=
set GOCACHE=C:\Users\root\AppData\Local\go-build
set GOENV=C:\Users\root\AppData\Roaming\go\env
set GOEXE=.exe
set GOFLAGS=
set GOHOSTARCH=amd64
set GOHOSTOS=windows
set GONOPROXY=
set GONOSUMDB=
set GOOS=windows
set GOPATH=E:\Develop\go
set GOPRIVATE=
set GOPROXY=https://proxy.golang.org,direct
set GOROOT=E:\Go
set GOSUMDB=sum.golang.org
set GOTMPDIR=
set GOTOOLDIR=E:\Go\pkg\tool\windows_amd64
set GCCGO=gccgo
set AR=ar
set CC=gcc
set CXX=g++
set CGO_ENABLED=1
set GOMOD=
set CGO_CFLAGS=-g -O2
set CGO_CPPFLAGS=
set CGO_CXXFLAGS=-g -O2
set CGO_FFLAGS=-g -O2
set CGO_LDFLAGS=-g -O2
set PKG_CONFIG=pkg-config
set GOGCCFLAGS=-m64 -mthreads -fno-caret-diagnostics -Qunused-arguments -fmessage-length=0 -fdebug-prefix-map=C:\Users\root\AppData\Local\Temp\go-build641561570=/tmp/go-build -gno-record-gcc-switches
```

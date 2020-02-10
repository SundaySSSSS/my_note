# 单元测试
## go test工具
Go语言中的测试依赖go test命令, go test命令是一个按照一定的约定和组织的测试代码的驱动程序.
所有以_test.go为后缀的源代码文件都是go test的一部分, 不会被go build编译到最终的可执行文件中

在*_test.go文件中, 有三种类型的测试函数:
类型 |	格式 	|   作用
----|-----|----
测试函数 |	函数名前缀为Test 	| 测试程序的一些逻辑行为是否正确
基准函数 |	函数名前缀为Benchmark 	| 测试函数的性能
示例函数 |	函数名前缀为Example 	| 为文档提供示例文档


## 测试函数
### 测试函数的格式
每个测试函数必须导入testing包，测试函数的基本格式（签名）如下：
``` go
func TestName(t *testing.T){
    // ...
}
```
测试函数的名字必须以Test开头，可选的后缀名必须以大写字母开头，举几个例子：
``` go
func TestAdd(t *testing.T){ ... }
func TestSum(t *testing.T){ ... }
func TestLog(t *testing.T){ ... }
```
其中参数t用于报告测试失败和附加的日志信息。 testing.T的拥有的方法如下：
``` go
func (c *T) Error(args ...interface{})
func (c *T) Errorf(format string, args ...interface{})
func (c *T) Fail()
func (c *T) FailNow()
func (c *T) Failed() bool
func (c *T) Fatal(args ...interface{})
func (c *T) Fatalf(format string, args ...interface{})
func (c *T) Log(args ...interface{})
func (c *T) Logf(format string, args ...interface{})
func (c *T) Name() string
func (t *T) Parallel()
func (t *T) Run(name string, f func(t *T)) bool
func (c *T) Skip(args ...interface{})
func (c *T) SkipNow()
func (c *T) Skipf(format string, args ...interface{})
func (c *T) Skipped() bool
```

### 测试函数示例
例如, 要测试一个split包, 里面有一个Split函数
如下:
split/split.go
``` go
// split/split.go

package split

import "strings"

// split package with a single split function.

// Split slices s into all substrings separated by sep and
// returns a slice of the substrings between those separators.
func Split(s, sep string) (result []string) {
	i := strings.Index(s, sep)

	for i > -1 {
		result = append(result, s[:i])
		s = s[i+1:]
		i = strings.Index(s, sep)
	}
	result = append(result, s)
	return
}
```
在同目录下, 创建一个名为split_test.go的文件, 并定义一个测试函数
split/split_test.go
``` go
// split/split_test.go

package split

import (
	"reflect"
	"testing"
)

func TestSplit(t *testing.T) { // 测试函数名必须以Test开头，必须接收一个*testing.T类型参数
	got := Split("a:b:c", ":")         // 程序输出的结果
	want := []string{"a", "b", "c"}    // 期望的结果
	if !reflect.DeepEqual(want, got) { // 因为slice不能比较直接，借助反射包中的方法比较
		t.Errorf("excepted:%v, got:%v", want, got) // 测试失败输出错误提示
	}
}
```

在此文件加中执行go test命令即可进行单元测试

## 基准函数

## 示例函数

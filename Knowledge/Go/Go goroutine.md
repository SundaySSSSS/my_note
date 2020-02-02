# Go goroutine
## 概念
### 基本特征
Go语言的并发通过goroutine实现, goroutine类似于线程, 是用户态的线程
线程由操作系统调度, 而goroutine是Go语言的运行时(runtime)调度的

goroutine之间的通信可以由channel完成
main函数也对应一个goroutine, main的goroutine结束后, 整个进程会终止
goroutine在对应的函数结束后自动结束
### goroutine和线程的不同

#### 可增长的栈
操作系统线程一般都有固定的栈内存（通常为2MB）,一个goroutine的栈在其生命周期开始时只有很小的栈（典型情况下2KB），goroutine的栈不是固定的，他可以按需增大和缩小，goroutine的栈大小限制可以达到1GB，虽然极少会用到这个大。所以在Go语言中一次创建十万左右的goroutine也是可以的

#### goroutine的调度
GPM是Go语言运行时（runtime）层面的实现，是go语言自己实现的一套调度系统。区别于操作系统调度OS线程。

##### G
G是Goroutine的缩写，相当于操作系统中的进程控制块，在这里就是Goroutine的控制结构，是对Goroutine的抽象。其中包括执行的函数指令及参数；G保存的任务对象；线程上下文切换，现场保护和现场恢复需要的寄存器(SP、IP)等信息。
##### P
P(Processor)是一个抽象的概念，并不是真正的物理CPU。P管理着一组goroutine队列，P里面会存储当前goroutine运行的上下文环境（函数指针，堆栈地址及地址边界），P会对自己管理的goroutine队列做一些调度（比如把占用CPU时间较长的goroutine暂停、运行后续的goroutine等等）当自己的队列消费完了就去全局队列里取，如果全局队列里也消费完了会去其他P的队列里抢任务。
##### M
M（machine）是Go运行时（runtime）对操作系统内核线程的虚拟， M与内核线程一般是一一映射的关系， 一个groutine最终是要放到M上执行的；

P与M一般也是一一对应的。他们关系是： P管理着一组G挂载在M上运行。当一个G长久阻塞在一个M上时，runtime会新建一个M，阻塞G所在的P会把其他的G 挂载在新建的M上。当旧的G阻塞完成或者认为其已经死掉时 回收旧的M。

P的个数是通过runtime.GOMAXPROCS设定（最大256），Go1.5版本之后默认为物理线程数。 在并发量大的时候会增加一些P和M，但不会太多，切换太频繁的话得不偿失。

#### goroutine调度上的优势
单从线程调度讲，Go语言相比起其他语言的优势在于OS线程是由OS内核来调度的，goroutine则是由Go运行时（runtime）自己的调度器调度的，这个调度器使用一个称为m:n调度的技术（复用/调度m个goroutine到n个OS线程）。 其一大特点是goroutine的调度是在用户态下完成的， 不涉及内核态与用户态之间的频繁切换，包括内存的分配与释放，都是在用户态维护着一块大的内存池， 不直接调用系统的malloc函数（除非内存池需要改变），成本比调度OS线程低很多。 另一方面充分利用了多核的硬件资源，近似的把若干goroutine均分在物理线程上， 再加上本身goroutine的超轻量，以上种种保证了go调度方面的性能。

### GOMAXPROCS
Go运行时的调度器使用GOMAXPROCS参数来确定需要使用多少个OS线程来同时执行Go代码。默认值是机器上的CPU核心数。例如在一个8核心的机器上，调度器会把Go代码同时调度到8个OS线程上（GOMAXPROCS是m:n调度中的n）。

Go语言中可以通过runtime.GOMAXPROCS()函数设置当前程序并发时占用的CPU逻辑核心数。

Go1.5版本之前，默认使用的是单核心执行。Go1.5版本之后，默认使用全部的CPU逻辑核心数。
#### 获取CPU线程数

``` go
fmt.Println(runtime.NumCPU())
```
注意, 如果CPU支持超线程技术, 则`runtime.NumCPU()`返回的数值为CPU核心数乘以2
例如AMD R5 3600为6核心12线程, 则则`runtime.NumCPU()`返回的数值为12

#### 设置GOMAXPROCS
``` go
runtime.GOMAXPROCS(6)
```

## 基本的使用
goroutine
``` go
package main

import "fmt"
import "time"

func hello() {
	fmt.Println("hello")
}

func main() {
	go hello()    //使用goroutine运行函数hello
	fmt.Println("main")
	time.Sleep(time.Second) //如果不sleep, 可能导致main函数终止, 而进程终止, 从而hello函数没有执行完
}
```

也可以使用匿名函数
``` go
func main() {
	go func() {
		fmt.Println("hello")
	}()
	fmt.Println("main")
	time.Sleep(time.Second)
}
```

## 使用Wait等待goroutine结束
### 基本方法
1, 创建sync.WaitGroup对象:`var wg sync.WaitGroup`
2, 在goroutine执行前, 调用`wg.Add`方法, 增加计数
3, 在goroutine执行后, 调用`wg.Done()`方法, 减少计数
4, 在需要等待goroutine结束的地方, 调用`wg.Wait()`方法, 此方法将一直阻塞直到wg的计数减为0

### 简单例子
``` go
var wg sync.WaitGroup
func f1(i int) {
	defer wg.Done()
	fmt.Println(i)
}

func testWait() {
	for i := 0; i < 10; i++ {
		wg.Add(1)
		go f1(i)
	}
	wg.Wait()
}

func main() {
	testWait()
}

```

### 较为复杂例子
``` go
package main

import (
	"fmt"
	"runtime"
	"sync"
)

func main() {
	//分配一个逻辑处理器给调度器使用
	runtime.GOMAXPROCS(1)

	var wg sync.WaitGroup
	wg.Add(2)
	fmt.Printf("Start Goroutines")
	//声明匿名函数, 并创建一个goroutine
	go func() {
		//在函数退出时调用Done来统治main函数工作已经完成
		defer wg.Done()
		//打印三次字母表
		for count := 0; count < 3; count++ {
			for char := 'a'; char < 'a' + 26; char++ {
				fmt.Printf("%c ", char)
			}
		}
	} ()

	go func() {
		//在函数退出时调用Done来统治main函数工作已经完成
		defer wg.Done()
		//打印三次字母表
		for count := 0; count < 3; count++ {
			for char := 'A'; char < 'A' + 26; char++ {
				fmt.Printf("%c ", char)
			}
		}
	} ()

	//等待goroutine结束
	fmt.Println("Waiting To Finish")
	wg.Wait()

	fmt.Println("\nTerminaing Program")
}
```
输出结果为:
```
Start GoroutinesWaiting To Finish
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z 
Terminaing Program
```
由于第一个 goroutine 完成所有显示需要花时间太短了，以至于在调度器切换到第二个 goroutine之前，就完成了所有任务。这也是为什么会看到先输出了所有的大写字母，之后才输出小写字母。

### 能看出并发效果的代码
下面代码中, 每个goroutine在计算并显示5000以内的素数
``` go
package main

import (
	"fmt"
	"runtime"
	"sync"
)

var wg sync.WaitGroup

func main() {
	n := runtime.NumCPU()
	fmt.Printf("%d CPU\n", n)
	//分配逻辑处理器给调度器使用
	runtime.GOMAXPROCS(n)

	wg.Add(2)
	fmt.Println("Create Goroutines")
	go printPrime("A")
	go printPrime("B")
	//等待goroutine结束
	fmt.Println("Waiting To Finish")
	wg.Wait()
	fmt.Println("\nTerminaing Program")
}

func printPrime(prefix string) {
	defer wg.Done()

	next:
	for outer := 2; outer < 5000; outer++ {
		for inner := 2; inner < outer; inner++ {
			if outer % inner == 0 {
				continue next
			}
		}
		fmt.Printf("%s:%d\n", prefix, outer)
	}
	fmt.Println("Completed", prefix)
}

```

## 竞争状态
### 监测竞争状态
访问共享资源时, 会发生竞争问题
go有自己的竞争状态监测工具
使用如下命令对go进行编译
`go bulid -race`
再运行, 如果程序发生了竞争状态, 则会报错
### 避免竞争状态
#### 原子函数
##### atomic.AddInt64
``` go
import "sync/atomic"
import "sync"

var counter int64

//安全的对counter加1
atomic.AddInt64(&counter, 1)
```

##### LoadInt64 和 StoreInt64
``` go
var shutdown int64
//安全的将shutdown变量设置为1
atomic.StoreInt64(&shutdown, 1)
//安全的取出shutdown变量的值
var int64 sd_safe := atomic.LoadInt64(&shutdown)
```

#### 互斥锁
``` go
import "sync"
var mutex sync.Mutex

mutex.Lock()
//Do Something
mutex.Unlock()
```

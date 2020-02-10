# Go channel
## 基本用法
### 创建通道
``` go
//一个传递int类型的channel
var ch1 chan int
ch1 = make(chan int)
// 无缓冲的整型通道
unbuffered := make(chan int)
// 有缓冲的字符串通道
buffered := make(chan string, 10)
```

### 向通道写数据
``` go
buffered := make(chan string, 10)
buffered <- "cxy"
```
注意:
如果channel是不带缓冲的, 则写入操作会阻塞, 直到从channel中取走数据后, 才会解除阻塞
如果channel是带缓冲的, 如果当前channel的缓冲不满, 则不会阻塞, 如果channel的缓冲区满了, 则会阻塞


### 从通道中接收数据
#### 常规方法
``` go
value := <-buffered
```

循环取值
``` go
for {
	i, ok := <-ch1 // 通道关闭后再取值ok=false
	if !ok {
	    break
	}
	//Do Something
}
```

#### 通过for range从通道循环取值
``` go
for i := range ch2 { // 通道关闭后会退出for range循环
    fmt.Println(i)
}
```

### 关闭通道
``` go
unbuffered := make(chan int)
// Do Something
close(unbuffered)
```
注意: 只有在通知接收方goroutine所有的数据都发送完毕的时候才需要关闭通道。通道是可以被垃圾回收机制回收的，它和关闭文件是不一样的，在结束操作之后关闭文件是必须要做的，但关闭通道不是必须的。

关闭后的通道有以下特点：

    对一个关闭的通道再发送值就会导致panic。
    对一个关闭的通道进行接收会一直获取值直到通道为空。
    对一个关闭的并且没有值的通道执行接收操作会得到对应类型的零值。
    关闭一个已经关闭的通道会导致panic。


## 最简单例子
``` go
package main

import "fmt"
import "sync"

var wg sync.WaitGroup
var ch chan int

func main() {
	ch = make(chan int)
	wg.Add(1)
	go func() {
		defer wg.Done()
		value := <- ch
		fmt.Printf("get %d from channel\n", value)
	}()
	ch <- 10

	wg.Wait()
	fmt.Println("close")
}
```

## 无缓冲的通道
无缓冲的通道（unbuffered channel）是指在接收前没有能力保存任何值的通道。这种类型的通道要求发送 goroutine 和接收 goroutine 同时准备好，才能完成发送和接收操作。如果两个 goroutine没有同时准备好，通道会导致先执行发送或接收操作的 goroutine 阻塞等待。这种对通道进行发送和接收的交互行为本身就是同步的。其中任意一个操作都无法离开另一个操作单独存在。

本程序模拟了两个球员在打网球, 通过随机数判定失球, 球通过channel进行传递.
``` go
package main

import (
    "fmt"
	"math/rand"
	"sync"
	"time"
)

// 本程序模拟两个选手在通过channel打网球

var wg sync.WaitGroup

func init() {
	rand.Seed(time.Now().UnixNano())
}

func main() {
	court := make(chan int)	//球场是一个通道
	wg.Add(2)

	//启动两个选手
	go player("cxy", court)
	go player("zlp", court)

	court <- 1	//发球
	//等待游戏结束
	wg.Wait()
}

func player(name string, court chan int) {
	defer wg.Done()

	for {
		//等待球被打过来
		ball, ok := <-court
		if !ok {
			//如果通道被关闭了, 说明本球手赢了
			fmt.Printf("Player %s Won\n", name)
			return
		}
		//通过随机数判定是否丢球
		n := rand.Intn(100)
		if n % 13 == 0 {
			fmt.Printf("Player %s Missed\n", name)
			//关闭通道, 表示本球员输了
			close(court)
			return
		}

		//成功将球打回, 将击球数++
		fmt.Printf("Player %s Hit %d\n", name, ball)
		ball++

		//将球打给对手
		court <- ball
	}
}

```

## 有缓冲的通道

有缓冲的通道（buffered channel）是一种在被接收前能存储一个或者多个值的通道。这种类型的通道并不强制要求 goroutine 之间必须同时完成发送和接收。通道会阻塞发送和接收动作的条件也会不同。只有在通道中没有要接收的值时，接收动作才会阻塞。只有在通道没有可用缓冲区容纳被发送的值时，发送动作才会阻塞。

当通道关闭后， goroutine 依旧可以从通道接收数据，
但是不能再向通道里发送数据。

## 单向通道
通常用于函数参数, 指明在此函数中, 此通道只用于写或者读
只写单向通道 `chan <- int`
只读单向通道`<-chan int`

例子
``` go
func counter(out chan<- int) {
	for i := 0; i < 100; i++ {
		out <- i
	}
	close(out)
}

func squarer(out chan<- int, in <-chan int) {
	for i := range in {
		out <- i * i
	}
	close(out)
}
func printer(in <-chan int) {
	for i := range in {
		fmt.Println(i)
	}
}

func main() {
	ch1 := make(chan int)
	ch2 := make(chan int)
	go counter(ch1)
	go squarer(ch2, ch1)
	printer(ch2)
}
```

## 通道总结
![](_v_images/20200201105631952_12550.png =516x)
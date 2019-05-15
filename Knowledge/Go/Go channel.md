# Go channel
## 基本用法
### 创建通道
``` go
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

### 从通道中接收数据
``` go
value := <-buffered
```

### 关闭通道
``` go
unbuffered := make(chan int)
// Do Something
close(unbuffered)
```
## 无缓冲的通道
无缓冲的通道（unbuffered channel）是指在接收前没有能力保存任何值的通道。这种类型的通道要求发送 goroutine 和接收 goroutine 同时准备好，才能完成发送和接收操作。如果两个 goroutine没有同时准备好，通道会导致先执行发送或接收操作的 goroutine 阻塞等待。这种对通道进行发送和接收的交互行为本身就是同步的。其中任意一个操作都无法离开另一个操作单独存在。

### 无缓冲通道示例
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

### 有缓冲的通道

有缓冲的通道（buffered channel）是一种在被接收前能存储一个或者多个值的通道。这种类型的通道并不强制要求 goroutine 之间必须同时完成发送和接收。通道会阻塞发送和接收动作的条件也会不同。只有在通道中没有要接收的值时，接收动作才会阻塞。只有在通道没有可用缓冲区容纳被发送的值时，发送动作才会阻塞。

当通道关闭后， goroutine 依旧可以从通道接收数据，
但是不能再向通道里发送数据。

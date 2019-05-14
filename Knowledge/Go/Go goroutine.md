# Go goroutine
## 基本的使用
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

## 能看出并发效果的代码
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

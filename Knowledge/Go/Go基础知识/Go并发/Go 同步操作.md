# Go 同步操作
## Go 互斥锁Mutex

### 常规互斥锁
``` go
import "sync"
var mutex sync.Mutex

mutex.Lock()
//Do Something
mutex.Unlock()
```

### 读写互斥锁
``` go
var rwmutex sync.RWMutex

rwMutex.RLock()
//读操作
rwMutex.UnLock()


rwMutex.Lock()//写锁
//写操作
rwMutex.UnLock()
```

## sync.Once
限制某个操作只会被执行一次
``` go
var loadOnce sync.Once

func load() {
    //加载某些内容
}

func main() {
    loadOnce.Do(load)    //保证load函数只会被调用一次
    //...
}

```

## sync.Map
sync.Map是Go提供的一个开箱即用的并发安全的map
sync.Map不用像内置的map一样使用make函数初始化就能直接使用。
同时sync.Map内置了诸如Store、Load、LoadOrStore、Delete、Range等操作方法。
例子:
``` go
var m = sync.Map{}

func main() {
	wg := sync.WaitGroup{}
	for i := 0; i < 20; i++ {
		wg.Add(1)
		go func(n int) {
			key := strconv.Itoa(n)
			m.Store(key, n)
			value, _ := m.Load(key)
			fmt.Printf("k=:%v,v:=%v\n", key, value)
			wg.Done()
		}(i)
	}
	wg.Wait()
}
```

## 原子操作
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


## 监测竞争状态
访问共享资源时, 会发生竞争问题
go有自己的竞争状态监测工具
使用如下命令对go进行编译
`go bulid -race`
再运行, 如果程序发生了竞争状态, 则会报错

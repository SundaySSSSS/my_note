# Go 并发模式
## runner
runner 包用于展示如何使用通道来监视程序的执行时间，如果程序运行时间太长，也可以用 runner 包来终止程序。当开发需要调度后台处理任务的程序的时候，这种模式会很有用。

代码如下:
runner.go
``` go

// runner包管理处理任务的运行和声明周期
package runner

import (
	"errors"
	"os"
	"os/signal"
	"time"
)

//Runner在给定的超时时间内执行一组任务, 在操作系统发送中断信号时, 结束这些任务
type Runner struct {
	//报告从操作系统发送的信号的channel
	interrupt chan os.Signal
	//报告任务完成用channel
	complete chan error
	//用于管理执行任务事件的channel
	timeout <-chan time.Time
	//任务slice
	tasks [] func(int)
}

//创建两种错误类型
var ErrTimeout = errors.New("received timeout")	//超时
var ErrInterrupt = errors.New("received interrupt") //收到中断

func New(d time.Duration) *Runner {
	return &Runner {
		interrupt: make(chan os.Signal, 1), 
		complete: make(chan error), 
		timeout: time.After(d),
	}
}

//添加任务
func (r *Runner) Add(tasks ...func(int)) {
	r.tasks = append(r.tasks, tasks...)
}
//执行所有任务, 并监视通道事件
func (r *Runner) Start() error {
	signal.Notify(r.interrupt, os.Interrupt)
	go func() {
		r.complete <- r.run()
	} ()

	select {
	case err := <-r.complete:
		return err
	case <-r.timeout:
		return ErrTimeout
	}
}

// 执行所有注册的任务
func (r * Runner) run() error {
	//逐个遍历任务列表, 并执行
	for id, task := range r.tasks {
		if r.gotInterrupt() {
			return ErrInterrupt
		}
		//执行任务
		task(id)
	}
	return nil
}

func (r *Runner) gotInterrupt() bool {
	select {
	case <-r.interrupt:
		signal.Stop(r.interrupt)
		return true
	default:
		return false
	}
}
```

main.go文件
``` go
package main

import (
	"log"
	"time"
	"os"
	"runner"
)

const timeout = 3 * time.Second

func main() {
	log.Println("Starting work...")

	r := runner.New(timeout)
	r.Add(createTask(), createTask(), createTask())
	if err := r.Start(); err != nil {
		switch err {
		case runner.ErrTimeout:
			log.Println("Terminating due to timeout.")
			os.Exit(1)
		case runner.ErrInterrupt:
			log.Println("Terminating due to interrupt.")
			os.Exit(2)
		}
	}
	log.Println("Process ended.")
}

func createTask() func(int) {
	return func(id int) {
		log.Printf("Processor - Task #%d.", id)
		time.Sleep(time.Duration(id) * time.Second)
	}
}
```

## pool
pool包用于展示如何使用有缓冲的通道实现资源池，来管理可以在任意数量的goroutine之间共享及独立使用的资源。这种模式在需要共享一组静态资源的情况（如共享数据库连接或者内存缓冲区）下非 常有用。如果goroutine需要从池里得到这些资源中的一个，它可以从池里申请，使用完后归还到资源池里。
Go1.6之后的版本, 标准库中自带了资源池的实现(sync.Pool). 推荐使用

pool.go
``` go
//本包管理用户定义的一组资源
package pool

import (
	"errors"
	"log"
	"io"
	"sync"
)

type Pool struct {
	m sync.Mutex
	resources chan io.Closer
	factory func() (io.Closer, error)	//工厂函数, 由使用者提供
	closed bool
}

//请求了一个已经关闭的资源池
var ErrPoolClosed = errors.New("Pool has been closed")

func New(fn func() (io.Closer, error), size uint) (*Pool, error) {
	if (size <= 0) {
		return nil, errors.New("Size value too small")
	}
	return &Pool {
		factory: fn,
		resources: make(chan io.Closer, size), 
	}, nil
}

// 获取资源池中的资源
func (p *Pool) Acquire() (io.Closer, error) {
	select {
	//检查是否有空闲的资源
	case r, ok := <-p.resources:
		log.Println("Acquire:", "Shared Resource")
		if !ok {
			return nil, ErrPoolClosed
		}
		return r, nil
	default:	//没有空闲资源, 创建新的资源
		log.Println("Acquire:", "New Resource")
		return p.factory()
	}
}

//将一个使用后的资源放回资源池中
func (p *Pool) Release(r io.Closer) {
	p.m.Lock()
	defer p.m.Unlock()

	if p.closed {
		r.Close()
		return
	}

	select {
		//试图将资源放入队列中
	case p.resources <- r:
		log.Println("Release:", "In Queue")
	default:
		//队列已满, 关闭资源
		log.Println("Release:", "Closing")
		r.Close()
	}
}

//关闭资源池, 并关闭所有资源
func (p *Pool) Close() {
	p.m.Lock()
	defer p.m.Unlock()

	if p.closed {
		return
	}
	p.closed = true
	close(p.resources)

	for r := range p.resources {
		r.Close()
	}
}

```

main.go
``` go
package main

import (
	"log"
	"io"
	"math/rand"
	"sync"
	"sync/atomic"
	"time"
	"pool"
)

const (
	maxGoroutines = 25
	pooledResources = 2 //资源池中资源的数量
)

// 模拟要共享的资源, 假设这是一个数据库连接
type dbConnection struct {
	ID int32
}

// 实现io.Closer接口
func (dbConn *dbConnection) Close() error {
	log.Println("Close: Connection", dbConn.ID)
	return nil
}

var idCounter int32	//用于给每个虚拟的数据库连接提供独一无二的id

//工厂函数
func createConnection() (io.Closer, error) {
	id := atomic.AddInt32(&idCounter, 1)
	log.Println("Create: New Connection", id)
	return &dbConnection{id}, nil
}

func main() {
	var wg sync.WaitGroup
	wg.Add(maxGoroutines)

	//创建资源池
	p, err := pool.New(createConnection, pooledResources)
	if err != nil {
		log.Println(err)
	}
	//
	for query := 0; query < maxGoroutines; query++ {
		go func(q int) {
			performQueries(q, p)
			wg.Done()
		} (query)
	}
	wg.Wait()
	log.Println("Shutdown Program")
	p.Close()
}

func performQueries(query int, p *pool.Pool) {
	conn, err := p.Acquire()
	if err != nil {
		log.Println(err)
		return
	}
	defer p.Release(conn)

	// 用等待的方式来模拟查询
	time.Sleep(time.Duration(rand.Intn(1000)) * time.Millisecond)
	log.Printf("QID[%d] CID[%d]\n", query, conn.(*dbConnection).ID)
}

```
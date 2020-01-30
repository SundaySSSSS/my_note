# Go time包
## 基本用法
``` go
now := time.Now()
fmt.Println(now)
fmt.Println(now.Year())
fmt.Println(now.Unix())

ret := time.Unix(1580096405, 100)//用UTC时间转换为time格式
fmt.Println(ret)

fmt.Println(time.Second)	//1s
```
## 时间的加减
``` go
//time可以Add, Sub
fmt.Println(now.Add(24 * time.Hour))
fmt.Println(now.Sub(time.Unix(1580096405, 100)))
```

## 时间的比较
``` go
func (Time) Equal
func (t Time) Equal(u Time) bool
```
判断两个时间是否相同，会考虑时区的影响，因此不同时区标准的时间也可以正确比较。本方法和用t==u不同，这种方法还会比较地点和时区信息。

``` go
func (Time) Before
func (t Time) Before(u Time) bool
```
如果t代表的时间点在u之前，返回真；否则返回假。

``` go
func (Time) After
func (t Time) After(u Time) bool
```
如果t代表的时间点在u之后，返回真；否则返回假。

## 定时器
``` go
//定时器
timer := time.Tick(time.Second)
for t := range timer {
	fmt.Println(t)//一秒钟执行一次
}
```

## 时间格式化
go语言的格式化不使用"y M d h m s"的格式, 而是使用go语言的诞生时间作为格式化的依据, go诞生时间为"2006/01/02 03:04:05.000 PM"

例子:
``` go
//格式化时间
fmt.Println(now.Format("2006-01-02 15:04:05"))//2020-01-27 12:39:58
fmt.Println(now.Format("2006/01/02 03:04:05 PM"))//2020/01/27 12:39:58 PM
fmt.Println(now.Format("2006/01/02 03:04:05.000 PM"))//2020/01/27 12:39:58.022 PM
```

## 按照指定格式解析时间字符串
``` go
//按照指定格式解析时间字符串
timeObj, err := time.Parse("2006-1-02", "2020-1-27")
if (err != nil) {
	fmt.Printf("Parse time failed, err:%v\n", err)
}
fmt.Println(timeObj)//2020-01-27 00:00:00 +0000 UTC
```
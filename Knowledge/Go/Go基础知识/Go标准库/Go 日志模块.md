# go 日志模块
``` go
package main
import "os"
import "fmt"
import "log"
import "time"

func main() {
	fileObj, err := os.OpenFile("./log.txt", os.O_APPEND | os.O_CREATE | os.O_WRONLY, 0644)
	if err != nil {
		fmt.Printf("create log file err : %v\n", err)
		return
	}
	log.SetOutput(fileObj)
	for {
		log.Println("测试日志")
		time.Sleep(time.Second * 1)
	}
}
```

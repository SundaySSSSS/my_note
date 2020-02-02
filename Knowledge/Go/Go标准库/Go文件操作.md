# Go文件操作
## 打开文件
``` go
//os包中的OpenFile函数可以打开文件
func OpenFile(name string, flag int, perm FileMode)(*File, error) {

}
```
其中name为文件名
flag为打开文件的模式, 具体值如下
``` go
	O_RDONLY // open the file read-only.
	O_WRONLY // open the file write-only.
	O_RDWR // open the file read-write.
	O_APPEND // append data to the file when writing.
	O_CREATE // create a new file if none exists.
	O_EXCL   // used with O_CREATE, file must not exist.
	O_SYNC   // open for synchronous I/O.
	O_TRUNC  // 清空, 每次打开时清空打开的文件
```
perm为文件权限, 一个八进制数, 在linux环境下有效 读04 写02 执行01

## 读文件
读文件可以使用os.OpenFile或者os.Open, 后者是对前者的封装, os.Open以只读形式打开文件
### 使用File的Read方法进行文件读取
``` go
func readFromFile() {
	fileObj, err := os.Open("./main.go")
	if err != nil {
		fmt.Printf("open file failed, err:%v", err)
		return
	}
	defer fileObj.Close()
	var tmp [128]byte
	for {
		n, err := fileObj.Read(tmp[:])
		if err == io.EOF {
			fmt.Println("文件读取完毕")
			return
		}
		if err != nil {
			fmt.Printf("read from file failed, err :%v", err)
			return
		}
		fmt.Printf("读取了%d个字节\n", n)
		fmt.Println(string(tmp[:n]))
		if n < 128 {
			return
		}
	}
}
```
### 使用bufio读取文件
``` go
//利用bufio这个包读取文件
func readFromFileByBufio() {
	fileObj, err := os.Open("./main.go")
	if err != nil {
		fmt.Printf("open file failed, err:%v", err)
		return
	}
	defer fileObj.Close()
	//创建一个用来从文件中读取内容的对象
	reader := bufio.NewReader(fileObj)
	for {
		line, err := reader.ReadString('\n')
		if err == io.EOF {
			return
		}
		if err != nil {
			fmt.Printf("read line failed, err : %v", err)
			return
		}
		fmt.Println(line)
	}
}
```

### 使用ioutil的ReadFile方法
``` go
func readFromFileByIOUtil() {
	ret, err := ioutil.ReadFile("./main.go")
	if err != nil {
		fmt.Printf("read file failed, err:%v", err)
		return
	}
	fmt.Println(string(ret))
}
```

## 写文件
### 使用File的Write方法
``` go
func writeFileTest() {
	fileObj, err := os.OpenFile("./xx.txt", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0644)
	if err != nil {
		fmt.Printf("open file err : %v", err)
		return
	}
	fileObj.Write([]byte("test write file")) //写buffer
	fileObj.WriteString("明月几时有")             //写字符串
	fileObj.Close()
}
```

### 使用Bufio写文件
``` go
func writeFileByBufio() {
	fileObj, err := os.OpenFile("./xx.txt", os.O_CREATE|os.O_WRONLY|os.O_TRUNC, 0644)
	if err != nil {
		fmt.Printf("open file failed, err %v", err)
		return
	}
	defer fileObj.Close()
	//创建一个写对象
	writer := bufio.NewWriter(fileObj)
	writer.WriteString("Hello World By BufIO")
	writer.Flush()	//必须Flush, 否则写不进去, 单独的Close是不行的
}
```

### 使用ioutil写文件
``` go
func writeFileByIOUtil() {
	str := "东临碣石, 以观沧海"
	err := ioutil.WriteFile("./xx.txt", []byte(str), 0666)
	if err != nil {
		fmt.Println("write file failed, err: ", err)
		return
	}
}
```


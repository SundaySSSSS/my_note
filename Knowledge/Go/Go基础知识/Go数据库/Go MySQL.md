# Go MySQL
## 安装MySQL驱动
`go get -u github.com/go-sql-driver/mysql`

## database/sql
database/sql原生支持连接池, 且保证并发安全

数据库连接池: 维持多个数据库连接, 当需要接入数据库时, 从连接池中取出一个连接使用, 使用完毕后放回连接池. 可以避免多次创建连接

## 具体使用方法
### 登录数据库
使用sql.Open方法和Ping()方法
sql.Open中dataSourceName 应该填写:`用户名:密码@连接方式(IP:端口号)/数据库名`
例如:
用户名为root, 密码为000000, 使用TCP连接, IP端口号分别为127.0.0.1和3306, 数据库名为gotest的数据库, 使用如下字符串
`root:000000@tcp(127.0.0.1:3306)/gotest`
``` go
dsn := "root:000000@tcp(127.0.0.1:3306)/gotest"
	db, err := sql.Open("mysql", dsn) //不会校验用户名和密码
	if err != nil {                   //dsn的格式不正确的时候会报错
		fmt.Printf("dsn %s invalid, err: %v\n", dsn, err)
		return
	}

	err = db.Ping()
	if err != nil {

		fmt.Printf("open %s failed, err: %v\n", dsn, err)
		return
	}
	fmt.Println("数据库登录成功")
```

## 数据库查询
如果有一个数据库表格名为student_table,此表格有3列, id, name, age
有数据如下:
```
+----+---------+------+
| id | name    | age  |
+----+---------+------+
|  1 | caocao  |   50 |
|  2 | sunquan |   25 |
+----+---------+------+
```

调用QueryRow方法进行查询

``` go
//查询数据库
	sqlStr := `select id, name, age from student_table where id = ?`
	//执行SQL语句
	rowObj := db.QueryRow(sqlStr, 1) //获取到Row对象后, 必须调用Scan方法, 或自行Close. 否则不会释放连接池

	//拿到结果
	var stu student
	rowObj.Scan(&stu.id, &stu.name, &stu.age)
	fmt.Printf("%v\n", stu)
```

上面sqlStr中的问号被替换为了QueryRow的第二个参数1,

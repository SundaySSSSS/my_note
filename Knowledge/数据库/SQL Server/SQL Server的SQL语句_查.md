# SQL Server的SQL语句_查
## 基本语法
``` SQL
SELECT <列名> FROM <表名> [WHERE <查询条件表达式>] [ORDER BY <排序的列名>[ASC或DESC]]
```

## 基本示例
查询所有内容:
``` SQL
SELECT * FROM student
```

查询部分列
``` SQL
SELECT student_name, address FROM student
```

查询部分行和列
``` SQL
SELECT student_name, code FROM student WHERE address='北京'
```

## 使用列别名(AS)
``` SQL
SELECT code AS 学号, student_name AS 学生姓名, address AS 学生地址 FROM student WHERE address<>'河南'
```

合并列名作为新列名
``` SQL
SELECT FirstName + '.' + LastName AS 姓名 FROM employee
```
备注: 字符串的+运算是字符串连接, 数字的+运算指的是数字相加






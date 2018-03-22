# MySQL创建数据库并插入数据
## 新建数据库
```
#基本格式: CREATE DATABASE <数据库名称>;
#例如:
CREATE DATABASE mysql_test;
```
查看是否添加成功
```
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| mysql_test         |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)
```
备注:
大多数系统中SQL是不区分大小写的, 一下语句都是合法的
```
CREATE DATABASE name1;
create database name2;
CREATE database name3;
create DAtabaSE name4;
```
但是出于严谨，而且便于区分保留字（保留字(reserved word)：指在高级语言中已经定义过的字，使用者不能再将这些字作为变量名或过程名使用。）和变量名，我们把保留字大写，把变量和数据小写。

## 删除数据库
```
DROP DATEBASE mysql_test;
```

## 连接数据库
```
use mysql_test;
```

## 建立数据表
基本格式为:
```
CREATE TABLE 表的名字
(
列名a 数据类型(数据长度),
列名b 数据类型(数据长度)，
列名c 数据类型(数据长度)
);
```
例如:
```
CREATE TABLE employee (id int(10),name char(20),phone int(12));
```
也可以利用mysql命令行的特点让命令更整洁
```
mysql> CREATE TABLE department
    -> (
    -> dpt_name CHAR(20),
    -> dpt_phone INT(12)
    -> );
Query OK, 0 rows affected (0.02 sec)
```
此时再查看刚才添加的两个表格
```
mysql> show tables;
+----------------------+
| Tables_in_mysql_test |
+----------------------+
| department           |
| employee             |
+----------------------+
2 rows in set (0.01 sec)
```
## 数据类型
在刚才新建表的过程中，我们提到了数据类型，MySQL 的数据类型和其他编程语言大同小异，下表是一些 MySQL 常用数据类型：
数据类型                 |  大小(字节)        |   用途         |   格式
----------------------|-----------------|--------------|--------------
INT	| 4 |	整数 |   
FLOAT | 	4 | 	单精度浮点数	
DOUBLE | 	8 | 	双精度浮点数	
ENUM	|	 | 单选,比如性别	| ENUM('a','b','c')
SET	|   |	多选 | 	SET('1','2','3')
DATE	| 3 | 	日期 |	YYYY-MM-DD
TIME | 	3	| 时间点或持续时间	 | HH:MM:SS
YEAR | 1 | 年份值 | YYYY
CHAR | 	0~255 | 定长字符串
VARCHAR | 	0~255 | 	变长字符串
TEXT	| 0~65535 |	长文本数据
整数除了 INT 外，还有 TINYINT、SMALLINT、MEDIUMINT、BIGINT。

CHAR 和 VARCHAR 的区别: CHAR 的长度是固定的，而 VARCHAR 的长度是可以变化的，比如，存储字符串 “abc"，对于 CHAR(10)，表示存储的字符将占 10 个字节(包括 7 个空字符)，而同样的 VARCHAR(12) 则只占用4个字节的长度，增加一个额外字节来存储字符串本身的长度，12 只是最大值，当你存储的字符小于 12 时，按实际长度存储。

ENUM和SET的区别: ENUM 类型的数据的值，必须是定义时枚举的值的其中之一，即单选，而 SET 类型的值则可以多选。

## 插入数据
基本格式
```
INSERT INTO 表的名字(列名a,列名b,列名c) VALUES(值1,值2,值3);
```
例如:
```
INSERT INTO employee(id,name,phone) VALUES(01,'Tom',110110110);
INSERT INTO employee VALUES(02,'Jack',119119119)
INSERT INTO employee(id,name) VALUES(03,'Rose');
```
完成后, 表格变为:
```
mysql> SELECT * FROM employee;
+------+------+-----------+
| id   | name | phone     |
+------+------+-----------+
|    1 | Tom  | 110110110 |
|    2 | Jack | 119119119 |
|    3 | Rose |      NULL |
+------+------+-----------+
3 rows in set (0.00 sec)
```



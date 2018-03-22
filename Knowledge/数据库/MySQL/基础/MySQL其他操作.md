# MySQL其他操作

## 索引
索引是一种与表有关的结构，它的作用相当于书的目录，可以根据目录中的页码快速找到所需的内容。

当表中有大量记录时，若要对表进行查询，没有索引的情况是全表搜索：将所有记录一一取出，和查询条件进行一一对比，然后返回满足条件的记录。这样做会消耗大量数据库系统时间，并造成大量磁盘 I/O 操作。

而如果在表中已建立索引，在索引中找到符合查询条件的索引值，通过索引值就可以快速找到表中的数据，可以大大加快查询速度。
### 建立索引
对一张表中的某个列建立索引，有以下两种语句格式：
```
ALTER TABLE 表名字 ADD INDEX 索引名 (列名);
CREATE INDEX 索引名 ON 表名字 (列名);
```
我们用这两种语句分别建立索引：
```
ALTER TABLE employee ADD INDEX idx_id (id);  #在employee表的id列上建立名为idx_id的索引
CREATE INDEX idx_name ON employee (name);   #在employee表的name列上建立名为idx_name的索引
```
例如:
```
SELECT * FROM employee;
;
+----+------+------+--------+--------+--------+
| id | name | age  | salary | phone  | in_dpt |
+----+------+------+--------+--------+--------+
|  1 | Tom  |   26 |   2500 | 119119 | dpt4   |
|  2 | Jack |   24 |   2500 | 120120 | dpt2   |
|  3 | Jobs | NULL |   3600 |  19283 | dpt2   |
|  4 | Tony | NULL |   3400 | 102938 | dpt3   |
|  5 | Rose |   22 |   2800 | 114114 | dpt3   |
+----+------+------+--------+--------+--------+
5 rows in set (0.00 sec)

mysql> ALTER TABLE employee ADD INDEX idx_id (id);
mysql> CREATE INDEX idx_name ON employee (name);
```

索引的效果是加快查询速度，当表中数据不够多的时候是感受不出它的效果的。这里我们使用命令 SHOW INDEX FROM 表名字;
```
mysql> SHOW INDEX FROM employee;
SHOW INDEX FROM employee;
+----------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table    | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+----------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| employee |          0 | PRIMARY  |            1 | id          | A         |           5 |     NULL | NULL   |      | BTREE      |         |               |
| employee |          0 | phone    |            1 | phone       | A         |           5 |     NULL | NULL   |      | BTREE      |         |               |
| employee |          1 | emp_fk   |            1 | in_dpt      | A         |           3 |     NULL | NULL   |      | BTREE      |         |               |
| employee |          1 | idx_id   |            1 | id          | A         |           5 |     NULL | NULL   |      | BTREE      |         |               |
| employee |          1 | idx_name |            1 | name        | A         |           5 |     NULL | NULL   | YES  | BTREE      |         |               |
+----------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
5 rows in set (0.00 sec)
```
在使用SELECT语句查询的时候，语句中WHERE里面的条件，会自动判断有没有可用的索引。

## 视图
视图是从一个或多个表中导出来的表，是一种虚拟存在的表。它就像一个窗口，通过这个窗口可以看到系统专门提供的数据，这样，用户可以不用看到整个数据库中的数据，而只关心对自己有用的数据。

注意理解视图是虚拟的表：

数据库中只存放了视图的定义，而没有存放视图中的数据，这些数据存放在原来的表中；
使用视图查询数据时，数据库系统会从原来的表中取出对应的数据；
视图中的数据依赖于原来表中的数据，一旦表中数据发生改变，显示在视图中的数据也会发生改变；
在使用视图的时候，可以把它当作一张表。
创建视图的语句格式为：
```
CREATE VIEW 视图名(列a,列b,列c) AS SELECT 列1,列2,列3 FROM 表名字;
```
可见创建视图的语句，后半句是一个SELECT查询语句，所以视图也可以建立在多张表上，只需在SELECT语句中使用子查询或连接查询，这些在之前的实验已经进行过。

现在我们创建一个简单的视图，名为 v_emp，包含v_name，v_age，v_phone三个列：
```
mysql> CREATE VIEW v_emp (v_name, v_age, v_phone) AS SELECT name, age, phone FROM employee;
mysql> SELECT * FROM v_emp;
SELECT * FROM v_emp;
+--------+-------+---------+
| v_name | v_age | v_phone |
+--------+-------+---------+
| Tom    |    26 |  119119 |
| Jack   |    24 |  120120 |
| Jobs   |  NULL |   19283 |
| Tony   |  NULL |  102938 |
| Rose   |    22 |  114114 |
+--------+-------+---------+
5 rows in set (0.00 sec)
```
## 导入
### 基本格式
导入操作，可以把一个文件里的数据保存进一张表。导入语句格式为：
```
LOAD DATA INFILE '文件路径和文件名' INTO TABLE 表名字;
```
### 示例
MySQL默认只能导入指定目录的文件
输入如下命令查看MySQL配置:
```
show global variables like '%secure%';
```
结果为
```
+--------------------------+-----------------------+
| Variable_name            | Value                 |
+--------------------------+-----------------------+
| require_secure_transport | OFF                   |
| secure_auth              | ON                    |
| secure_file_priv         | /var/lib/mysql-files/ |
+--------------------------+-----------------------+
3 rows in set (0.00 sec)
```
`secure_file_priv`即为默认的导入路径
将文件`in.txt`放入`/var/lib/mysql-files/`中
执行如下命令即可导入:
```
LOAD DATA INFILE '/var/lib/mysql-files/in.txt' INTO TABLE employee;
SELECT * FROM employee;
+----+------+------+--------+--------+--------+
| id | name | age  | salary | phone  | in_dpt |
+----+------+------+--------+--------+--------+
|  1 | Tom  |   26 |   2500 | 119119 | dpt4   |
|  2 | Jack |   24 |   2500 | 120120 | dpt2   |
|  3 | Jobs | NULL |   3600 |  19283 | dpt2   |
|  4 | Tony | NULL |   3400 | 102938 | dpt3   |
|  5 | Rose |   22 |   2800 | 114114 | dpt3   |
|  6 | Alex |   26 |   3000 | 123456 | dpt1   |
|  7 | Ken  |   27 |   3500 | 654321 | dpt1   |
|  8 | Rick |   24 |   3500 | 987654 | dpt3   |
|  9 | Joe  |   31 |   3600 | 100129 | dpt2   |
| 10 | Mike |   23 |   3400 | 110110 | dpt1   |
| 11 | Jim  |   35 |   3000 | 100861 | dpt4   |
| 12 | Mary |   21 |   3000 | 100101 | dpt2   |
+----+------+------+--------+--------+--------+
12 rows in set (0.00 sec)
```
### 导入文件示例:
```
6	Alex	26	3000	123456	dpt1
7	Ken	27	3500	654321	dpt1
8	Rick	24	3500	987654	dpt3
9	Joe	31	3600	100129	dpt2
10	Mike	23	3400	110110	dpt1
11	Jim	35	3000	100861	dpt4
12	Mary	21	3000	100101	dpt2
```

## 导出
### 基本形式
导出与导入是相反的过程，是把数据库某个表中的数据保存到一个文件之中。导出语句基本格式为：
```
SELECT 列1，列2 INTO OUTFILE '文件路径和文件名' FROM 表名字;
```
注意：语句中 “文件路径” 之下不能已经有同名文件。

现在我们把整个employee表的数据导出到 /tmp 目录下，导出文件命名为 out.txt 具体语句为：
```
SELECT * INTO OUTFILE '/tmp/out.txt' FROM employee;
```
### 示例
```
SELECT * INTO OUTFILE '/var/lib/mysql-files/out.txt' FROM employee;
```

### 导出的文件
```
1	Tom	26	2500	119119	dpt4
2	Jack	24	2500	120120	dpt2
3	Jobs	\N	3600	19283	dpt2
4	Tony	\N	3400	102938	dpt3
5	Rose	22	2800	114114	dpt3
6	Alex	26	3000	123456	dpt1
7	Ken	27	3500	654321	dpt1
8	Rick	24	3500	987654	dpt3
9	Joe	31	3600	100129	dpt2
10	Mike	23	3400	110110	dpt1
11	Jim	35	3000	100861	dpt4
12	Mary	21	3000	100101	dpt2
```

## 备份
数据库中的数据或许十分重要，出于安全性考虑，在数据库的使用中，应该注意使用备份功能。
备份与导出的区别：导出的文件只是保存数据库中的数据；而备份，则是把数据库的结构，包括数据、约束、索引、视图等全部另存为一个文件。
`mysqldump` 是 MySQL 用于备份数据库的实用程序。它主要产生一个 SQL 脚本文件，其中包含从头重新创建数据库所必需的命令CREATE TABLE INSERT 等。

使用 mysqldump 备份的语句：
```
mysqldump -u root 数据库名>备份文件名;   #备份整个数据库
mysqldump -u root 数据库名 表名字>备份文件名;  #备份整个表
```
例如:
```
# 需要在shell中运行, 不是在mysql中运行
mysqldump -u root -p mysql_shiyan > bak.sql #实际使用时需要加上-p选项来输入root的密码
```

## 恢复
```
source /tmp/SQL6/MySQL-06.sql
```
这就是一条恢复语句，它把 MySQL-06.sql 文件中保存的mysql_shiyan 数据库恢复。

还有另一种方式恢复数据库，但是在这之前我们先使用命令新建一个空的数据库 test：
```
mysql -u root          #因为在上一步已经退出了MySQL，现在需要重新登录
CREATE DATABASE test;  #新建一个名为test的数据库
```
再次 Ctrl+Z 退出MySQL，然后输入语句进行恢复，把刚才备份的 bak.sql 恢复到 test 数据库：
```
mysql -u root test < bak.sql
```

## 实验数据
```

CREATE DATABASE mysql_shiyan;

use mysql_shiyan;

CREATE TABLE department
(
  dpt_name   CHAR(20) NOT NULL,
  people_num INT(10) DEFAULT '10',
  CONSTRAINT dpt_pk PRIMARY KEY (dpt_name)
 );

CREATE TABLE employee
(
  id      INT(10) PRIMARY KEY,
  name    CHAR(20),
  age     INT(10),
  salary  INT(10) NOT NULL,
  phone   INT(12) NOT NULL,
  in_dpt  CHAR(20) NOT NULL,
  UNIQUE  (phone),
  CONSTRAINT emp_fk FOREIGN KEY (in_dpt) REFERENCES department(dpt_name)
 );
 
CREATE TABLE project
(
  proj_num   INT(10) NOT NULL,
  proj_name  CHAR(20) NOT NULL,
  start_date DATE NOT NULL,
  end_date   DATE DEFAULT '2015-04-01',
  of_dpt     CHAR(20) REFERENCES department(dpt_name),
  CONSTRAINT proj_pk PRIMARY KEY (proj_num,proj_name)
 );

CREATE TABLE table_1
(
l_1 INT(10) PRIMARY KEY,
l_2 INT(10),
l_3 INT(10)
 );



#INSERT INTO department(dpt_name,people_num) VALUES('部门',人数);

INSERT INTO department(dpt_name,people_num) VALUES('dpt1',11);
INSERT INTO department(dpt_name,people_num) VALUES('dpt2',12);
INSERT INTO department(dpt_name,people_num) VALUES('dpt3',10);
INSERT INTO department(dpt_name,people_num) VALUES('dpt4',15);


#INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(编号,'名字',年龄,工资,电话,'部门');

INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(01,'Tom',26,2500,119119,'dpt4');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(02,'Jack',24,2500,120120,'dpt2');
INSERT INTO employee(id,name,salary,phone,in_dpt) VALUES(03,'Jobs',3600,019283,'dpt2');
INSERT INTO employee(id,name,salary,phone,in_dpt) VALUES(04,'Tony',3400,102938,'dpt3');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(05,'Rose',22,2800,114114,'dpt3');



#INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(编号,'工程名','开始时间','结束时间','部门名');

INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(01,'proj_a','2015-01-15','2015-01-31','dpt2');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(02,'proj_b','2015-01-15','2015-02-15','dpt1');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(03,'proj_c','2015-02-01','2015-03-01','dpt4');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(04,'proj_d','2015-02-15','2015-04-01','dpt3');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(05,'proj_e','2015-02-25','2015-03-01','dpt4');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(06,'proj_f','2015-02-26','2015-03-01','dpt2');
```
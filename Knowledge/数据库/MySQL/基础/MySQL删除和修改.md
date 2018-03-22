# MySQL删除和修改
## 数据库的修改
### 删除数据库
```
DROP DATABASE database_name
```
## 表的修改
### 重命名表
重命名一张表的语句有多种形式，以下 3 种格式效果是一样的：
```
RENAME TABLE 原名 TO 新名字;
ALTER TABLE 原名 RENAME 新名;
ALTER TABLE 原名 RENAME TO 新名;
```

### 删除表
```
DROP TABLE 表名字
```

### 增加一列
```
ALTER TABLE 表名字 ADD COLUMN 列名字 数据类型 约束;
# 或：
ALTER TABLE 表名字 ADD 列名字 数据类型 约束;
```
例如:
```
ALTER TABLE employee ADD height INT(4) DEFAULT 170;
```
增加完毕后表格为:
```
+----+------+------+--------+--------+--------+--------+
| id | name | age  | salary | phone  | in_dpt | height |
+----+------+------+--------+--------+--------+--------+
|  1 | Tom  |   26 |   2500 | 119119 | dpt4   |    170 |
|  2 | Jack |   24 |   2500 | 120120 | dpt2   |    170 |
|  3 | Rose |   22 |   2800 | 114114 | dpt3   |    170 |
|  4 | Jim  |   35 |   3000 | 100861 | dpt1   |    170 |
|  5 | Mary |   21 |   3000 | 100101 | dpt2   |    170 |
|  6 | Alex |   26 |   3000 | 123456 | dpt1   |    170 |
+----+------+------+--------+--------+--------+--------+
6 rows in set (0.00 sec)
```
新增加的列，被默认放置在这张表的最右边。如果要把增加的列插入在指定位置，则需要在语句的最后使用AFTER关键词(“AFTER 列1” 表示新增的列被放置在 “列1” 的后面)。
```
ALTER TABLE 表名字 ADD COLUMN 列名字 数据类型 约束;
# 或：
ALTER TABLE 表名字 ADD 列名字 数据类型 约束;
```
例如:
```
 ALTER TABLE employee ADD weight INT(4) DEFAULT 120 AFTER salary;
```
完成后, 表格变为:
```
+----+------+------+--------+--------+--------+--------+--------+
| id | name | age  | salary | weight | phone  | in_dpt | height |
+----+------+------+--------+--------+--------+--------+--------+
|  1 | Tom  |   26 |   2500 |    120 | 119119 | dpt4   |    170 |
|  2 | Jack |   24 |   2500 |    120 | 120120 | dpt2   |    170 |
|  3 | Rose |   22 |   2800 |    120 | 114114 | dpt3   |    170 |
|  4 | Jim  |   35 |   3000 |    120 | 100861 | dpt1   |    170 |
|  5 | Mary |   21 |   3000 |    120 | 100101 | dpt2   |    170 |
|  6 | Alex |   26 |   3000 |    120 | 123456 | dpt1   |    170 |
+----+------+------+--------+--------+--------+--------+--------+
6 rows in set (0.00 sec)
```
上面的效果是把新增的列加在某位置的后面，如果想放在第一列的位置，则使用 FIRST 关键词，如语句：
```
ALTER TABLE employee ADD test INT(10) DEFAULT 11 FIRST;
```
### 删除一列

```SQL
ALTER TABLE 表名字 DROP COLUMN 列名字;
# 或:
ALTER TABLE 表名字 DROP 列名字;
```
例如:
```
ALTER TABLE employee DROP test;
```
### 重命名一列
```
ALTER TABLE 表名字 CHANGE 原列名 新列名 数据类型 约束;
# 注意：这条重命名语句后面的 “数据类型” 不能省略，否则重命名失败。
```
当原列名和新列名相同的时候，指定新的数据类型或约束，就可以用于修改数据类型或约束。需要注意的是，修改数据类型可能会导致数据丢失，所以要慎重使用。
例如:
```
ALTER TABLE employee CHANGE height shengao INT(4) DEFAULT 170;
```
修改后表格变为:
```
+----+------+------+--------+--------+--------+--------+---------+
| id | name | age  | salary | weight | phone  | in_dpt | shengao |
+----+------+------+--------+--------+--------+--------+---------+
|  1 | Tom  |   26 |   2500 |    120 | 119119 | dpt4   |     170 |
|  2 | Jack |   24 |   2500 |    120 | 120120 | dpt2   |     170 |
|  3 | Rose |   22 |   2800 |    120 | 114114 | dpt3   |     170 |
|  4 | Jim  |   35 |   3000 |    120 | 100861 | dpt1   |     170 |
|  5 | Mary |   21 |   3000 |    120 | 100101 | dpt2   |     170 |
|  6 | Alex |   26 |   3000 |    120 | 123456 | dpt1   |     170 |
+----+------+------+--------+--------+--------+--------+---------+
6 rows in set (0.00 sec)
```

### 改变数据类型
要修改一列的数据类型，除了使用刚才的CHANGE语句外，还可以用这样的MODIFY语句：
```
ALTER TABLE 表名字 MODIFY 列名字 新数据类型;
```
再次提醒，修改数据类型必须小心，因为这可能会导致数据丢失。在尝试修改数据类型之前，请慎重考虑。

### 修改表格中的某个值
```
UPDATE 表名字 SET 列1=值1,列2=值2 WHERE 条件;
```
例如:
Tom原来的年龄为26, 工资为3000
```
 SELECT * FROM employee WHERE name = 'Tom'
SELECT * FROM employee WHERE name = 'Tom';
+----+------+------+--------+--------+--------+--------+---------+
| id | name | age  | salary | weight | phone  | in_dpt | shengao |
+----+------+------+--------+--------+--------+--------+---------+
|  1 | Tom  |   26 |   2500 |    120 | 119119 | dpt4   |     170 |
+----+------+------+--------+--------+--------+--------+---------+
1 row in set (0.00 sec)
```
现在改为年龄21, 工资3000
```
mysql> UPDATE employee SET age = 21, salary = 3000 WHERE name = 'Tom';
mysql> SELECT * FROM employee WHERE name = 'Tom';
+----+------+------+--------+--------+--------+--------+---------+
| id | name | age  | salary | weight | phone  | in_dpt | shengao |
+----+------+------+--------+--------+--------+--------+---------+
|  1 | Tom  |   21 |   3000 |    120 | 119119 | dpt4   |     170 |
+----+------+------+--------+--------+--------+--------+---------+
1 row in set (0.00 sec)
```
### 删除一行记录
```
DELETE FROM 表名字 WHERE 条件;
```
删除Tom
```
mysql> DELETE FROM employee WHERE name = 'Tom';
mysql> SELECT * FROM employee;
+----+------+------+--------+--------+--------+--------+---------+
| id | name | age  | salary | weight | phone  | in_dpt | shengao |
+----+------+------+--------+--------+--------+--------+---------+
|  2 | Jack |   24 |   2500 |    120 | 120120 | dpt2   |     170 |
|  3 | Rose |   22 |   2800 |    120 | 114114 | dpt3   |     170 |
|  4 | Jim  |   35 |   3000 |    120 | 100861 | dpt1   |     170 |
|  5 | Mary |   21 |   3000 |    120 | 100101 | dpt2   |     170 |
|  6 | Alex |   26 |   3000 |    120 | 123456 | dpt1   |     170 |
+----+------+------+--------+--------+--------+--------+---------+
5 rows in set (0.00 sec)
```

## 实验数据
```SQL
CREATE DATABASE test_01;

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
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(03,'Rose',22,2800,114114,'dpt3');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(04,'Jim',35,3000,100861,'dpt1');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(05,'Mary',21,3000,100101,'dpt2');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(06,'Alex',26,3000,123456,'dpt1');

#INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(编号,'工程名','开始时间','结束时间','部门名');

INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(01,'proj_a','2015-01-15','2015-01-31','dpt2');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(02,'proj_b','2015-01-15','2015-02-15','dpt1');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(03,'proj_c','2015-02-01','2015-03-01','dpt4');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(04,'proj_d','2015-02-15','2015-04-01','dpt3');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(05,'proj_e','2015-02-25','2015-03-01','dpt4');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(06,'proj_f','2015-02-26','2015-03-01','dpt2');


#INSERT INTO table_1 VALUES(01,11,12);

INSERT INTO table_1 VALUES(02,22,89);
INSERT INTO table_1 VALUES(03,56,33);
INSERT INTO table_1 VALUES(04,34,37);
INSERT INTO table_1 VALUES(05,39,32);
INSERT INTO table_1 VALUES(06,90,33);

```
# SQL SELECT基础用法
实验用的原始数据见最后
## 基本的SELECT语句
SELECT 语句的基本格式为：
```
SELECT 要查询的列名 FROM 表名字 WHERE 限制条件;
```
如果要查询表的所有内容，则把 要查询的列名 用一个星号 * 号表示
而大多数情况，我们只需要查看某个表的指定的列，比如要查看employee 表的 name 和 age：
```
SELECT name,age FROM employee;
```
输出为:
```
+------+------+
| name | age  |
+------+------+
| Tom  |   26 |
| Jack |   24 |
| Rose |   22 |
| Jim  |   35 |
| Mary |   21 |
| Alex |   26 |
| Ken  |   27 |
| Rick |   24 |
| Joe  |   31 |
| Mike |   23 |
| Jobs | NULL |
| Tony | NULL |
+------+------+
12 rows in set (0.00 sec)
```
## 数学符号条件
SELECT 语句常常会有 WHERE 限制条件，用于达到更加精确的查询。WHERE限制条件可以有数学符号 (=,<,>,>=,<=) ，刚才我们查询了 name 和 age，现在稍作修改：
```
SELECT name,age FROM employee WHERE age>25;
```
筛选出 age 大于 25 的结果：
```
+------+------+
| name | age  |
+------+------+
| Tom  |   26 |
| Jim  |   35 |
| Alex |   26 |
| Ken  |   27 |
| Joe  |   31 |
+------+------+
5 rows in set (0.00 sec)
```
或者查找一个名字为 Mary 的员工的 name,age 和 phone：
```
SELECT name,age,phone FROM employee WHERE name='Mary';
```
结果为:
```
+------+------+--------+
| name | age  | phone  |
+------+------+--------+
| Mary |   21 | 100101 |
+------+------+--------+
1 row in set (0.00 sec)
```

## 逻辑与 逻辑或
WHERE 后面可以有不止一条限制，而根据条件之间的逻辑关系，可以用 OR(或) 和 AND(且) 连接：
```
#筛选出 age 小于 25，或 age 大于 30
SELECT name,age FROM employee WHERE age<25 OR age>30;
```
结果为:
```
+------+------+
| name | age  |
+------+------+
| Jack |   24 |
| Rose |   22 |
| Jim  |   35 |
| Mary |   21 |
| Rick |   24 |
| Joe  |   31 |
| Mike |   23 |
+------+------+
7 rows in set (0.00 sec)
```
筛选出 age 大于 25，且 age 小于 30
```
SELECT name,age FROM employee WHERE age>25 AND age<30;
```
结果为:
```
+------+------+
| name | age  |
+------+------+
| Tom  |   26 |
| Alex |   26 |
| Ken  |   27 |
+------+------+
3 rows in set (0.01 sec)
```
而刚才的限制条件 age>25 AND age<30 ，如果需要包含25和30这两个数字的话，可以替换为 age BETWEEN 25 AND 30 ：
```
SELECT name, age FROM employee WHERE age BETWEEN 25 AND 30;
```
结果同上

## IN和NOT IN
关键词IN和NOT IN的作用和它们的名字一样明显，用于筛选“在”或“不在”某个范围内的结果，比如说我们要查询在dpt3或dpt4的人:
```
SELECT name, age, phone, in_dpt FROM employee WHERE in_dpt IN ('dpt3', 'dpt4');
```
结果为:
```
+------+------+--------+--------+
| name | age  | phone  | in_dpt |
+------+------+--------+--------+
| Tom  |   26 | 119119 | dpt4   |
| Rose |   22 | 114114 | dpt3   |
| Rick |   24 | 987654 | dpt3   |
| Mike |   23 | 110110 | dpt4   |
| Tony | NULL | 102938 | dpt3   |
+------+------+--------+--------+
5 rows in set (0.00 sec)
```
而NOT IN的效果则是查询不在某个范围内的数据，如下面这条命令，查询出了不在dpt1也不在dpt3的人：
```
SELECT name, age, phone, in_dpt FROM employee WHERE in_dpt NOT IN ('dpt1', 'dpt3');
```
结果为:
```
+------+------+--------+--------+
| name | age  | phone  | in_dpt |
+------+------+--------+--------+
| Tom  |   26 | 119119 | dpt4   |
| Jack |   24 | 120120 | dpt2   |
| Mary |   21 | 100101 | dpt2   |
| Joe  |   31 | 110129 | dpt2   |
| Mike |   23 | 110110 | dpt4   |
| Jobs | NULL |  19283 | dpt2   |
+------+------+--------+--------+
6 rows in set (0.00 sec)
```

## 通配符
关键字 LIKE 在SQL语句中和通配符一起使用，通配符代表未知字符。SQL中的通配符是 _ 和 % 。其中 _ 代表一个未指定字符，% 代表不定个未指定字符。
比如，要只记得电话号码前四位数为1101，而后两位忘记了，则可以用两个 _ 通配符代替：
```
SELECT name, age, phone FROM employee WHERE phone LIKE '1101__';
```
结果为:
```
+------+------+--------+
| name | age  | phone  |
+------+------+--------+
| Joe  |   31 | 110129 |
| Mike |   23 | 110110 |
+------+------+--------+
2 rows in set (0.00 sec)
```
另一种情况，比如只记名字的首字母，又不知道名字长度，则用 % 通配符代替不定个字符：
```
SELECT name, age, phone FROM employee WHERE name LIKE 'J%';
```
结果为:
```
+------+------+--------+
| name | age  | phone  |
+------+------+--------+
| Jack |   24 | 120120 |
| Jim  |   35 | 100861 |
| Joe  |   31 | 110129 |
| Jobs | NULL |  19283 |
+------+------+--------+
4 rows in set (0.00 sec)
```

## 对结果排序
为了使查询结果看起来更顺眼，我们可能需要对结果按某一列来排序，这就要用到 ORDER BY 排序关键词。默认情况下，ORDER BY的结果是升序排列，而使用关键词ASC和DESC可指定升序或降序排序。
```
SELECT name, age, salary, phone FROM employee ORDER BY salary DESC;
```
结果为:
```
+------+------+--------+--------+
| name | age  | salary | phone  |
+------+------+--------+--------+
| Joe  |   31 |   3600 | 110129 |
| Jobs | NULL |   3600 |  19283 |
| Ken  |   27 |   3500 | 654321 |
| Rick |   24 |   3500 | 987654 |
| Mike |   23 |   3400 | 110110 |
| Tony | NULL |   3400 | 102938 |
| Jim  |   35 |   3000 | 100861 |
| Mary |   21 |   3000 | 100101 |
| Alex |   26 |   3000 | 123456 |
| Rose |   22 |   2800 | 114114 |
| Tom  |   26 |   2500 | 119119 |
| Jack |   24 |   2500 | 120120 |
+------+------+--------+--------+
12 rows in set (0.00 sec)
```

## SQL内置函数和计算
SQL 允许对表中的数据进行计算。对此，SQL 有 5 个内置函数，这些函数都对 SELECT 的结果做操作：

函数名                |  COUNT        |   SUM         |   AVG | MAX | MIN
---------------|-----------------|--------------|-------|----|---
作用|计数|求和|求平均值|最大值|最小值

其中 COUNT 函数可用于任何数据类型(因为它只是计数)，而 SUM 、AVG 函数都只能对数字类数据类型做计算，MAX 和 MIN 可用于数值、字符串或是日期时间数据类型。
具体举例，比如计算出salary的最大、最小值，用这样的一条语句：
```
SELECT MAX(salary) AS max_salary, MIN(salary) FROM employee;
```
结果为:
```
+------------+-------------+
| max_salary | MIN(salary) |
+------------+-------------+
|       3600 |        2500 |
+------------+-------------+
1 row in set (0.00 sec)
```
其中MAX(salary)被AS重命名为了max_salary

## 子查询
上面讨论的 SELECT 语句都仅涉及一个表中的数据，然而有时必须处理多个表才能获得所需的信息。例如：想要知道名为名字为"J"开头 的员工所在部门做了几个工程。员工信息储存在 employee 表中，但工程信息储存在project 表中。

对于这样的情况，我们可以用子查询：

```
SELECT of_dpt FROM project WHERE of_dpt IN (SELECT in_dpt FROM employee WHERE name LIKE 'J%');
```
结果为:
```
+--------+
| of_dpt |
+--------+
| dpt2   |
| dpt2   |
| dpt1   |
+--------+
```

## 连接查询
在处理多个表时，子查询只有在结果来自一个表时才有用。但如果需要显示两个表或多个表中的数据，这时就必须使用连接 (join) 操作。

连接的基本思想是把两个或多个表当作一个新的表来操作，如下：
```
Select id, name, people_num FROM employee, department WHERE employee.in_dpt = department.dpt_name ORDER BY id;
```
这条语句查询出的是，各员工所在部门的人数，其中员工的 id 和 name 来自 employee 表，people_num 来自 department 表：
```
+----+------+------------+
| id | name | people_num |
+----+------+------------+
|  1 | Tom  |         15 |
|  2 | Jack |         12 |
|  3 | Rose |         10 |
|  4 | Jim  |         11 |
|  5 | Mary |         12 |
|  6 | Alex |         11 |
|  7 | Ken  |         11 |
|  8 | Rick |         10 |
|  9 | Joe  |         12 |
| 10 | Mike |         15 |
| 11 | Jobs |         12 |
| 12 | Tony |         10 |
+----+------+------------+
12 rows in set (0.01 sec)
```
另一个连接语句格式是使用 JOIN ON 语法，刚才的语句等同于：
```
SELECT id, name, people_num FROM employee JOIN department ON employee.in_dpt = department.dpt_name ORDER BY id;
```
结果也与之前相同

## 实验原始数据
MySQL-04-01.sql
```SQL
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
```

MySQL-04-02.sql
```SQL

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
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(07,'Ken',27,3500,654321,'dpt1');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(08,'Rick',24,3500,987654,'dpt3');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(09,'Joe',31,3600,110129,'dpt2');
INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(10,'Mike',23,3400,110110,'dpt4');
INSERT INTO employee(id,name,salary,phone,in_dpt) VALUES(11,'Jobs',3600,019283,'dpt2');
INSERT INTO employee(id,name,salary,phone,in_dpt) VALUES(12,'Tony',3400,102938,'dpt3');


#INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(编号,'工程名','开始时间','结束时间','部门名');

INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(01,'proj_a','2015-01-15','2015-01-31','dpt2');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(02,'proj_b','2015-01-15','2015-02-15','dpt1');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(03,'proj_c','2015-02-01','2015-03-01','dpt4');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(04,'proj_d','2015-02-15','2015-04-01','dpt3');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(05,'proj_e','2015-02-25','2015-03-01','dpt4');
INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(06,'proj_f','2015-02-26','2015-03-01','dpt2');
```


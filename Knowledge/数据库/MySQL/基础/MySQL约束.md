# SQL约束

## MySQL示例:
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

```

## 主键
主键 (PRIMARY KEY)是用于约束表中的一行，作为这一行的唯一标识符，在一张表中通过主键就能准确定位到一行，因此主键十分重要。主键不能有重复且不能为空。
### 定义主键的方法
```
# 例如employee中的id
  id      INT(10) PRIMARY KEY,
# 例如department中的dpt_pk和dpt_name
CONSTRAINT dpt_pk PRIMARY KEY (dpt_name)
# 复合主键, 如project中的proj_pk (proj_num和proj_name共同构成了一个主键)
CONSTRAINT proj_pk PRIMARY KEY (proj_num,proj_name)
```
## 默认值约束
默认值约束 (DEFAULT) 规定，当有 DEFAULT 约束的列，插入数据为空时，将使用默认值。
DEFAULT 约束只会在使用 INSERT 语句时体现出来，INSERT语句中，如果被 DEFAULT 约束的位置没有值，那么这个位置将会被 DEFAULT 的值填充
```
# 例如department中的people_num
people_num INT(10) DEFAULT '10',
```
## 唯一约束
唯一约束 (UNIQUE) 规定一张表中指定的一列的值必须不能有重复值，即这一列每个值都是唯一的。
```
# 例如employee中的phone
phone   INT(12) NOT NULL,
```

## 非空约束
非空约束 (NOT NULL)的列，在插入值时必须非空。
```
# 例如employee中的salary, phone, in_dpt
  salary  INT(10) NOT NULL,
  phone   INT(12) NOT NULL,
  in_dpt  CHAR(20) NOT NULL,
```
## 外键约束
外键 (FOREIGN KEY) 既能确保数据完整性，也能表现表之间的关系。
一个表可以有多个外键，每个外键必须 REFERENCES (参考) 另一个表的主键，被外键约束的列，取值必须在它参考的列中有对应值。

```
# 例如employee中的emp_fk
  CONSTRAINT emp_fk FOREIGN KEY (in_dpt) REFERENCES department(dpt_name)
```


# MySQL简单示例-简易成绩管理系统

## 题目要求
现需要构建一个简易的成绩管理系统的数据库，来记录几门课程的学生成绩。数据库中有三张表分别用于记录学生信息、课程信息和成绩信息。

数据库表的数据如下：
学生表(student)：学生 id 、学生姓名和性别
![](_v_images/_1517654299_21084.png)

课程表：课程 id 和课程名
![](_v_images/_1517654317_29265.png)


成绩表：成绩 id 、学生 id 、课程 id 和分数
![](_v_images/_1517654339_26467.png)


目标
1.MySQL 服务处于运行状态
2.新建数据库的名称为 gradesystem
3.gradesystem 包含三个表：student、course、mark；

student 表包含3列：sid(主键)、sname、gender；
course 表包含2列：cid(主键)、cname；
mark 表包含4列：mid(主键)、sid、cid、score ，注意与其他两个表主键之间的关系。
4.将上述表中的数据分别插入到各个表中

提示

建立表时注意 id 自增和键约束
每个表插入语句可通过一条语句完成

```SQL
DROP DATABASE gradesystem;

CREATE DATABASE gradesystem;

use gradesystem;

CREATE TABLE student
(
    sid INT(10) PRIMARY KEY,
    sname CHAR(64),
    gender ENUM('male', 'female')
);

CREATE TABLE course
(
    cid INT(10) PRIMARY KEY,
    cname CHAR(64)
);

CREATE TABLE mark
(
    mid INT(10) PRIMARY KEY,
    sid INT(10),
    cid INT(10),
    score INT(10)
);


INSERT INTO student(sid, sname, gender) VALUES(01, 'Tom', 'male');
INSERT INTO student(sid, sname, gender) VALUES(02, 'Jack', 'male');
INSERT INTO student(sid, sname, gender) VALUES(03, 'Rose', 'female');

INSERT INTO course(cid, cname) VALUES(1, 'math');
INSERT INTO course(cid, cname) VALUES(2, 'physics');
INSERT INTO course(cid, cname) VALUES(3, 'chemistry');

INSERT INTO mark(mid, sid, cid, score) VALUES(1, 1, 1, 80);
INSERT INTO mark(mid, sid, cid, score) VALUES(2, 2, 1, 85);
INSERT INTO mark(mid, sid, cid, score) VALUES(3, 3, 1, 90);
INSERT INTO mark(mid, sid, cid, score) VALUES(4, 1, 2, 60);
INSERT INTO mark(mid, sid, cid, score) VALUES(5, 2, 2, 90);
INSERT INTO mark(mid, sid, cid, score) VALUES(6, 3, 2, 75);
INSERT INTO mark(mid, sid, cid, score) VALUES(7, 1, 3, 95);
INSERT INTO mark(mid, sid, cid, score) VALUES(8, 2, 3, 75);
INSERT INTO mark(mid, sid, cid, score) VALUES(9, 3, 3, 85);

show tables;
select * from student;
select * from course;
select * from mark;


```

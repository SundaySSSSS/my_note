# SQL Server的T-SQL语句
## 基础
### T-SQL
T-SQL语句是SQL的增强版
对SQL的功能进行了扩充: 如变量说明, 流程控制, 功能函数
### SQL的组成
#### DML数据操作语言
插入, 删除, 修改数据库中的数据
INSERT, UPDATE, DELETE等

#### DCL数据控制语言
用来控制存取许可,存取权限等
GRANT, REVOKE等

#### DQL数据查询语言
用来查询数据库中的数据
SELECT等

#### DDL数据定义语言
用来建立数据库, 数据库对象和定义表的列
CTEATE TABLE, DROP TABLE 等

### SQL中的运算符
算术运算
+-*/(整除) %(取余)
赋值运算
=
逻辑运算
AND OR NOT

比较运算符
```
=
>
<
>=
<=
<> 不等于(推荐使用的方式)
!= 不等于(非SQL-92标准, 不推荐使用)
```

## 增删改
### 增(INSERT)
#### 基本示例
``` SQL
INSERT [INTO] 表名 [(列名)] VALUES (值列表)
例如:
INSERT INTO student(sname, saddress, sgrade, semail, ssex) 
values('张三','北京',1,'zhangsan@126.com', 1)
```
#### 注意事项
1, 必须将一整行的数据插全
2, 注意插入数据的类型匹配
3, 自增列不能赋值
4, 赋空值可以使用NULL关键字
5, 插入默认值使用DEFAULT关键字

#### 插入其他表中的数据
方法1
``` SQL
INSERT INTO <表名>(列名) SELECT <列名> FROM <源表名>
例如: 把student表中sname, saddress, semail列插入addresslist表中
INSERT INTO addresslist(name, address, email) SELECT sname, saddress, semail FROM student
备注: addresslist表必须已经存在, 且存在name, address, email三列
```
方法2
``` SQL
SELECT sname, saddress INTO student_bak from student
```
备注: student_bak允许不存在, 会新建此表

#### 插入多行数据
``` SQL
INSERT INTO <表名>(列名)
SELECT<列名> UNION
SELECT<列名> UNION
例如:
INSERT student(sname, sgrade, ssex)
SELECT '张三', 7, 1 UNION
SELECT '李四', 4, 0 UNION
SELECT '王五', 5, 1 UNION
```

### 删(DELETE)

### 改(UPDATE)
#### 基本示例
```SQL
UPDATE 表名 SET 列名=更新值, 列名=更新值, ... [WHERE 更新条件]
示例:
UPDATE student SET ssex = 0  -- 将所有性别更新为0
UPDATE student SET saddress='上海' WHERE saddress='北京' --将所有地址为北京的记录更新为上海
UPDATE test_scores SET scores=scores+5 WHERE scores<=95 -- 将所有分数低于95分的提高5分
```

## 查


## 导入导出
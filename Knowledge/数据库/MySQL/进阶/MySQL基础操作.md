# MySQL 基础操作
## 数据库操作
### SHOW DATABASES 显示当前存在的数据库
```sql
SHOW DATABASES;
```

### CREATE DATABASE 创建数据库
```sql
CREATE DATABASE test;
```

### USE 选定数据库
```sql
USE test;
```

## 表操作
### CREATE TABLE 创建表
下面创建一个关于宠物的表, 拥有如下信息:
名字、主人、种类，性别、出生和死亡日期
```sql
CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);
```
VARCHAR适合于name、owner和species列，因为这些列值的长度是可以变化的，这些列的长度不必都相同，而且不必是20。你可以选从1到65535选择一个最合理的值作为列属性值的长度。如果选择得不合适，MySQL提供一个ALTER TABLE语句来修改表格（后来证明你需要一个更长的字段）。

动物性别可以由多个名称表示，例如，"m"和"f"，或"male"和"female"。使用单字符"m"和"f"是最简单的方法。

很显然，birth和death列应选用DATE（日期）数据类型。

### SHOW TABLES 显示数据库中存在的表格
```sql
SHOW TABLES;
```
执行完毕后只显示存在哪些表格, 具体表格内容不会显示

### DESCRIBE 显示表格有哪些列
下面显示一个叫做pet的表格的列信息
```sql
DESCRIBE pet;
```
显示内容如下:
```
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| name    | varchar(20) | YES  |     | NULL    |       |
| owner   | varchar(20) | YES  |     | NULL    |       |
| species | varchar(20) | YES  |     | NULL    |       |
| sex     | char(1)     | YES  |     | NULL    |       |
| birth   | date        | YES  |     | NULL    |       |
| death   | date        | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+
```

### LOAD DATA 将数据文件加载到表中
从一个空表开始的，填充它的一个简易方法是创建一个文本文件，每个动物各一行，然后用一个语句将文件的内容加载到表中。
你可以根据上面的宠物记录创建一个文本文件“pet.txt”，每行包含一个记录，用定位符(tab)把值分开，并且按照上面的CREATE TABLE语句中列出的次序依次填写数据。对于丢失的值(例如未知的性别，或仍然活着的动物的死亡日期)，你可以使用\N（反斜线，字母N）表示该值属于NULL。
pet.txt的内容可以如下:
```
Fluffy	Harold	cat	f	1993-02-04	\N
Claws	Gwen	cat	m	1994-03-17	\N
Buffy	Harold	dog	f	1989-05-13	\N
Fang	Benny	dog	m	1990-08-27	\N
Bowser	Diane	dog	m	1979-08-31	1995-07-29
Chirpy	Gwen	bird	m	1998-09-11	\N
Whister	Gwen	bird	m	1997-12-09	\N
Slim	Benny	snake	m	1996-04-29	\N
```

MySQL默认只能导入指定目录的文件
输入如下命令查看MySQL配置:
```sql
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
```
secure_file_priv即为默认的导入路径
将文件pet.txt放入/var/lib/mysql-files/中
执行如下命令即可导入:
```sql
LOAD DATA INFILE '/var/lib/mysql-files/pet.txt' INTO TABLE pet;
```

### INSERT INTO 向表格中插入一行
```
INSERT INTO pet VALUES('Puffball', 'Diane', 'hamster', 'f', '1999-03-30', NULL);
```

### SELECT 从表格中检索
#### 选择所有数据
```
SELECT * FROM pet;
```
#### 选择特殊列
```
mysql> SELECT name, birth FROM pet;
```
#### DISTINCT 避免重复
增加关键字DISTINCT检索出每条唯一的输出记录：
```
mysql> SELECT DISTINCT owner FROM pet;
```

### UPDATE 更新表格中某个项的值
```
UPDATE pet SET birth = '1989-08-31' WHERE name = 'Bowser';
```

### WHERE 条件限定
```
mysql> SELECT * FROM pet WHERE birth > '1998-1-1';
```
还可以使用AND语句组合筛选条件，例如，找出雌性的狗：
```
mysql> SELECT * FROM pet WHERE species = 'dog' AND sex = 'f';
```
有AND逻辑操作符，那么就有一个OR操作符：
```
mysql> SELECT * FROM pet WHERE species = 'snake' OR species = 'bird';
```
AND和OR可以混用，但AND比OR具有更高的优先级。如果你使用两个操作符，最好是使用圆括号指明如何按条件分组：
```
mysql> SELECT * FROM pet WHERE (species = 'cat' AND sex = 'm')
    -> OR (species = 'dog' AND sex = 'f');
```

### ORDER BY 规定顺序
使用ORDER BY关键字进行排序, 默认为升序
```
SELECT name, birth FROM pet ORDER BY birth;
```
如果想要降序, 可以使用DESC关键字
```
SELECT name, birth FROM pet ORDER BY birth DESC;
```

可以对多个列进行排序，并且可以按不同的方向对不同的列进行排序。例如，按升序对动物的种类进行排序，然后按降序根据生日对各动物种类进行排序（最年轻的动物在最前面），使用下列查询：
```
SELECT name, species, birth FROM pet ORDER BY species, birth DESC;
```
注意DESC关键字仅适用于在它前面的列名(birth)；不影响species列的排序顺序。

## 匹配模式
### SQL匹配模式
MySQL提供标准的SQL模式匹配，以及一种基于类Unix里的程序如vi、grep和sed里的扩展正则表达式模式匹配的格式。 SQL模式匹配允许你使用“_”匹配任何单个字符，而“%”匹配任意数目字符(包括零字符)。在 MySQL中，SQL的模式默认是忽略大小写的。下面给出一些例子。注意使用SQL模式时，不能使用=或!=；而应使用LIKE或NOT LIKE比较操作符。 要想找出以“b”开头的名字的动物信息：

`mysql> SELECT * FROM pet WHERE name LIKE 'b%';`
要想找出以“fy”结尾的名字：

`mysql> SELECT * FROM pet WHERE name LIKE '%fy';`
要想找出包含“w”的名字：

`mysql> SELECT * FROM pet WHERE name LIKE '%w%';`
要想找出正好包含5个字符的名字，使用“_”模式字符：

`mysql> SELECT * FROM pet WHERE name LIKE '_____';`
### 正则匹配
使用REGEXP和NOT REGEXP操作符(或RLIKE和NOT RLIKE，它们是同义词)。

扩展正则表达式的一些字符是：

‘.’匹配任何单个的字符。

字符类“[...]”匹配在方括号内的任何字符。例如，“[abc]”匹配“a”、“b”或“c”。为了命名字符的范围，使用一个“-”。“[a-z]”匹配任何字母，而“[0-9]”匹配任何数字。

“ ”匹配零个或多个在它前面的字符。例如，“x”匹配任何数量的“x”字符，“[0-9]”匹配任何数量的数字，而“.”匹配任何数量的任何字符。

如果REGEXP模式与被测试值的任何地方匹配，模式就匹配(这不同于LIKE模式匹配，只有与整个值匹配，模式才匹配)。 为了定位一个模式以便它必须匹配被测试值的开始或结尾，在模式开始处使用“^”或在模式的结尾用“$”。 为了说明扩展正则表达式如何工作，下面使用REGEXP重写上面所示的LIKE查询：

为了找出以“b”开头的名字，使用“^”匹配名字的开始：

`mysql> SELECT * FROM pet WHERE name REGEXP '^b';`
如果你想强制使REGEXP比较区分大小写，使用BINARY关键字使其中一个字符串变为二进制字符串。该查询只匹配名称首字母的小写‘b’。

`mysql> SELECT * FROM pet WHERE name REGEXP BINARY '^b';`
为了找出以“fy”结尾的名字，使用“$”匹配名字的结尾：

`mysql> SELECT * FROM pet WHERE name REGEXP 'fy$';`
为了找出包含一个“w”的名字，使用以下查询：

`mysql> SELECT * FROM pet WHERE name REGEXP 'w';`
既然如果一个正则表达式出现在值的任何地方，他就会被模式匹配，就不必在先前的查询中在模式的两侧放置一个通配符以使得它匹配整个值，就像你使用了一个SQL模式那样。

为了找出包含正好5个字符的名字，使用“^”和“$”匹配名字的开始和结尾，和5个“.”实例在两者之间：

`mysql> SELECT * FROM pet WHERE name REGEXP '^.....$';`
你也可以使用“{n}”重复n次操作符,重写前面的查询：

`mysql> SELECT * FROM pet WHERE name REGEXP '^.{5}$';`


## 函数
### 日期时间相关
#### CURTIME() CURDATE() NOW() 获取当前日期,时间
调用结果如下:
NOW()	| CURDATE() | CURTIME()
---------|-------------|-----------
2008-12-29 16:25:46 | 	2008-12-29 | 	16:25:46

#### DAY() MONTH() YEAR() 日期截取函数
取时间字段的天, 月, 年

#### TIMESTAMPDIFF() 计算日期差
基本形式:
```
TIMESTAMPDIFF(单位，开始时间，结束时间)
```
例如:
```
SELECT name, birth, CURDATE(), TIMESTAMPDIFF(YEAR, birth, CURDATE()) AS age FROM pet;
```
选出的结果为:
```
+---------+------------+------------+------+
| name    | birth      | CURDATE()  | age  |
+---------+------------+------------+------+
| Fluffy  | 1993-02-04 | 2018-02-19 |   25 |
| Claws   | 1994-03-17 | 2018-02-19 |   23 |
| Buffy   | 1989-05-13 | 2018-02-19 |   28 |
| Fang    | 1990-08-27 | 2018-02-19 |   27 |
| Bowser  | 1979-08-31 | 2018-02-19 |   38 |
| Chirpy  | 1998-09-11 | 2018-02-19 |   19 |
| Whister | 1997-12-09 | 2018-02-19 |   20 |
| Slim    | 1996-04-29 | 2018-02-19 |   21 |
+---------+------------+------------+------+
```
### 行数计算
数据库经常用于回答这个问题，“查询出某个类型的数据在表中出现的频数是多少?”

例如，你可能想要知道你有多少宠物，或每位主人有多少宠物，或你可能想要对你的动物进行各种类型的普查。

计算你拥有动物的总数目与“在pet表中有多少行?”是同样的问题，因为每个宠物都对应一条记录。COUNT(*)函数计算行数，所以计算动物数目的查询应为：

`mysql> SELECT COUNT(*) FROM pet;`
在前面的章节中，你检索了拥有宠物的人的名字。如果你想要知道每个主人有多少宠物，你也可以使用COUNT(*)函数：

`mysql> SELECT owner, COUNT(*) FROM pet GROUP BY owner;`
注意，使用GROUP BY对每个owner的所有记录分组，没有它，你会得到错误消息：
```
mysql> SELECT owner, COUNT(*) FROM pet;
ERROR 1140 (42000): Mixing of GROUP columns (MIN(),MAX(),COUNT(),...)
with no GROUP columns is illegal if there is no GROUP BY clause
```
COUNT(*)和GROUP BY以各种形式分类你的数据。下列例子显示出以不同方式进行动物普查操作。

查看每种动物的数量：

`mysql> SELECT species, COUNT(*) FROM pet GROUP BY species;`
查看每种性别的动物数量：

`mysql> SELECT sex, COUNT(*) FROM pet GROUP BY sex;`
按种类和性别组合分类的动物数量：

`mysql> SELECT species, sex, COUNT(*) FROM pet GROUP BY species, sex;`
若使用COUNT(*)，你不必检索整个表。例如, 当只对狗和猫进行查询时，应为：
```
mysql> SELECT species, sex, COUNT(*) FROM pet
    -> WHERE species = 'dog' OR species = 'cat'
    -> GROUP BY species, sex;
```
或，如果你仅需要知道已知性别的按性别分组的动物数目：
```
mysql> SELECT species, sex, COUNT(*) FROM pet
    -> WHERE sex IS NOT NULL
    -> GROUP BY species, sex;
```
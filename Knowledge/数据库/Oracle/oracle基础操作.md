# oracle基础操作
## oracle的安装
全局数据库名: orcl
口令: 000000

oracle安装会自动生成两个用户: sys和system
sys是超级用户, 具有最高权限, 具有sysdba角色, 具有create database权限, 默认密码为manager(10g下)
system是 管理操作员, 权限很大, 具有sysoper角色, 没有create database权限, 默认密码为change_on_install(10g下)
一般来讲, 对数据库维护, 使用system用户就可以了

oracle安装完毕后, 会在后台作为服务启动, 如ORCL数据库, 会启动一个OracleServiceORCL服务

## oracle的卸载
不能用控制面板
自己从网上查吧

## 用户管理
用户身份：
sysdba 数据库管理员
sysoper 数据库操作员 
normal 普通用户 只能查询

创建用户：
CREATE USER 用户名 IDENTIFIED BY 口令 [ACCOUNT LOCK|UNLOCK]
语法解析：
LOCK|UNLOCK 创建用户时是否锁定，默认为锁定状态。锁定的用户无法正常的登录进
行数据库操作。

例如：
CREATE USER jerry IDENTIFIED BY 123 ACCOUNT UNLOCK;

创建完用户后, 还需要给他权限, 
grant create connect,resource to 用户名
例如:
grant create connect,resource to jerry

登录oracle
安装完毕后, 可以在开始菜单中找到SQL Plus工具
打开, 输入用户名密码, 可以登录

用户相关命令:
show user: 显示当前登录的用户

连接命令
conn 用户名/密码 @网络服务名 as sysdba/sysoper/normal
例如:
conn sott/tiger;

断开连接
disc

修改密码:
passw 可以修改自己的密码, 如果要修改其他人的密码, 需要用sys或system
输入passw后, 按照提示操作即可

退出:
exit

## 文件操作命令:
### 运行sql脚本
start和@
例如:
start d:\a.sql
或
@ d:\a.sql

### edit
编辑指定sql脚本
例如: edit d:\a.sql

### spool
将sql*plus屏幕上的内容输出到文件中
spool d:\b.sql <-文件开始建立, 等待用户输入
*** <-输入各种命令
spool off <-停止输入

## 表格操作
### 显示所有表格
`select * from tab;`

### 创建表格:
`create table people(id number(9) primary key, name varchar2(40) not null);`

### 删除表格:
`drop table [table_name];`
例如:
`drop table test;`

问题:
在oracle中drop掉了一张表，表是删除了，但是会自动生成一个表名为BIN$DIb3jDFOQA2CVQWgNxEPXg==$0的数据库表。

解决：
这个是oracle10g以上的闪回技术，类似回收站，你可以用sql命令永久删除：
```sql
SQL>purge table "BIN$DIb3jDFOQA2CVQWgNxEPXg==$0";
```

### 插入数据:
`insert into people values(1, 'cxy');`

### 更新数据
```sql
UPDATE 表名称 SET 列名称 = 新值 WHERE 列名称 = 某值;
```
例如:
```sql
UPDATE Person SET FirstName = 'Fred' WHERE LastName = 'Wilson';
```

### 简单查找:
`select * from people;`

### 判断表格是否存在:
`select count(*) from user_tables where table_name='PEOPLE';`
其中表格名为PEOPLE, 必须全为大写

### 表格信息
`desc table_name;`




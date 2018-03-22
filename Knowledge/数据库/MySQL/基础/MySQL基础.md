# MySQL基础

## MySQL的安装
### 利用apt包管理器安装MySQL
```
#安装 MySQL 服务端、核心程序
sudo apt-get install mysql-server
# 安装时会要求建立mysql root的密码

#安装 MySQL 客户端
sudo apt-get install mysql-client
```

### 验证是否安装成功
```
sudo netstat -tap | grep mysql
```
如果提示如下内容表示安装成功
```
tcp        0      0 localhost:mysql         *:*                     LISTEN      5821/mysqld
```

## MySQL的登陆和基本使用
### 启动MySQL
```
sudo service mysql start
```
### 使用root登陆
```
mysql -u root -p
```
输入安装mysql时创建的密码即可登陆

### 查看数据库
```
show databases;
```
会显示已有的数据库, 例如:
```
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)
```

### 连接数据库
使用use + 数据库名, 可以连接指定的数据库
```
use information_schema
```

### 查看表
连接某个数据库后, 可以查看存在哪些表
```
show tables;
```

### 退出MySQL
```
quit
```
或者
```
exit
```


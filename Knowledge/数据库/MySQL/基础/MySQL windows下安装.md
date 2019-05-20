# MySQL windows下安装
1, 下载zip包, 解压, 将解压的文件夹放到适合的目录下, 比如
`C:\Program Files\MySql`
2, 设置PATH环境变量添加`C:\Program Files\MySql\bin`
3, 以管理员启动命令行, cd到`C:\Program Files\MySql\bin`目录下
4, 执行`mysqld -install`
5, 执行`mysqld --initialize-insecure --user=mysql`
6, 执行`net start mysql`
7, 可以使用root登录了`mysql -u root -p`

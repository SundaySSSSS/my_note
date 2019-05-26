# Qt连接mysql提示错误

## QSqlDatabase: QMYSQL driver not loaded

在Qt 5.9中使用数据库连接时，弹出下面的错误：

QSqlDatabase: QMYSQL driver not loaded
QSqlDatabase: available drivers: QSQLITE QMYSQL QMYSQL3 QODBC QODBC3 QPSQL QPSQL7
从上面的错误可以看出，错误发生在MySQL数据库驱动并未加载。

对于这种错误一般有两种解决方案：

第一种：无MySQL驱动。

在这种情况下，检查 Qt\5.3\msvc2013_64_opengl\plugins 目录下是否有qsqlmysql.dll。如果没有，就说明Qt没有相应的mysql驱动。

这时，在QSqlDatabase: available drivers: QSQLITE QMYSQL QMYSQL3 QODBC QODBC3 QPSQL QPSQL7 报错中没有QMYSQL项。

解决方法是：拷贝qmysql.dll至plugins目录下。

第二种：库支持不完善。

解决方法是：将MySQL\MySQL Server 5.7\lib下的libmysql.dll拷贝至Qt\5.3\msvc2013_64_opengl\bin下即可。
# QT操作oracle数据库

## 插入数据方法
方法1:
``` C++
QSqlQuery query(m_db);
query.exec(QString("INSERT INTO TEST2(id, age) VALUES(3, 28)"));
```
方法2:
```C++
QSqlQuery query(m_db);
query.prepare("INSERT INTO TEST2(id, age)"
           "VALUES (?,?)");
int id = 3;
int age = 28;
query.addBindValue(id);
query.addBindValue(age);
query.exec();
```

备注: 插入数据时, 用户不能在别的客户端登录, 如果已经登录, 则query.exec()会等待用户在其他地点下线, 会一直等待.

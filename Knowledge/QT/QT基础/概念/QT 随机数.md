# QT 随机数
生成0-9之间的随机数
``` C++
qsrand(QTime(0, 0, 0).secsTo(QTime::currentTime()));
int randomNum = qrand() % 10;
```

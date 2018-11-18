# QT 格式化字符串

## 方法1 使用sprintf

```C++
int m_baudRateCur = 100;
QString strTest("Tst");
QString strSerInfo;
QByteArray baTmp = strTest.toLatin1();
strSerInfo.sprintf("%s %d",baTmp.data(),m_baudRateCur);
hintSerSts->setText(strSerInfo);
```

## 方法2 使用arg

```C++
int m_baudRateCur = 100;
QString strTest("Tst");
QString str;
str = QString("%1 %2").arg(strTest).arg(m_baudRateCur);
```
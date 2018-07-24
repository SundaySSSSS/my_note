# QString和数字之间的转换
## 把QString转换为 double类型

方法1.QString str="123.45";
```
double val=str.toDouble(); //val=123.45
```
方法2.很适合科学计数法形式转换
```
bool ok;
double d;
d=QString("1234.56e-02").toDouble(&ok); //ok=true;d;12.3456.
```
## 把QString转换为float形

1.
```
QString str="123.45";
float d=str.toFloat(); //d=123.45
```
2.
```
QString str="R2D2";
bool ok;
float d=str.toFloat(&ok); //转换是被时返回0.0,ok=false;
```

## 把QString形转换为整形

注意：基数默认为10。当基数为10时，并且基数必须在2到36之间。如果基数为0，若字符串是以0x开头的就会转换为16进制，若以0开头就转换为八进制，否则就转换为十进制。
```
Qstring str="FF";
bool ok;
int dec=str.toInt(&ok,10); //dec=255 ; ok=rue
int hex =str.toInt(&ok,16); //hex=255;ok=true;
```

## 常整形转换为Qstring形
```
long a =63;
QString str=QString::number(a,16); //str="3f";
QString str=QString::number(a,16).toUpper(); //str="3F";
```
## Qstring 转换char*问题

方法一:
```
QString qstr("hello,word");
const char * p = qstr.toLocal8Bit().data();
```
方法二:
```
const char *p = qstr.toStdString().data();
```
转换过来的是常量


## 把当前时间转化为QString
```
public QDateTime qdate = QDateTime.currentDateTime();
datetime = qdate.toString("yyyy年MM月dd日ddddhh:mm:ss");
```
如果不是QTime和QDate类比如说：通过TCP/IP接收到的char unsigned char 类等如何转换为QString类
```
QString Time2String( DWORD dwTime)
{
char cTime[50] = {0};
memset(cTime,0,50);
strftime(cTime,32,"%Y-%m-%d %H:%M:%S",localtime(&time_t(dwTime)));
return QString(cTime);
}
```

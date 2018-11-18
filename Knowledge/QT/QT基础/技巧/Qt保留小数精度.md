# Qt保留小数精度

```C++
double/float  size = 2.3334524;
QString str = QString::number(size, 'f', 2);
//其中f代表非科学计数法格式，2代表小数点后两位。
```
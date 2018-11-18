# QT QString char wchar_t的转换
## QString -> char*
```C++
QString dome0;
char dome1[20];
QByteArray dome2 = dome0.toLocal8Bit();
strcpy(dome1, dome2.data()); 
```

## QString -> wchar_t*
```C++
const wchar_t * encodedName = reinterpret_cast<const wchar_t *>(fileName.utf16());
```
## char* -> QString
直接构造即可

## wchar_t* -> QString
```C++
wchar_t temp[] = TEXT("test");
QString item = QString::fromStdWString(temp);
```

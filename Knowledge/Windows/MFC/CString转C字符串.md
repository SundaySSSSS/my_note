# CString转C字符串

```
CString temp;
temp.Format("this is a test");
char* p = temp.GetBuffer(temp.GetLength());
//使用指针p
//....
temp.ReleaseBuffer();


```

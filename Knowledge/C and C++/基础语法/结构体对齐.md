# 结构体对齐

## 指定结构体对齐的字节数
``` C++
#pragma pack(1)
...
#pragma pack()
```
或

``` C++
#pragma pack(push, 1)
...
#pragma pack(pop)
```


## 具体实例
结构体存在对齐问题:

``` C++
typedef struct _testS
{
	char a;
	double b;
}
testS;

int main(int argc, char* argv[])
{
	testS s;
	cout << sizeof(s) << endl;
	system("pause");
	return 0;
}
```
输出为16

指定对齐方式后, 

``` C++
#pragma pack(1)
typedef struct _testS
{
	char a;
	double b;
}
testS;
#pragma pack()

int main(int argc, char* argv[])
{
	testS s;
	cout << sizeof(s) << endl;
	system("pause");
	return 0;
}
```
输出为9

下面的写法相同, 也会让结构体1字节对齐, 输出也为9

``` C++
#pragma pack(push, 1)
typedef struct _testS
{
	char a;
	double b;
}
testS;
#pragma pack(pop)

int main(int argc, char* argv[])
{
	testS s;
	cout << sizeof(s) << endl;
	system("pause");
	return 0;
}
```
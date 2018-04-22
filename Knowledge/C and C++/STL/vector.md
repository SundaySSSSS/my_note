# vector的用法

## 插入
```
vector<int> v;
v.push_back(1);
```

## 遍历

```
vector<int> v;

//对vector进行操作

for (vector<int>::iterator iter = v.begin(); iter != v.end(); iter++)
{
	int a = (*iter);
}

//备注:
//如果不改变iter指向的值, 应该使用vecotr<int>::const_iterator iter
```

## 删除

```
vector<int> v;
//对vector进行操作...
vector<int>::iterator iter = v.begin();
while (iter != v.end())
{
	if (/* 删除条件 */)
	{
		iter = v.erase(iter);
	}
	else
	{
		++iter;
	}
}

```
## 复制
vector是一个构造对象, 不能直接用=赋值  
要使用如下方法之一:  
1. 初始化构造  
    ` vector<int> v1(v2)`
2. swap  
```
vector<int> v1();
v1.swap(v2);
```
3. assign
```
v1.assign(v2.begin(), v2.end());
```
4, 使用迭代器循环赋值




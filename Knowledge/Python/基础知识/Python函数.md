#Python函数
## 函数基本格式
```
def my_func(a, b, c):
    pass
```

## 函数参数
### 函数参数传递方式
python函数采用值传递
但传入list名, 字典名时, 相当于传入C语言中的数组名, 类似于地址

### 关键字参数
```
def my_func(a, b, c):
    print(a)
    print(b)
    print(c)

my_func(1, 2, 3)
my_func(b=3, a=2, c=1)
```

### 默认参数
```
def my_func2(a, b=2):
    print(a + b)

my_func2(1)
my_func2(1, 2)
```

## 函数文档

```python
def func():
    """
    this is function doc
    """
    pass
```

函数文档可以通过如下方式获取
```
func.__doc__
```
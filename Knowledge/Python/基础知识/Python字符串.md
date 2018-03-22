# Python字符串

## '和"
'和"意义相同
特殊情况:
```
"Let's go"
'"Hello" she said'
```
如上使用方法正确
但如下使用方法错误:
```
'Let's go'
```
## 转义字符\
```
'Let\' go'
```
## 字符串拼接
方法1: 字符串 字符串
例如:
```
"Let's say" '"Hello World!!!!"'
```
方法2: 字符串 + 字符串
```
"Hello " + "World"
```
## 数值转换为字符串
```
repr(10000L) 转换成的字符串为'10000L'
或者
str(10000L) 转换成的字符串为'10000'
```
区别:
str: 把值转换为合理形式的字符串
repr: 创建一个字符串, 以合法的Python表达式的形式来表示值
## 长字符串
跨行的字符串用'''包裹
例如:
```python
'''This is a very 
long string, so 
use a big buffer to
save'''

```
## 原始字符串
```
r'C:\Program Files\XXX'
```
原始字符串忽略任何转义字符, 认为内部全部是字符

# Python序列

Python内置六种序列， 分别是：
列表(List)， 元组， 字符串， Unicode字符串， buffer对象和xrange对象

## 序列通用操作
### 索引
```python
greeting = "Hello"
print(greeting[1])
```
`>>> e`
### 分片
#### 基本用法
基本格式：
`seq[a:b]`
其中， seq是待分片的序列， 
a是要取出的第一个元素，
b是要取出部分最后一个元素的后一个元素

`seq[-a:]`
序列的最后a个元素

`seq[:a]`
序列的最开始a个元素

例如：
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
numbers[3:6]
```
`>>>[3, 4, 5]`
```
numbers[-3:]
```
`>>>[6, 7, 8]`

```
numbers[:3]
```
`>>>[0, 1, 2]`

如果不指定任何上下限，则为整个序列
```
numbers[:]
```
`>>>[0, 1, 2, 3, 4, 5, 6, 7, 8]`

#### 指定步长
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
numbers[::2]
```
`>>>[0, 2, 4, 6, 8]`

### 加法运算
序列的加法运算即为序列的连接
```
seq1 = [0, 1, 2]
seq2 = [3, 4, 5]
seq2 + seq1
```
`[3, 4, 5, 0, 1, 2]`

### 乘法
序列乘法即为重复
```
seq = [0, 1, 2]
seq * 3
```
`[0, 1, 2, 0, 1, 2, 0, 1, 2]`

### 成员资格
检查某元素是否在序列中
```
seq1 = [0, 1, 2]
1 in seq1
```
`True`

```
seq2 = "abc"
'a' in seq2
```
`True`

### 长度， 最大值， 最小值
```
seq = [0, 1, 2]
len(seq) # 返回3
min(seq) # 返回0
max(seq) # 返回2
```

## List
### 创建
```Python
a = []
b = [1, 2, 3]
name = list('Python')
```
### 修改
```
b[1] = 0
```
### 删除
```
del b[1]
```
### 分片赋值
#### 覆盖
```
>>> name = list('Python')
>>> name
['P', 'y', 't', 'h', 'o', 'n']
>>> name[1:] = list('icture')
>>> name
['P', 'i', 'c', 't', 'u', 'r', 'e']
```
#### 插入
```
>>> lst = [1, 5]
>>> lst[1:1] = [2, 3, 4]
>>> lst
[1, 2, 3, 4, 5]
```
#### 删除
```
[1, 2, 3, 4, 5]
>>> lst = [1, 2, 3, 4, 5]
>>> lst[1:4] = []
>>> lst
[1, 5]
```
### List方法
#### append
功能: 在list尾部追加
```
>>> lst = [1, 2, 3]
>>> lst.append(4)
>>> lst
[1, 2, 3, 4]
```
#### count
功能: 计算某元素在list中出现的次数
```
>>> lst = ['to', 'be', 'or', 'not', 'to', 'be']
>>> lst.count('to')
2
```
#### extend
#### index
#### insert
#### pop
#### remove
#### reverse
#### sort



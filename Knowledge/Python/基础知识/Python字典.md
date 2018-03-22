# Python字典
## 创建
### 直接创建
```
>>> d = {'cxy': '001', 'lc': '002'}
>>> d
{'cxy': '001', 'lc': '002'}
```
### 使用其他映射创建字典
```
>>> temp = [('a', 1), ('b',2)]
>>> d = dict(temp)
>>> d
{'a': 1, 'b': 2}
```
### 使用键值对创建字典
```
>>> d = dict(a=1,b=2)
>>> d
{'a': 1, 'b': 2}
```

## 字典基本操作
```
len(d) 返回d中键值对的个数
d[k]返回关联到k上的值
d[k] = v将值v关联到k上
del d[k]删除键为k的项
k in d检查d中是否含有键为k的项
```
## 字典方法
```
clear
copy
fromkeys
get
has_key
items和iteritems
items让字典以list方式返回, iteritems返回字典迭代器
key和iterkeys
pop
popitem <- 随机删除一个元素, 因为字典是无序的, 没有最后元素
setdefault 设置字典无键值的情况下的默认值
update
values和itervalues

```
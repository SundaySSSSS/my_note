# Python命令行参数
Python 中可以所用 sys 的 sys.argv 来获取命令行参数：
sys.argv 是命令行参数列表。
len(sys.argv) 是命令行参数个数。

注：sys.argv[0] 表示脚本名。

实例
test.py 文件代码如下：

``` Python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

print '参数个数为:', len(sys.argv), '个参数。'
print '参数列表:', str(sys.argv)
执行以上代码，输出结果为：
```

`$ python test.py arg1 arg2 arg3`
参数个数为: 4 个参数。
参数列表: ['test.py', 'arg1', 'arg2', 'arg3']
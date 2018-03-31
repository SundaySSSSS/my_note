# python导入模块
## 同级目录导入
三种基本方法如下:
```python
import moduleA
from moduleA import *
from moduleA import something
from moduleA import something as a
```

## 加载子目录中的模块
例如在test目录下, 有moduleB.py文件, 可以使用如下方法导入
```python
import test.moduleB
```

## 上一级目录的模块
在上一次目录中, 存在moduleC.py文件, 可以使用如下方法导入
```python
import sys
sys.path.append("..")
import moduleC

```
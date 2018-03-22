# python创建删除目录

## 创建目录
主要涉及到三个函数

1、`os.path.exists(path)` 判断一个目录是否存在
2、`os.makedirs(path)` 多层创建目录
3、`os.mkdir(path)` 创建目录

```Python
import os

def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        　# 创建目录操作函数
        os.makedirs(path)

        print path+' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path+' 目录已存在'
        return False

# 定义要创建的目录
mkpath="d:\\qttc\\web\\"
# 调用函数
mkdir(mkpath)
```

## 删除目录
```
import shutil
shutil.rmtree('c:\\test')
```


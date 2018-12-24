# emacs中Python环境搭建
1, 安装如下python库
```
pip install rope
pip install jedi
# flake8 用来检查语法错误
pip install flake8
# importmagic 用来自动引入需要的包
pip install importmagic
# autopep8 用来检查PEP8规范
pip install autopep8
# yapf 用来格式化代码
pip install yapf
```

2, 安装elpy, 并启用
自行安装即可
启用elpy在配置文件中加入如下内容
```lisp
(elpy-enable)
```
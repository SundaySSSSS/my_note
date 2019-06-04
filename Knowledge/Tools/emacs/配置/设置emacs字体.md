# 设置emacs字体
1, 在图形化工具上先修改字体, 具体为: 在菜单栏上找到Option->set Default Font
在弹出窗口上选择合适的字体

2, M-x describe-font
在输出的内容中找到类似下面的文字:
``` lisp
-outline-Consolas-normal-normal-normal-mono-15-*-*-*-c-*-iso8859-15
```

3, 在配置文件中加入如下内容即可
``` lisp
(set-default-font "-outline-Consolas-normal-normal-normal-mono-15-*-*-*-c-*-iso8859-1")
```
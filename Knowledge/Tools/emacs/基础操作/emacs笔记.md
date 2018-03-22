# emacs笔记

## 基本概念
emacs的编辑模式分为主mode(major mode)和副模式(minor mode)

如何emacs显示所有minor mode
目前只知道如下方法:
在下面的一条类似状态栏的位置上点击鼠标中键(滚轮)
会显示:
```
Enabled minor modes: Auto-Composition ...
```

## emacs自己的帮助系统
C-h C-h会弹出选项, 如果是查看按键帮助, 可以再点击k
如果是变量, 就是v, 等等

## 文件, 缓冲区操作
```
C-x C-f    | find-file | 查找文件并打开
C-x C-s    | save-buffer | 保存文件
C-x C-v    | find-alternate-file | 用一个新的文件替换掉当前文件
C-x C-w    | write-file | 另存为
当文件发生变更时, emacs不提供刷新buffer的方法, 只能重新C-x C-f
```

## 缓冲区操作
```
C-x b buffer_name | switch-to-buffer |如果输入的buffer name存在, 则切换到那个缓冲区
如果输入的不存在, 则创建一个新的缓冲区并转移到那里
C-x k 关闭指定的缓冲区
C-x C-b | list-buffers | 显示缓冲区清单
```

## 光标移动
```
C-f
C-b
C-p
C-n
ESC-f
ESC-b
C-a    | beginning-of-line | 光标移动到行首
ESC-m    | 将光标移动到本行第一个非空格字符
C-e    | end-of-line | 光标移动到行尾
C-v    | 向下移动一屏
ESC-v    | 向上移动一屏
ESC-<    | 移动到文件头
ESC->    | 移动到文件尾
C-l    | recenter |重新绘制画面, 并把当前行放到画面中央
```

## 文本编辑
```
C-x u | advertised-undo | 撤销上一次的编辑
对撤销的撤销便是重做（或者向前撤销）
  ┌────
  │ 第一，执行 C-x u 向后撤销
  │ 第二，执行 C-g 然后 C-x u 就是向前撤销了。
  └────
C-d | 删除光标位置的字符
DEL | 删除光标前的字符
ESC-d | 删除光标后单词
ESC-DEL | 删除光标前的单词
C-k | 删除从光标处到行尾的所有文本
```

## 复制文本块
```
C-@ 设置文本块起点, 再移动光标, 选择文本块的区域
C-w 删除文本块
Esc-w 复制文本块
C-y 粘贴(可以粘贴系统剪贴板内的内容)
```

## Dired命令
```
键盘操作     | 命令名称 | 动作
C-x d         |     dired     |     启动Dired
在Dired模式下
n 向下移动一行
p 向上移动一行
e 编辑文件
v 浏览文件
q 退出Dired模式
> 移动到下一个目录
< 移动到上一个目录
g 从磁盘上重新读取目录内容(刷新)

d 给该文件打上待删除标记
m 给文件打上待操作标记, 后续的C或R会操作此文件
u 取消待操作标记
x 删除所有有待删除标记的文件
C 复制当前文件, 后续会询问复制路径
R 移动文件,后续会询问路径
+ 创建目录

```


## 窗口
```
键盘操作     | 命令名称 | 动作
C-x 0         | delete-window |     删除当前窗口
C-x 1         | delete-other-windows | 删除其他窗口
C-x 2         | split-window-vertically | 将窗口分成上下两个窗口
C-x 3         将窗口分成左右两个窗口

C-x o        | other-window |移动到下一个窗口

```

改变窗口大小
```
C-x ^ 窗口增高
C-x { 窗口变窄
C-x } 窗口变宽
上面命令如果前面加C-u, 则一次操作四行(列)
```

## 窗格
```
C-x 5 2 make-frame 创建一个新的窗格
```

## shell
```
键盘操作     | 命令名称 | 动作
ESC x shell    shell    进入shell模式
ESC p     上一条命令
C-c C-c    相当于普通shell中的Ctrl+C
```

## Telnet模式
```
Esc x telnet 进入telnet模式
```


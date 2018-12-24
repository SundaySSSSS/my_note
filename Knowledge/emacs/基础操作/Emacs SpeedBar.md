# Emacs SpeedBar
## 1 启动speedbar
speedbar可以用来查看当前buffer的概况信息.调用它的方法是执行命令M-x speedbar

## 2 speedbar的通用命令
命令	说明
Q	退出speedbar并杀掉frame
q	退出speedbar并隐藏frame
g	刷新
t	是否追踪绑定的frame
p/n	上/下移动,被绑定的frame的minibuffer中会显示指定项的信息
M-p /M-q	同级之间上下移动,被绑定的frame的minibuffer中会显示指定项的信息
C-M-n / C-M-p	快速跳转
C-x b	切换被绑定frame的buffer
b	临时切换speedbar到Qucik-buffer-mode
f	切换speedbar到Qucik-file-mode
r	切回speedbar到上一个模式
RET / e	打开speedbar的指定项
+ / =	展开speedbar的指定项
-	收缩speedbar的指定项
## 3 speedbar的三种mode
speedbar提供了三种显示模式:file-mode,buffer-mode和quick-buffer-mode. 可以通过鼠标右键弹出的菜单里选择"Displays->Files","Displays->Quick Buffers","Displays->Buffers"来切换不同的显示模式

### 3.1 File-mode
#### 3.1.1 文件标识说明
在文件的后面有时会有一些字母表示的标识，这些标识表示了文件的一些附加信息
```
* 星号表示该文件有版本控制功能
# 井号表示该源文件有最新的对应目标文件存在
! 感叹号标识该源文件有过时的对应目标文件存在
```
#### 3.1.2 如何显示隐藏文件？
默认情况下speedbar不显示隐藏文件，要显示隐藏文件需要点击鼠标右键，在弹出的菜单中选择“Show-all-files”

#### 3.1.3 操作
命令	说明
U	跳转到上一级目录
I	在被绑定的frame的minibuffer中显示当前文件的信息
B	编译当前的Emacs Lisp文件
L	加载当前的Emacs Lisp文件
C	拷贝当前文件
R	重命名当前文件
D	删除当前文件
O	删除当前文件的目标文件（object file）
### 3.2 buffer-mode
命令	说明
k	kill当前buffer
r	revert当前buffer
### 3.3 qucik-buffer-mode
quick-buffer-mode跟buffer-mode类似,所不同之处在于在quick-buffer-mode下,对指定的buffer操作之后,speedbar会立刻返回前一个mode,所以可以将之理解为临时的buffer-mode

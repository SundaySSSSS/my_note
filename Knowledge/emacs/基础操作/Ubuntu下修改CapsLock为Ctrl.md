# Ubuntu下修改CapsLock为Ctrl

由于最近使用AS编程的时候安装了Vim插件，慢慢开始学习使用。但是频繁的Esc及Control操作给左手小指带来很大的负担，所以参考网上的方案将Caps_Lock键替换为Control左键，将～（Esc键下面的键）键替换为Esc键。以下为方法：
在home下新建.Xmodmap文件，将以下代码保存上。

```
!
! swap Caps_Lock <---> Control_L
!
remove Lock = Caps_Lock
remove Control = Control_L
keysym Control_L = Caps_Lock
keysym Caps_Lock = Control_L
add Lock = Caps_Lock
add Control = Control_L

!
! swap Esc <---> `(on the left of '1' key)
!
keysym Escape = grave asciitilde grave asciitilde
keysym grave = Escape
```
之后在Terminal中执行xmodmap .Xmodmap就可以了。
另外，可以使用xev命令来获取各个按键的keycode，如图：

使配置永久有效
执行gnome-session-properties命令，打开启动项管理工具，添加如下命令：

```
xmodmap -e "remove Lock = Caps_Lock"; xmodmap -e "remove Control = Control_L"; xmodmap -e "keysym Control_L = Caps_Lock"; xmodmap -e "keysym Caps_Lock = Control_L"; xmodmap -e "add Lock = Caps_Lock"; xmodmap -e "add Control = Control_L"
```

# 打开两个shell

每次使用ESC-x shell, 都会打开同一个shell
可以通过重命名*shell*的buffer来实现打开多个shell

在已经打开的第一个shell的buffer下,
`M-x rename-buffer`
再输入一个不同于shell的名字, 例如`shell-debug`

此时, 再用`M-x shell`打开的就是一个新的shell了


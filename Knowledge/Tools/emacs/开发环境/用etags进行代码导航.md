# 用etags进行代码导航

1, 生成TAGS文件
在工程根目录执行如下命令
`find . -name '*.[ch]' | xargs etags -a`
如果浏览cpp工程, 可以考虑如下
`find . -name "*.c" -o -name "*.cpp" -o -name "*.h" | xargs etags -a`

2, 加载TAGS文件
`M-x visit-tags-table`

3, 查找一个tag, 比如函数定义或类型定义等
`M-.`
查找下一个tag的位置
`C-u M-.`

回到上一次执行`M-.`前的光标位置
`M-*`

4, 让emacs默认加载特定的TAGS文件



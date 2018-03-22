# GDB异常解决方法

## cannot find new threads: generic error

如果启动gdb, r
出现cannot find new threads: generic error
则说明没有链接pthread库
在生成时加上-lpthread即可

备注:
如果proc1里面没有用到pthread相关内容, 仍然出现此错误, 
可能是proc1加载了其他用到pthread的动态库或静态库
也需要在proc1生成时加上-lphread才能使用gdb调试



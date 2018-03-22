# gcc选项

## -E 完成预处理后停止
例如: gcc -E hello_world.c > hello_world.i

## -S 得到汇编代码
例如: gcc -S hello_world.c -o hello_world.s

共享库相关参考Linux/Linux编程/Linux共享库.md

-l链接库的名字
例如: gcc test.c -o test -lpthread

## -L 链接库的路径
`-Wl,-rpath,`
如果使用了非系统的链接库, 需要使用-L指定链接库所在的路径
如:
nanomsg库所在的路径为/work/share/bus_test
编译命令为
`gcc -o bus_test bus_test.c -L/work/share/bus_test -Wl,-rpath,/work/share/bus_test -lnanomsg`

备注, 如果不加-Wl,-rpath,则会在运行时报错, 找不到动态库

## -D 宏定义
### 单纯定义宏
`gcc -DLINUX ...`
相当于代码中`#define LINUX`
### 定义有值的宏
`gcc -DTYPE=2`
相当于代码中`#define TYPE 2`
### 定义字符串
定义字符串需要用\来转义"
`gcc -DVERSION=\"1.0.4\" ...`
相当于代码中`#define VERSION "1.0.4"`



# Linux共享库

## 创建共享库的基本方法
```
gcc -g -c -fPIC -Wall mod1.c mod2.c mod3.c
gcc -g -shared -o libfoo.so mod1.o mod2.o mod3.o
```
## 共享库的名称
### 共享库的三个名称
* 真实名称
真实名称即共享库文件的文件名

* soname
一个共享库通常有soname, soname提供了一个间接层
指定soname的方法
```
gcc -g -c -fPIC -Wall mod1.c mod2.c mod3.c
gcc -g -shared -Wl,-soname,libucmsg.so -o libfoo.so mod1.o mod2.o mod3.o
```

* 链接器名称
一个符号链接, 通常指向soname
在和程序链接时, 通常使用此名称

### 三个名称之间的关系
例如要创建一个名为ucmsg的共享库
则: 
真实名称: `lib共享库名.so.主版本号.次版本号`, 例如`libucmsg.so.1.0.2`
soname: `lib共享库名.so.主版本号`, 例如`libucmsg.so.1`
链接器名称: `lib共享库名.so`, 例如`libucmsg.so`

## 创建共享库的标准流程
```
# 第一步, 创建目标文件
gcc -g -c -fPIC -Wall mod1.c mod2.c mod3.c
# 第二步, 创建共享库并制定soname
gcc -g -shared -Wl,-soname,libucmsg.so.1 -o libucmsg.so.1.0.2 mod1.o mod2.o mod3.o
# 第三步, 为soname和链接器名称创建符号链接
ln -s libucmsg.so.1.0.2 libucmsg.so.1
ln -s libucmsg.so.1 libucmsg.so
```

最后生成的三个文件为:
```
libucmsg.so(链接器名称) --> libucmsg.so.1(soname) --> libucmsg.so.1.0.2(真实的动态库文件)
```

## 共享库的版本管理
共享库通常有 主版本号(major version) 和 次版本号(minor version)
主版本号变更意味着发生了不兼容更新(修改了原有的接口)
如果接口没变或追加了部分接口, 则变更次版本号

## 创建共享库标准流程的makefile示例
```
#目录定义
SRC_DIR = src

#平台定义
PLATFORM=x86
#PLATFORM=8127
#PLATFORM=6467_2009q1

#变量初始化
CC=g++
BIN_PATH=bin/x86

ifeq ($(PLATFORM), 8127)
	CC:=/work/share/NVC200E/ti_tools/linux_devkit/bin/arm-arago-linux-gnueabi-g++
	BIN_PATH=bin/8127
else ifeq ($(PLATFORM), 6467)
	CC:=/work/share/6467_ti_tools/arm/v5t_le/bin/arm_v5t_le-g++
	BIN_PATH=bin/6467
else ifeq ($(PLATFORM), 6467_2009q1)
	CC:=/work/share/6467_2009q1_ti_tools/arm-2009q1/bin/arm-none-linux-gnueabi-g++
	BIN_PATH=bin/6467_2009q1
else ifeq ($(PLATFORM), x86)
	CC:=g++
	BIN_PATH=bin/x86
else
	CC:=g++
	BIN_PATH=bin/x86
endif

CORE_NAME = ucmsg
SO_REAL_NAME = lib$(CORE_NAME).so.1.0.1
SO_NAME = lib$(CORE_NAME).so.1
SO_LINK_NAME = lib$(CORE_NAME).so

OBJS += src/UcMsg.o 
OBJS += src/cjson/cjson.o

CFLAGS = -g

so: clean $(SO_REAL_NAME)

$(SO_REAL_NAME) : $(OBJS)
	$(CC) $(CFLAGS) -fPIC -shared -Wl,-soname,$(SO_NAME) -o $(SO_REAL_NAME) $(OBJS) 
	#删除临时文件
	rm -f *.o
	rm -f */*.o
	rm -f */*/*.o
	#生成链接器名称和soname
	ln -s $(SO_REAL_NAME) $(SO_NAME)
	ln -s $(SO_NAME) $(SO_LINK_NAME)
	#移动到最终目录
	mv -f $(SO_REAL_NAME) $(BIN_PATH)
	mv -f $(SO_NAME) $(BIN_PATH)
	mv -f $(SO_LINK_NAME) $(BIN_PATH)
	#生成共享库完毕

test: src/test.o
	$(CC) $(CFLAGS) src/test.o -L./$(BIN_PATH) -l$(CORE_NAME) -Wl,-rpath,./$(BIN_PATH) -o test

%.o:%.cpp	
	$(CC) $(CFLAGS) -c  -o $@  $<
%.o:%.c
	$(CC) $(CFLAGS) -c  -o $@  $<

clean:
	rm -f $(BIN_PATH)/$(SO_REAL_NAME)
	rm -f $(BIN_PATH)/$(SO_NAME)
	rm -f $(BIN_PATH)/$(SO_LINK_NAME)
	rm -f *.o
	rm -f */*.o
	rm -f */*/*.o
```

## 编译选项的意义
### -fPIC
生成位置独立的代码, 可以使共享库能够在进程间共享

### -L -l
如果要链接的库为libucmsg.so, 并且没有在系统目录中
可以使用-L指定libucmsg.so所在的目录
-l指定要链接的库, 这里应该用: `-lucmsg`
例子:
假设`libucmsg.so`在`./lib`目录下
```
g++ test.o -L./lib -lucmsg -o test
```

### -Wl,-rpath,
指定运行时搜索动态库的地址
例子:
假设`libucmsg.so`在`./lib`目录下
```
g++ test.o -L./lib -lucmsg -Wl,-rpath,./lib -o test 
```
这样, 运行时就会在`./lib`中搜索动态库了

### -Wall

### --Xlinker --unresolved-symbols=ignore-in-shared-libs
如果出现未知符号, 如果在动态库中, 忽略
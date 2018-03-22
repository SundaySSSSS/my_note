# makefile

## 赋值
```
=最基本的赋值
=:覆盖之前的值
?=如果没有被赋值过则赋予=后的值
+=添加等号后面的值
```

## 打印
@echo $(变量名)

## 条件语句

```
ifeq($(TARGET_ARCH), arm)
    CC=arm_gcc
else ifeq($(TARGET_ARCH), 8127)
    CC=8127_gcc
else
    CC=gcc
```

## 自定义函数
```
#定义函数
define my_func
	@echo $(1)
	@echo $(2)
endef

#调用函数
$(call my_func, 123, abc)
```

## 宏定义
第一种 -D DEFINES
第二种 -D DEFINES=CONDITION

例如:
-DTEST_ADD 相当于在代码中`#define TEST_ADD`
-DTEST_SUB=1 相当于在代码中`#define TEST_SUB 1`

```
DEFS = -DTEST_ADD -DTEST_SUB=1
CC = gcc
$(CC) $(DEFS) -o $@ -c $<
```
## 多makefile的写法

可参考DataSync的代码实现
目录结构:
```
src_dll
	源代码文件…
	Makefile ----------[1]
src_center_demo
	源代码文件…
	Makefile ----------[2]
src_node_demo
	源代码文件…
	Makefile ----------[3]
Makefile ----------[0]
```
在Makefile[0]中, 使用@cd进入下层目录, 在调用对应makefile中的命令
Makefile[0]节选
```
SRC_CENTER_DEMO_DIR = src_center_demo
SRC_NODE_DEMO_DIR = src_node_demo
SRC_DLL_DIR = src_dll
#############################################
#dll
#############################################
dll:
	@cd $(SRC_DLL_DIR)/ ; $(MAKE) all
dll_clean:
	@cd $(SRC_DLL_DIR)/ ; $(MAKE) clean
dll_test:
	@cd $(SRC_DLL_DIR)/ ; $(MAKE) test
dll_run:
	@cd $(SRC_DLL_DIR)/ ; $(MAKE) run

在Makefile[1]中, 代码节选:
all: clean $(DLL)

$(DLL) : $(OBJS)
	$(CC) $(CFLAGS) -shared -o $(DLL) $(OBJS) -L./ -Wl,-rpath,./ -lnanomsg -lpthread -ldl -Xlinker --unresolved-symbols=ignore-in-shared-libs

$(TEST) : $(OBJS) main.o
	$(CC) $(CFLAGS) -o $(TEST) $(OBJS) main.o -L./ -Wl,-rpath,./ -lnanomsg -lpthread -ldl

run : 
	@cd ../bin ; ./$(TEST)

%.o:%.cpp
	$(CC) $(CFLAGS) -c  -o $@  $<
%.o:%.c
	$(CC) $(CFLAGS) -c  -o $@  $<
```
效果:
在最外层目录, 使用命令
`make dll_run`
则会进入到src_dll下, 再执行run命令

## 多makefile变量传递

在根makefile中定义变量
例如:
`CC=g++`
然后添加
`export CC`

则在通过@cd进入的其他的makefile中就可以直接使用CC变量了



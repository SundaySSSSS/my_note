# makefile宏定义[转]

## 1.gcc复习
宏定义使用前缀-D，在编译过程中可以把宏定义追加到CFLAG中。宏定义有两种相似的写法
第一种   `-D DEFINES`
第二种   `-D DEFINES=CONDITION`
 
## 2.源文件
使用两种不同的方式，通过宏定义包裹打印功能，分别使用#ifdef和#if

```
#include <stdio.h>  
#include <test-add.h>  
#include <test-sub.h>  
int main(void)  
{  
    int a = 3;  
    int b = 2;  

    printf("a=%d\n", a);  
    printf("b=%d\n", b);  
#ifdef TEST_ADD  
    printf("a+b=%d\n", add(a,b));  
#endif  
#if TEST_SUB  
    printf("a-b=%d\n", sub(a,b));  
#endif  
    return 0;  
}
```
## 3.makefile
请替换其中的[tab]，并以代码仓库中的makefile文件为主。

```
# 指令编译器和选项  
CC=gcc  
CFLAGS=-Wall -std=gnu99  
# 宏定义  
DEFS = -DTEST_ADD -DTEST_SUB=1  
CFLAGS += $(DEFS)  
# 目标文件  
      
TARGET=test  
 # 源文件  
 SRCS = test.c \  
   ./test-add/test-add.c \  
   ./test-sub/test-sub.c  
 # 头文件查找路径  
 INC = -I./test-add -I./test-sub  
 # 目标文件  
 OBJS = $(SRCS:.c=.o)  
 # 链接为可执行文件  
 $(TARGET):$(OBJS)  
 #   @echo TARGET:$@  
 #   @echo OBJECTS:$^  
 [tab]$(CC) -o $@ $^  
 clean:  
 [tab]rm -rf $(TARGET) $(OBJS)  
 # 连续动作，请清除再编译链接，最后执行  
 exec:clean $(TARGET)  
 [tab]@echo 开始执行  
 [tab]./$(TARGET)  
 [tab]@echo 执行结束  
 # 编译规则 $@代表目标文件 $< 代表第一个依赖文件  
 %.o:%.c  

[tab]$(CC) $(CFLAGS) $(INC) -o $@ -c $<
```
## 4.具体说明
【1】 makefile定义头文件的方法有两种
【第一种】-D DEFINES 
【第二种】-D DEFINES=CONDITION

【2】DEFS = -DTEST_ADD -DTEST_SUB=1 
为了说明问题，此处使用了两种不同的写法。此时两处打印功能均被执行
【3】CFLAGS += $(DEFS) 
追加到CFLAGS中，此处需要强调CFLAGS只是一个变量，可以命名为任何合法的名称，只要在编译过程中引用该参数即可。
`    $(CC) $(CFLAGS) $(INC) -o $@ -c $<`
 
## 5.执行过程
【编译和链接】
`make clean && make`
【控制台输出】
```
rm -rf test test.o ./test-add/test-add.o ./test-sub/test-sub.o
gcc -Wall -std=gnu99 -DTEST_ADD -DTEST_SUB=1 -I./test-add -I./test-sub -o test.o -c test.c
gcc -Wall -std=gnu99 -DTEST_ADD -DTEST_SUB=1 -I./test-add -I./test-sub -o test-add/test-add.o -c test-add/test-add.c
gcc -Wall -std=gnu99 -DTEST_ADD -DTEST_SUB=1 -I./test-add -I./test-sub -o test-sub/test-sub.o -c test-sub/test-sub.c
gcc -o test test.o test-add/test-add.o test-sub/test-sub.o
```
从控制台的输出可以看出，在编译过程中加入了-D参数。
【执行】
```
a=3
b=2
a+b=5
a-b=1
```
最终效果和预期完全相同，makefile得到的验证。
 
## 6.总结
【1】增加宏定义的两个方法 -D DEFINES  和 -D DEFINES=CONDITION

【2】宏定义追加到CFLAG之后
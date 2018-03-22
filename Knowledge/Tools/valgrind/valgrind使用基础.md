# valgrind使用基础

## 最常用字符串
```
valgrind --tool=memcheck --leak-check=yes --show-reachable=yes ./test
```

## valgrind是什么
Valgrind是一款用于内存调试、内存泄漏检测以及性能分析的软件开发工具。
Valgrind的最初作者是Julian Seward，他于2006年由于在开发Valgrind上的工作获得了第二届Google-O'Reilly开源代码奖。
Valgrind遵守GNU通用公共许可证条款，是一款自由软件

## valgrind的安装

去官网下载`valgrind-3.8.1.tar.bz2`
依次执行
```
tar xvf valgrind-3.8.1.tar.bz2
cd valgrind-3.8.1
./configure
make
make install
```

## valgrind的简单使用
测试代码如下
```
#include <stdlib.h>  
int* func(void)  
{  
   int* x = malloc(10 * sizeof(int));  
   x[10] = 0;  //问题1: 数组下标越界  
}
int main(void)  
{  
    int* x=NULL;  
    x=func();  
    //free(x);    
    x=NULL;  
    return 0;   //问题2: 内存没有释放  
}
```

编译
`gcc -g -o test test.c`
内存检查
`valgrind --tool=memcheck --leak-check=yes --show-reachable=yes ./test`
报告结果为
```
==11271== Memcheck, a memory error detector
==11271== Copyright (C) 2002-2012, and GNU GPL'd, by Julian Seward et al.
==11271== Using Valgrind-3.8.1 and LibVEX; rerun with -h for copyright info
==11271== Command: ./test
==11271== 
==11271== Invalid write of size 4
==11271==    at 0x80484DF: func() (test.c:5)
==11271==    by 0x80484FC: main (test.c:10)
==11271==  Address 0x42d2050 is 0 bytes after a block of size 40 alloc'd
==11271==    at 0x40265DC: malloc (vg_replace_malloc.c:270)
==11271==    by 0x80484D5: func() (test.c:4)
==11271==    by 0x80484FC: main (test.c:10)
==11271== 
==11271== 
==11271== HEAP SUMMARY:
==11271==     in use at exit: 40 bytes in 1 blocks
==11271==   total heap usage: 1 allocs, 0 frees, 40 bytes allocated
==11271== 
==11271== 40 bytes in 1 blocks are definitely lost in loss record 1 of 1
==11271==    at 0x40265DC: malloc (vg_replace_malloc.c:270)
==11271==    by 0x80484D5: func() (test.c:4)
==11271==    by 0x80484FC: main (test.c:10)
==11271== 
==11271== LEAK SUMMARY:
==11271==    definitely lost: 40 bytes in 1 blocks
==11271==    indirectly lost: 0 bytes in 0 blocks
==11271==      possibly lost: 0 bytes in 0 blocks
==11271==    still reachable: 0 bytes in 0 blocks
==11271==         suppressed: 0 bytes in 0 blocks
==11271== 
==11271== For counts of detected and suppressed errors, rerun with: -v
==11271== ERROR SUMMARY: 2 errors from 2 contexts (suppressed: 17 from 6)
```
报告指出了问题所在, 修改后, 再次测试, 报告如下
```
==11291== Memcheck, a memory error detector
==11291== Copyright (C) 2002-2012, and GNU GPL'd, by Julian Seward et al.
==11291== Using Valgrind-3.8.1 and LibVEX; rerun with -h for copyright info
==11291== Command: ./test_right
==11291== 
==11291== 
==11291== HEAP SUMMARY:
==11291==     in use at exit: 0 bytes in 0 blocks
==11291==   total heap usage: 1 allocs, 1 frees, 40 bytes allocated
==11291== 
==11291== All heap blocks were freed -- no leaks are possible
==11291== 
==11291== For counts of detected and suppressed errors, rerun with: -v
==11291== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 11 from 6)
```

## valgrind可检查的错误
Valgrind 中包含的 Memcheck 工具可以检查以下的程序错误：

　　使用未初始化的内存 (Use of uninitialised memory)
　　使用已经释放了的内存 (Reading/writing memory after it has been free’d)
　　使用超过malloc分配的内存空间(Reading/writing off the end of malloc’d blocks)
　　对堆栈的非法访问 (Reading/writing inappropriate areas on the stack)
　　申请的空间是否有释放 (Memory leaks – where pointers to malloc’d blocks are lost forever)
　　malloc/free/new/delete申请和释放内存的匹配(Mismatched use of malloc/new/new [] vs free/delete/delete [])
　　src和dst的重叠(Overlapping src and dst pointers in memcpy() and related functions)
　　重复free


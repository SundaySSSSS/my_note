# Linux驱动开发环境配置
一个基本的Linux设备驱动开发环境由宿主机和目标机组成，宿主机就是用来做驱动开发工作的主机，目标机就是用来运行和测试设备驱动的主机，在宿 主机上需要有开发工具（gcc，gdb，make等）和linux源码（版本要对应目标机上的linux内核），而目标机上只要运行linux即可。由于 步骤有所不同，下面分为普通Linux设备驱动开发和嵌入式Linux设别驱动开发两种情况来讲述环境的搭建和驱动程序的编译：

## （一）普通Linux设备驱动开发

普通Linux主要是区分于嵌入式Linux（一般指uClinux），在这种开发中宿主机和目标机可以是一台主机，即在本机上开发编译然后在本机 上加载运行（Linux设备驱动也可以直接编译进内核，但为了开发工作方便，一般采用动态加载的方式），当然也可以是两台主机，如果是两台主机的话，要保 证宿主机上的linux源码的版本号与目标机中的linux内核版本一致。普通Linux设备驱动开发的步骤如下：

在宿主机上安装开发工具和下载linux源码（要求版本号和目标机上的linux内核版本一致）。开发工具主要有gcc、gdb、make等，这些工具在redhat或fc中默认就安装了，在debian或Ubuntu中可以通过下面这个命令安装：
`apt-get install build-essential`
linux源码可以通过以下几种途径获得：
直接去www.kernel.org下载
通过包管理工具下载源码，在debian和Ubuntu中可以通过下面这个命令下载，
`apt-get install linux-source-(版本号) `，下载后的文件在/usr/src目录中，解压到该目录即可
将源码解压到/usr/src/目录后，进入linux-source-(版本号)目录中执行下面几个命令：
```
make oldconfig
make prepare
make scripts
```

编写Linux驱动程序，以一个最简单的hello.c为例，hello.c的内容如下：

``` C
#include "linux/init.h"
#include "linux/module.h"

static int hello_init(void)
{
    printk(KERN_ALERT "Hello World linux_driver_module\n");
    return 0;
}

static void hello_exit(void)
{
    printk(KERN_ALERT "Goodbey linux_driver_module\n");
}

module_init(hello_init);
module_exit(hello_exit);
MODULE_LICENSE("GPL");
MODULE_AUTHOR("lpj");
```
写Makefile文件，一个示例如下，里面各项参数根据实际情况更改：

``` makefile
#sample driver module
obj-m := hello.o
KDIR = /usr/src/linux-source-2.6.24/

all:
     $(MAKE) -C $(KDIR) M=$(PWD)

.PHONY:clean
clean:
     rm -f *.mod.c *.mod.o *.ko *.o *.tmp_versions
```
编译，在hello.c和Makefile所在目录下执行 make 即可，编译后在当前目录生成hello.ko文件
加载并测试：加载使用insmod或modprobe命令来实现，如在当前路径执行如下代码：
insmod hello.ko 或 modprobe hello
注意，如果在虚拟终端加载内核的话，将看不到内核打印信息，因为内核打印信息不会输出到虚拟终端，而是输出到/proc/kmsg文件中，所以可以通过以下方式查看内核信息：
cat /proc/kmsg 会一直打印，需要Ctrl－C手动终止
dmesg 或 dmesg | tail -N ，N为一数字，表示显示最后N行
卸载：使用rmmod命令卸载驱动模块，如 rmmod hello
## （二）嵌入式Ｌinux设备驱动开发

这种开发中一般目标机为带有嵌入式处理器的开发板，而宿主机为PC，开发环境需要在宿主机上搭建，嵌入式Linux设备驱动开发的步骤如下：

在宿主机上下载嵌入式Linux的源码,并安装嵌入式Linux开发工具（针对于不同的嵌入式处理器，工具也有所不同，如对应于Arm的arm-gcc系列，针对nios2处理器的nios2-cc系列）
编写Linux设备驱动驱动程序，还以上面给出的hello.c为例，将该文件复制到(linux 源码目录)/drivers/(目标文件夹)／中
在(目标文件夹)中创建Makefile和Kconfig(菜单配置文件)，内容分别如下：

``` makefile
#makefile
obj-$(CONFIG_HELLODRV) += hello.o

#Kconfig
menu  USER_DEVICE_DRIVERS
config HELLODRV
 tristate "Hello"
 ---help---
   This is a sample driver programme.
endmenu
```
注意，如果Kconfig文件中的"tristate"写成"bool"，则该模块只能选为Y（编译进内核）或N（不选择），不能选为M（编译为模块，可动态加载）

修改上层目录（ linux内核源码目录/drivers/）中的Makefile和Kconfig文件，Makefile中加入如下语句：

#makefile
obj-y += (目标文件夹)

(此处有多种写法，这只是其中一种)
Kconfig中加入如下语句：

#Kconfig
source "drivers/(目标文件夹)/Kconfig"
编译内核：几个基本的命令及选择界面如下：
make menuconfig 执行到这一步后，会看到下面这个界面：
      
其中Vendor/Product...是选择处理器厂家和型号的，Kernel/Library...是配置应用程序的，按空格键或回车键可以进入选项进行配置，用上下键移动到Kernel/Library...菜单上，按空格或回车进入下面的内核配置界面：
   


在该界面有两个Customize...选项，第一个是选择自定义配置内核，第二个是选择自定义配置应用程序，按空格键可以选择这些选项，选择后按 exit键退出，选择是否保存的时候选择“yes“，如果选择了第一个Customize...，则退出后会自动进入内核配置界面，如下图：
 


该界面有很多选项，这里不细讲，我们要配置驱动模块，就用上下键移动到Device Drivers上，然后按回车或空格键进入，设备驱动配置界面如下图：
 


这里就是linux-2.X/drivers/Kconfig里的内容了，下面那个绿色的V(+)表示这一页没显示完，可以用下键继续往下浏览，找到我们自己的菜单名，然后按回车或空格进入，我的模块配置界面如下：
 


用M键使选项前的尖括号里显示M表示该模块要动态加载，也可以按y键选择直接编辑进内核，选择完后exit退出，选择yes或no的对话框通一选yes。
make romfs #第一次编译内核前一定要有该步骤
make

加载测试：将生成的zImage文件下载到开发板，开发板上的嵌入式Linux启动后可以用insmod或modprobe加载驱动模块，测试完毕后可以通过rmmod命令卸载驱动模块

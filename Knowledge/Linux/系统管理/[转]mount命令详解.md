# [转]mount命令详解

```

一、简单用法
$ mount /dev/hda2 /home
第一个叁数是与包括文件系统的磁盘或分区相关的设备文件。
第二个叁数是要mount到的目录。
$ umount /dev/hda2
$ umount /usr
参数可以是设备文件或安装点。
 
二、mount详细介绍

如果想在运行的Linux下访问其它文件系统中的资源的话，就要用mount命令来实现。

 1.    mount的基本用法是？
格式：mount [-参数] [设备名称] [挂载点]
其中常用的参数有：
-a 安装在/etc/fstab文件中类出的所有文件系统。
-f 伪装mount，作出检查设备和目录的样子，但并不真正挂载文件系统。
-n 不把安装记录在/etc/mtab文件中。
-r 讲文件系统安装为只读。
-v 详细显示安装信息。
-w 将文件系统安装为可写，为命令默认情况。
-t 指定设备的文件系统类型，常见的有：
ext2  linux目前常用的文件系统
msdos   MS-DOS的fat，就是fat16
vfat   windows98常用的fat32
nfs   网络文件系统
iso9660   CD-ROM光盘标准文件系统
ntfs   windows NT/2000/XP的文件系统
auto 自动检测文件系统
-o 指定挂载文件系统时的选项，有些也可写到在/etc/fstab中。常用的有：
defaults 使用所有选项的默认值（auto、nouser、rw、suid）
auto/noauto 允许/不允许以 –a选项进行安装
dev/nodev 对/不对文件系统上的特殊设备进行解释
exec/noexec 允许/不允许执行二进制代码
suid/nosuid 确认/不确认suid和sgid位
user /nouser 允许/不允许一般用户挂载
codepage=XXX 代码页
iocharset=XXX 字符集
ro 以只读方式挂载
rw 以读写方式挂载
remount 重新安装已经安装了的文件系统
loop 挂载回旋设备
需要注意的是，挂载点必须是一个已经存在的目录，这个目录可以不为空，但挂载后这个目录下以前的内容将不可用，umount以后会恢复正常。使用多个-o参数的时候，-o只用一次，参数之间用半角逗号隔开：
CODE:
# mount –o remount,rw /
例如要挂载windows下文件系统为FAT32的D盘，一般而言在Linux下这个分区对应/dev/hda5，根据具体的分区情况会有不同，这里就以hda5来举例说明：
CODE:
# mkdir /mnt/hda5   //创建hda5的目录作为挂载点，位置和目录名可自定义//
# mount -t vfat /dev/hda5 /mnt/hda5
一般而言，Linux会自动探测分区的文件系统，除非让你指定时，否则-t vfat 可以省掉。
CODE:
# mount /dev/hda5 /mnt/hda5
这样就可以进入/mnt/hda5目录去访问分区中的资源了。
 
2.    为什么mount上分区后显示不了中文文件为问号/乱码？
显 示问号表明你的系统中没有可识别使用的中文字体，请先安装中文字体。确保你的系统已经可以很好的显示中文。显示为乱码一般是mount默认使用的文件系统 编码和文件系统中文件的实际编码不一致造成的。要想正常显示中文文件，mount时需要用到 -o 参数里的codepage和iocharset选项。codepage指定文件系统的代码页，简体中文中文代码是936；iocharset指定字符集，简体中文一般用cp936或gb2312。
CODE:
# mount –o iocharset=gb2312 codepage=936 /dev/hda5 /mnt/hda5
一般来说 mount –o iocharset=cp936 /dev/hda5 /mnt/hda5 就可以解决问题了。
如果这样做了以后还有问题，请尝试UTF-8编码：
CODE:
# mount –o iocharset=utf8 /dev/hda5 /mnt/hda5
 
3.    为什么mount上去以后分区普通用户不可写？
mount时加上 –oumask=000 即可：
CODE:
# mount –o umask=000, iocharset=cp936 /dev/hda5 /mnt/hda5
 
4.    为什么mount上去后的分区中的文件都变成短文件名了？
这是文件系统挂错的原因，将FAT32挂载成FAT16时就会出现这种情况，先umount，然后用–t vfat 重新挂载即可解决问题。
CODE:
# mount –t vat /dev/hda5 /mnt/hda5
 
5.    为什么不能mount ntfs分区？
这是内核不支持NTFS文件系统的原因，请重新编译内核或者安装内核的NTFS文件系统支持包，以使得内核有NTFS文件系统的支持。
 
6.    如何挂载U盘和mp3？
如果计算机没有其它SCSI设备和usb外设的情况下，插入的U盘的设备路径是 /dev/sda1，用命令：
CODE:
# mkdir /mnt/u
# mount /dev/sda1 /mnt/u
挂载即可。
7.    可以直接使用iso文件吗？
可以，就是mount的这一选项使得Linux下有免费虚拟光驱的说法，具体用法是：
CODE:
# mkdir /mnt/iso
# mount –o loop linux.iso /mnt/iso
当然，挂载以后挂载点/mnt/iso也是只读的。 
 
8.    我怎么不可以mount iso文件？
一般而言，大多数的发行版使用的内核均已将loop设备的支持编译进去了，但是也有没有的情况，所以请确保系统所使用的内核支持loop设备。
第二种情况是iso文件被放置到了NTFS或其它只读文件系统中了。挂载loop 设备必须要求挂载到一个可写的分区中，目前Linux内核对NTFS文件系统的写支持非常有限，请将iso文件复制到其它可写文件系统中后再挂载。
 
9.  如何挂载光驱和软驱
一般来说CDROM的设备文件是/dev/hdc，软驱的设备名是/dev/fd0
CODE:
# mkdir /mnt/cdrom
# mount /dev/hdc /mnt/cdrom //挂载光驱 //
# mkdir /mnt/floppy 
# mount /dev/fd0 /mnt/floppy //挂载软驱 //
 
10.   为何挂载的CD-ROM不能显示中文文件？
使用 –o iocharset=cp936 选项一般能解决问题，否则使用utf-8编码。
CODE:
# mount –o iocharset=cp936 /dev/hdc /mnt/cdrom
 
11.   如何开机自动挂载分区？
每次挂载都要输入那么长的命令的确是繁琐了些，只要将分区信息写到/etc/fstab文件中即可实现系统启动的自动挂载，例如对于/dev/hda5的自动挂载添加如下的行即可：
CODE:
/dev/hda5 /mnt/hda5 vfat defaults,iocharset=cp936, rw 0 0
 
12.   如何挂载samba 分区？
CODE:
# mkdir /mnt/share
# mount -t smbfs -ousername=root,password=abc,codepage=936,iocharset=gb2312//192.168.1.100/share   /mnt/share
如果中文显示不正常请尝试UTF-8编码。当然可以写到fstab中实现自动挂载。
 
13.   mount--bind是什么意思？
mount --bind 是将一个目录中的内容挂载到另一个目录上，用法是
CODE:
# mount --bind olddir newdir
这个命令使得自己搭建的FTP要共享某个目录的时候变得特别方便。如果要取消mount用命令：
CODE:
# mount --move olddir newdir 即可。
如果mount --bind 也想写入fstab中的话格式如下：
CODE:
olddir newdir none bind 0 0
 
三、 umount基本用法
 
譬如 /dev/hda5 已经挂载在/mnt/hda5上,用一下三条命令均可卸载挂载的文件系统
CODE:
# umount /dev/hda5
# umount /mnt/hda5
# umount /dev/hda5 /mnt/hda5
16.   为什么umount的时候老显示 device busy？
这是因为有程序正在访问这个设备，最简单的办法就是让访问该设备的程序退出以后再umount。可能有时候用户搞不清除究竟是什么程序在访问设备，如果用户不急着umount，则可以用:
CODE:
# umount -l /mnt/hda5
来卸载设备。选项 –l 并不是马上umount，而是在该目录空闲后再umount。还可以先用命令ps aux 来查看占用设备的程序PID，然后用命令kill来杀死占用设备的进程，这样就umount的非常放心了。



```

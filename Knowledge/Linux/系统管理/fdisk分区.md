# fdisk分区

```

将SD卡分为两个ext2的分区:

加入SD卡插入系统后, /dev下的设备文件为:/dev/sdc

输入命令:
dd if=/dev/zero of=/dev/sdc bs=1024 count=1024
(相当于格式化一次)

使用fdisk进行分区:
先fdisk -l查看一下所有设备文件
找到要进行处理的设备, 这里是/dev/sdc

fdisk /dev/sdc
输入p打印当前分区情况
d删除某个分区
n新建某个分区
w进行写入

完成分区后,/dev/下会出现两个新的设备文件, 通常为: sdcp0和sdcp1, 再使用ext2进行格式化
mkfs.ext2 /dev/sdcp0
mkfs.ext2 /dev/sdcp1

SD卡制作完毕


```

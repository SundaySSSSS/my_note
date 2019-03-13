# 恢复Win32DiskImager的U盘
在使用Win32 Disk Imager制作启动盘后，重新插入U盘，电脑就会自动提示在使用该U盘的时候需要将其格式化。现在开始使用diskpart 
1、启用diskpart 
进入DOS命令行，输入DISKPART 
2、查看机器磁盘 
DISKPART> list disk

```
磁盘 ### 状态 大小 可用 Dyn Gpt 
-------- ------------- ------- ------- --- --- 
磁盘 0 联机 238 GB 1024 KB 
磁盘 1 联机 28 GB 0 B

DISKPART> 
```
根据大小可判断U盘为磁盘1 
3、选择磁盘1 
DISKPART> select disk 1 
4、输入CLEAN删除磁盘 
DISKPART> clean 
5、创建主磁盘分区 
DISKPART>CREATE PARTITION PRIMARY 
6、激活磁盘分区 
DISKPART> active 
7、以FAT32格式快速格式化磁盘分区 
DISKPART>FORMAT FS=FAT32 QUICK
# Linux基础命令

## 软链接
`ln -s -T /media/mmcblk0p1/ mmcblk0p1`
创建一个名字叫做mmcblk0p1的指向/media/mmcblk0p1/的软链接

## 系统运行时间
`uptime`
或者
`who -b`

## 解压缩/压缩
把filesys文件夹压缩成filesys.tar.gz:
`tar -czvf filesys.tar.gz filesys/`

解压filesys.tar.gz文件:
`tar xzvf filesys.tar.gz`

解压.tar.bz2文件
`tar   -jxvf    xx.tar.bz2`

通常解压.tar的文件不需要z选项

## 文件查找
`find /work/share/NVC200E/ipnc_uc -mtime -3`
查找3天之内(含3天本身)倍更改过的文件
见P233

`find /work/share/NVC200E/ipnc_uc -name ndkDemo.c`
在指定目录搜索指定名称的文件

## mount
直接输入mount: 显示目前挂载的信息

将某装置的文件名挂载到某位置
mount 装置文件名 挂载点
例如: `mount /dev/hdc6 /mnt/hdc6`
把/dev/hdc6 挂载到/mnt/hdc6上 

`unmount`
unmount [-fn] 装置名或挂载点

-f 强制删除
-n 不更新/etc/mtab 情况下卸除

## 设置IP
`ifconfig eth0 172.17.4.77`

## 查看端口占用
`netstat -apn`

## 查看进程内存占用情况
`cat /proc/进程pid/statm`
查看某进程的内存使用情况, 显示的第二项为实际物理内存消耗


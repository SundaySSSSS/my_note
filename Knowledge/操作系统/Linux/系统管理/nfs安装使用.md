# nfs安装使用
（一）安装NFS服务器
1.1-安装Ubuntu nfs服务器端：

sudo apt-get install nfs-kernel-server

1.2-安装nfs的客户端：

sudo apt-get install nfs-common​

(在安装nfs-kernel-server的时候，也会安装nfs-commom。如果没有安装这个软件包，则要执行1.2中的命令了)
1.3-设置共享的文件目录

sudo mkdir /***/***

（二）配置NFS
2.1-修改配置文件/etc/exports

在最后一行添加：/home/USER/nfs *(rw,sync,no_root_squash,no_subtree_check)
前面那个目录是与nfs服务客户端共享的目录，*代表允许所有的网段访问（也可以使用具体的IP）
rw：挂接此目录的客户端对该共享目录具有读写权限
sync：资料同步写入内存和硬盘
no_root_squash：客户机用root访问该共享文件夹时，不映射root用户。（root_squash：客户机用root用户访问该共享文件夹时，将root用户映射成匿名用户）
no_subtree_check：不检查父目录的权限。
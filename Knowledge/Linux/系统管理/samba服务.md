# samba服务

## 常用命令

检查samba服务状态
`service smbd status`

启动samba服务
`service smbd start`

## 安装配置方法
### 安装samba
如果能联网, 可以使用
`sudo apt-get install samba`

### 建立共享目录
比如想把/home/share设为和外界共享的目录
可以
`sudo mkdir /home/share`
`sudo chmod 777 /home/share`

### 修改samba配置文件
打开samba配置文件
`sudo gedit /etc/samba/smb.conf`
追加如下信息, 并保存
```
[share]
comment=VMware Ubuntu Share
path=/work/share
public=yes
writable=yes
available = yes
```

如果想强制使用root创建目录或文件, 可以加上
```
force user = root
force group = root
```

如果想控制生成的文件和目录的权限, 可以使用如下:
```
create mask = 0755
directory mask = 0755
```


### 重启samba服务
`sudo service smbd restart`


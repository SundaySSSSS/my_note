# docker安装与配置
## Ubuntu中
### apt-get方式
`sudo apt-get install -y docker.io`
安装完毕后，启动docker
`systemctl start docker`
设置开机就启动docker
`systemctl enable docker`
查看docker是否安装成功
`docker version`


### 使用docker维护的版本
1, 先检查APT的HTTPS支持, 查看
`/usr/lib/apt/methdos/https`文件是否存在
如果不存在:
使用`apt-get update`, `apt-get install -y apt-transport-https`

2, 
`sudo apt-get install -y curl`
`curl -sSL https://get.docker.com/ubuntu/ | sudo sh`

## Windows中
windows上本身不能运行docker
可以使用Boot2Docker

### 下载Boot2Docker
`https://github.com/boot2docker/boot2docker`
下载docker-install.exe
安装docker-install.exe

## MacOS中

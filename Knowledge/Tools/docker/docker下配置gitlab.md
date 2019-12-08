# docker下配置gitlab
## windows下安装docker
安装docker toolbox
下载地址：http://mirrors.aliyun.com/docker-toolbox/windows/docker-toolbox/

docker toolbox 是一个工具集，它主要包含以下一些内容：
```
Docker CLI 客户端，用来运行docker引擎创建镜像和容器
Docker Machine. 可以让你在windows的命令行中运行docker引擎命令
Docker Compose. 用来运行docker-compose命令
Kitematic. 这是Docker的GUI版本
Docker QuickStart shell. 这是一个已经配置好Docker的命令行环境
Oracle VM Virtualbox. 虚拟机
```
## 启动Docker QuickStart shell
如果没有正常启动， 则再Docker QuickStart Shell上右键属性， 将目标改为：
`"E:\Program Files\Git\bin\bash.exe" --login -i "E:\Develop\Docker Toolbox\start.sh"`

前半部分要是git的bin目录下的bash.exe


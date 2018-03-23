# ssh基本使用
## 安装ssh
`apt-get install openssh-server`

## 检查ssh服务状态
`service ssh status`

## 启动(重启)ssh服务
`service ssh restart`

## 让ssh允许root登陆
修改/etc/ssh/sshd_config文件
找到`PermitRootLogin without-passwd`一行
改为`PermitRootLogin yes`
再重启ssh服务

## 连接ssh
`ssh root@192.168.0.112`
其中, root是用户名, 192.168.0.112是要连接机器的ip

## 让ssh开机自启动
`update-rc.d ssh enable`
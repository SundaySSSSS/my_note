# 搭建ftp服务器

安装vsftpd
`sudo apt-get install vsftpd`

配置vsftpd， 修改`/etc/vsftpd.conf`
`listen=YES`
`#listen_ipv6=YES`
注： listen和listen_ipv6只能有一个
`anonymous_enable=NO` 禁止匿名登陆
`write_enable=YES`
`local_umask=022`

重启vsftpd
`sudo service vsftpd restart`
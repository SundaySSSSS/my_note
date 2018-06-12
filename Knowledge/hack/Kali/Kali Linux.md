# Kali Linux
## 安装后配置
### 修改apt源
`/etc/apt/sources.list`文件中, 替换原来的源为:
```
#中科大的源
deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
deb http://mirrors.ustc.edu.cn/kali kali-rolling main contrib non-free
deb-src http://mirrors.ustc.edu.cn/kali kali-rolling main contrib non-free
deb http://mirrors.ustc.edu.cn/kali-security kali-current/updates main contrib non-free
deb-src http://mirrors.ustc.edu.cn/kali-security kali-current/updates main contrib non-free
```
### 更新软件
`apt update`
`apt -y full-upgrade`

完成后重启
`reboot`

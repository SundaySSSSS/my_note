# awk用法
awk是一个文本分析工具，简单来说awk就是把文件逐行读入，以空格为默认分隔符将每行切片， 切开的部分再进行各种分析处理

##基本格式：
awk 'pattern + action' {filenames}

## awk的工作流程：
1， 读入一行（按\n分割）
2， 按照指定的域分割符（用-F指定）划分域，默认的分隔符为空格或Tab
    其中$0表示所有域， $1表示第一个域，$2表示第二个域

## 简单示例：
假如`/etc/passwd`内容为：
`root:*:0:0:System Administrator:/var/root:/bin/sh`
则：
`cat /etc/passwd | awk -F ':' '{ print $1 }'`
结果为：
`root`

`cat /etc/passwd | awk -F ':' '{ print $5 }'`
结果为：
`System Administrator`

`cat /etc/passwd | awk -F ':' '{ print $0 }'`
结果为：
`root:*:0:0:System Administrator:/var/root:/bin/sh`

显示账户和对应的shell（$1和$7）,并用tab分割
`cat /etc/passwd | awk -F ':' '{ print $1“\t”$7 }'`
结果为：
`root	/bin/sh`

## 在结果的开头和结尾添加内容：（使用BEGIN和END）
`cat /etc/passwd | awk -F ':' 'BEGIN{print "the first line"} {print $1","$7} END{ print "the last line" }'`
结果为：
```
the first line
root,/bin/sh
the last line
```

## pattern的使用示例
`awk 'pattern + action' {filenames}`
例如， 要找到`/etc/passwd`中带有root的行，找到后打印对应shell($7)
`awk -F: '/root/ {print $7}' /etc/passwd`
结果为：
`/bin/sh`
其中pattern为/root/, 用/正则表达式/来表示待匹配的内容, 这里就是找带有root的行
action为{print $7}

## awk的内置变量
ARGC 命令行参数个数
ARGV 命令行参数排列
ENVIRON 支持队列中系统环境变量的使用 <-何意？
FILENAME awk浏览的文件名
FNR 浏览文件的记录数
FS 设置输入域分隔符,等价于命令行-F选项
NF 浏览记录的域的个数
NR 已读的记录数
OFS 输出域分隔符
ORS 输出记录分隔符
RS 控制记录分隔符
$0 整行
$1 当前行第一个域
$n 当前行第n个域, n=1,2,3...
例子:

`awk -F ':' '{print "filename: " FILENAME ", linenumber: " NR ", columns: " NF ", linecontent: " $0}' /etc/passwd`
结果为:
`filename: /etc/passwd, linenumber: 1, columns: 7, linecontent: root:*:0:0:System Administrator:/var/root:/bin/sh`
print可以改为printf,printf用法和C语言类似
`awk -F ':' '{ printf("filename: %s, linenumber: %s, columns: %s, linecontent: %s\n", FILENAME, NR, NF, $0) }' /etc/passwd`
结果为:
`filename: /etc/passwd, linenumber: 12, columns: 7, linecontent: root:*:0:0:System Administrator:/var/root:/bin/sh`

## 数组的应用:
数组使用的简单例子:
`awk -F ':' 'BEGIN {count=0;} {name[count] = $1;count++;}; END {for (i = 0; i < NR; i++) print i, name[i]}' /etc/passwd`
结果为:
```
0 root
1 daemon
2 bin
3 sys
4 sync
5 games
```

## split
使用split分割字串,并存入数组
例如:
将`China Hebei 1-2-3-4-5`变成如下形式:
```
China Hebei 1
China Hebei 2
China Hebei 3
China Hebei 4
China Hebei 5
```
可以使用
`echo "China Hebei 1-2-3-4-5" | awk '{n = split($3, a, "-"); for(i = 1; i <= n; i++) print $1, $2, a[i]}'`



## 综合例子:
fw_printenv程序会打印uboot环境变量, 内容为:
```
baudrate=115200                                                                 
autoload=yes                                                                    
verify=yes                                                                      
bootfile=uImage                                                                 
ramdisk_file=ramdisk.gz                                                         
loadaddr=0x81000000                                                             
script_addr=0x80900000                                                          
loadbootscript=fatload mmc 0 ${script_addr} boot.scr                            
bootscript= echo Running bootscript from MMC/SD to set the ENV...; source ${scri
pt_addr}                                                                        
currentimage=4                                                                  
ethact=cpsw                                                                     
passwd=env@2015                                                                 
bootdelay=1                                                                     
tftpu=tftp 0x40300000 u-boot.bin; go 0x40300000                                 
uduimage=tftp 0x81000000 uImage;nand erase 0x280000 0x300000;nand write.i 0x81000000 0x280000 0x300000;reset                                                    
fileaddr=81000000                                                               
netmask=255.255.248.0                                                           
ipaddr=172.16.2.193                                                             
serverip=172.16.2.190                                                           
filesize=210                                                                    
sdtest=0                                                                        
netupdate=1                                                                     
ethaddr=00:20:17:08:14:01                                                       
bootcmd=ipnc_ff_init 1;nboot 0x81000000 0 0x280000;nand read 0x81400000 0x6C0000 0xA00000;bootm                                                                 
nandupdate=0                                                                    
stdin=serial                                                                    
stdout=serial                                                                   
stderr=serial                                                                   
ver=Second U-Boot 41.0.9.170413 (Apr 14 2017 - 09:02:45)                        
bootargs=mem=200M console=ttyO0,115200n8 root=/dev/nfs nfsroot=172.16.4.78:/work /share/NVC200E/ipnc_uc/target/filesys ip=172.16.4.77:172.16.4.33:172.16.0.1:255.
255.240.0::eth0:off vmalloc=830M vram=4M notifyk.vpssm3_sva=0xbfd00000 cmemk.phy s_start=0xA8000000 cmemk.phys_end=0xADE00000 cmemk.allowOverlap=1 rootdelay=10 forbid_video_recog=1                                                             
bootsuccess=1 
```
要解析出`forbid_video_recog`的值
`/usr/bin/fw_printenv | awk '/bootargs/ {print $0}' | awk '{n = split($0, array, " ");for(i = 1; i <= n; i++) print array[i]}' | awk -F '=' '{if ($1 == "forbid_video_recog") print $2}'`









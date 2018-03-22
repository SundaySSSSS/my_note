# 设置固定ip

修改`/etc/network/interfaces`文件
```
auto lo

iface lo inet loopback
iface eth0 inet static 

address 192.168.0.110
netmask 255.255.255.0
gateway 192.168.0.1

allow-hotplug wlan0
iface wlan0 inet static
wpa-ssid "Tenda_54160"
wpa-psk "15531100568"
address 192.168.0.111
netmask 255.255.255.0
gateway 192.168.0.1
```

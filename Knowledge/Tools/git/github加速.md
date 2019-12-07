# github加速（Windows）
## 一、打开http://IPAddress.com网站，查询下面3个网址对应的IP地址
1. http://github.com
2. http://assets-cdn.github.com
3. http://github.global.ssl.fastly.net

## 二、修改本地电脑系统hosts文件
路径 C:\Windows\System32\drivers\etc
直接在最后加入以下代码
140.82.113.4     github.com
185.199.108.153  assets-cdn.github.com
199.232.5.194    github.global.ssl.fastly.net

## 三、刷新系统dns缓存
用WIN+R快捷键打开运行窗口，输入命令：cmd并回车进入命令行窗口。

接着输入命令：ipconfig /flushdns回车后执行刷新本地dns缓存数据即可。

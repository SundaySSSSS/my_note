# win7自带截图不好用解决方案
win7系统打开截图工具显示“截图工具当前未在计算机上运行” 如何解决
2016年12月20日 11:52:20
阅读数：18719

1、首先在C盘中搜索tpcps.dll；

2、将数据最大那个tpcps.dll文件拷贝制C:\Windows\System32；

3、然后，再在C盘搜索InkObj.dll文件；

4、将数据最大那个InkObj.dll文件拷贝制C:\Windows\System32；

5、打开“运行”程序； 

6、输入 “regsvr32 InkObj.dll”，然后点击确认。 

7、输入 “regsvr32 tpcps.dll”，然后点击确认。  
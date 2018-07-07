# QT发布程序(windows环境)
qt官方已经做好了发布程序的软件, 名为
`windeployqt.exe`
一般在QT安装目录下, 例如
`D:\Qt\Qt5.7.0\5.7\msvc2013_64\bin`

将此路径加入系统环境变量

将自己要发布的程序编译成为Release版本, 找到编译好的exe, 例如`demo.exe`
自己建一个空的文件夹, 把`demo.exe`放进去
在此目录下启动命令行, 输入命令
`windeployqt demo.exe`
等待生成完毕即可
生成的translate文件夹是多语言支持的, 不需要可以删去
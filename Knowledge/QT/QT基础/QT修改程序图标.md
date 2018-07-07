# QT修改程序图标

找一个ico文件, 例如demo.ico
放到代码目录下, 如res/demo.ico
在pro文件中添加如下代码
```C++
RC_ICONS = res/demo.ico
```

在工程上右键, 选择[执行qmake]
在工程上右键, 选择[重新构建]

之后的程序的图标就被替换为了demo.ico

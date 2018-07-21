# QT编译Oracle驱动

## 软件环境
QT环境: 5.5.1 mingw
oracle11g client 32位

备注: 由于5.5.1 mingw只有32位的, 故只能使用32位的oracle客户端

QT安装目录为:
`D:\Qt\Qt5.5.1\5.5`
需要安装源代码

Oracle安装目录为:
`D:/development/oracleBase`
32位的客户端为client_2

## 编译步骤
进入目录: `D:\Qt\Qt5.5.1\5.5\Src\qtbase\src\plugins\sqldrivers\oci`

用QT打开里面的oci.pro文件


在oci.pro中加入两行:
```
INCLUDEPATH +=D:/development/oracleBase/product/11.2.0/client_2/oci/include
LIBPATH +=D:/development/oracleBase/product/11.2.0/client_2/oci/lib/msvc
```

执行qmake , 重新构建
成功后, 在目录
`D:\Qt\Qt5.5.1\5.5\Src\qtbase\plugins\sqldrivers`
下会生成四个文件
```
libqsqloci.a
libqsqlocid.a
qsqloci.dll
qsqlocid.dll
```

将其复制到如下文件夹内, 就可以使用了
`D:\Qt\Qt5.5.1\5.5\mingw492_32\plugins\sqldrivers`
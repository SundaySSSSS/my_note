# mac下QT找不到sdk的问题
问题现象: xcode卸载重新安装旧版本后, 编译原来的Qt项目出现如下问题:

no such sysroot directory:

'/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk' [-Wmissing-sysroot]

【解决办法】

‎⁨1、 在安装目录： ▸ ⁨Qt5.11.1⁩ ▸ ⁨5.11.1⁩ ▸ ⁨clang_64⁩ ▸ ⁨mkspecs⁩  下找到文件：qdevice.pri

打开后，把此行：

QMAKE_MAC_SDK = macosx
改为：

QMAKE_MAC_SDK = macosx10.14
记得保存。

2、Qt5 中清理项目、构建项目；

3、项目正常通过。

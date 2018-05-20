# boost编译安装

1， 运行Bootstrap.bat
2， b2.exe -toolset=msvc-12.0 address-model=64 install --prefix="D:\Program Files\boost\1.6.0\msvc2013_64" --without-graph_parallel --without-python -j8 link=static runtime-link=shared --build-type=complete
（用vs2013， 64位的编译器进行编译， 安装到目录：D:\Program Files\boost\1.6.0\msvc2013_64）

如果要编译出静态的（文件名中有s标记， 见下面的库名介绍），去掉编译命令中的runtime-link=shared

3， 在VS中引入boost库 设置 项目属性VC++目录  
包含目录D:\Program Files\boost\1.6.0\msvc2013_64\include\boost-1_66
库目录和引用目录 D:\Program Files\boost\1.6.0\msvc2013_64\lib

boost编译后的lib文件命名规则
libboost_filesystem-vc80-mt-sgdp-1_42.lib
前缀：统一为lib，但在Windows下只有静态库有lib前缀；
库名称：以"boost一”开头的库名称，在这里是boost_filesystem；
编译器标识：编译该库文件的编译器名称和版本，在这里是-vc80；
多线程标识：支持多线程使用-mt，没有表示不支持多线程；
ABI标识：这个标识比较复杂，标识了Boost库的几个编译链接选项；
s：  静态库标识；
gd：debug版标识；
p：  使用STlport而不是编译器自带STL实现；
版本号：Boost库的版本号，小数点用下画线代替，在这里是1_42；
扩展名：在Windows上是lib，在Linux等类Unix操作系统上是a或者.so。
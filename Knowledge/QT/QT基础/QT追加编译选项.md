# QT追加编译选项
在pro文件中加入类似的条目即可
```
QMAKE_CXXFLAGS   +=    -std=c++11

QMAKE_CFLAGS += -fPIC

# 添加库文件
# 静态库
linux：LIBS += your_lib_path/your_lib
# 动态库
linux：LIBS += -L your_lib_path -lyour_lib//经过测试了
```
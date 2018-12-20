# QT 下使用openmp

在pro文件中追加:

```
QMAKE_CXXFLAGS += -fopenmp
LIBS += -lgomp
```

linux操作系统上, 貌似需要加入以下内容, windows + mingw不需要

```
LIBS += lpthread
```
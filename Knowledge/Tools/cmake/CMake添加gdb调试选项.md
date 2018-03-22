# CMake添加gdb调试选项

在配置文件中追加如下即可
```
SET(CMAKE_BUILD_TYPE "Debug")
SET(CMAKE_CXX_FLAGS_DEBUG "$(ENV{CXXFLAGS} -O0 -Wall -g)")
```

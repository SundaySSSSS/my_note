# Nanomsg交叉编译

## 1 修改CMakeLists.txt
在CMakeLists.txt中追加如下内容
`CMAKE_C_COMPILER`和`CMAKE_CXX_COMPILER`指定交叉编译的工具
`CMAKE_FIND_ROOT_PATH`指定交叉编译环境, 此目录下通常应该有bin, lib等目录(C库和头文件等) 
```
# this is required
SET(CMAKE_SYSTEM_NAME Linux)

# specify the cross compiler
SET(CMAKE_C_COMPILER   /work/share/NVC200E/ti_tools/linux_devkit/bin/arm-arago-linux-gnueabi-gcc)
SET(CMAKE_CXX_COMPILER /work/share/NVC200E/ti_tools/linux_devkit/bin/arm-arago-linux-gnueabi-g++)

# where is the target environment 
SET(CMAKE_FIND_ROOT_PATH  /work/share/NVC200E/ti_tools/linux_devkit)

# for libraries and headers in the target directories
SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
```
## 2 执行configure
在命令行运行
`./configure`

## 3 make
在命令行运行
`make`

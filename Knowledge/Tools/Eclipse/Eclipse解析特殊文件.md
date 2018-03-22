# Eclipse解析特殊文件

当某个工程里用了一些特殊的文件后缀, Eclipse无法解析的情况
比如nanomsg的文件中, 有一些是*.inc的
Eclipse不认识inc文件, 就把它当做文本文件解析了

解决方法:
Window->Preferences
C/C++->File Types
在里面追加inc的解析格式

回到工程, 右键工程
Index->Rebuild
所有inc的文档就被解析了


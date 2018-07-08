# QT 调用WindowsAPI

不仅需要#include <windows.h>
还需要在pro文件中加入对应的lib库
如：
```
LIBS +=User32.LIB
```

否则会发生类似如下的错误:
```
SyaringanWidget.obj:-1: error: LNK2019: 无法解析的外部符号 __imp_RegisterHotKey，该符号在函数 "public: __cdecl SyaringanWidget::SyaringanWidget(class QWidget *)" (??0SyaringanWidget@@QEAA@PEAVQWidget@@@Z) 中被引用
```
# windows动态库编写
需要注意:
1, C的接口函数要加`extern "C"`
2, C的接口函数要加`__declspec(dllexport)`

例如:
``` C
extern "C" __declspec(dllexport) void thisIsAExportFunction(int a, int b);
```

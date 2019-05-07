# VS编译时_提示要定义_CRT_SECURE_NO_WARNINGS

可能是用到了`fopen`等不安全的函数
解决方法为:
在项目->属性->配置属性->C/C++->预处理器 中
预处理器定义中, 追加`_CRT_SECURE_NO_WARNINGS`即可
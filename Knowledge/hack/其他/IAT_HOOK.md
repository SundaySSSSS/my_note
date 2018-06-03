# IAT_HOOK

## 基本概念
IAT: import address table 输入地址表
里面存储了各种API的地址, 如MessageBox等地址

## windows程序正常调用API的过程
1, PE文件加载的过程中会自动填写要使用的API地址到IAT表
2, 程序中调用过程: `near dword ptr ds:[IAT表]`
3, 跳转到API的具体实现中去执行

## hack基本思路
1, 需要一个可以修改程序内存的代码 - 一个弹头, payload 有效载荷
2, 需要一个程序将1中的代码发送到目标程序中 - 一个导弹 missile

# 3_Windows API编程
## 文件系统API
### 文件相关API
```C++
CreateFile
DeleteFile
ReadFile
WriteFile
FlushFileBuffers
SetFilePointer
CopyFile
```

### 驱动器及目录API
```C++
GetLogicalDriveString
GetDriveType //输入"C:\", 输出光盘/硬盘/U盘等
CreateDirectory
RemoveDirectory
GetModuleFileName //获取程序路径
```

## 一个删不掉的文件夹
在cmd中
```
mkdir cannot_del_dir
cd cannot_del_dir
mkdir haha..\
```
这样, cannot_del_dir文件夹则无法被删除
要删除需要如下操作
```
rd cannot_del_dir\haha..\
rd cannot_del_dir
```
## 注册表API
```C++
RegOpenKeyEx //打开注册表
RegCloseKey //关闭注册表
RegCreateKeyEx //创建子键
RegDeleteKey //删除子键
RegQueryValueEx //查询注册表
RegSetValueEx //写入注册表
RegEnumKeyEx //遍历注册表
RegEnumValue
```
### 示例: 系统启动项管理
系统启动项的注册表位置是:
`计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`


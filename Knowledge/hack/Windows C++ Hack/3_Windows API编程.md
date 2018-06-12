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
这个示例并不好用, 读不到, 写不进去, 且必须用管理员权限运行才能Open成功, 咱不知道问题所在
```C++

#define REG_RUN "Software\\Microsoft\\Windows\\CurrentVersion\\Run"

int main(int argc, char** argv)
{
	HKEY hKey = NULL;
	LONG lRet = RegOpenKeyEx(HKEY_LOCAL_MACHINE, REG_RUN, 0, KEY_ALL_ACCESS, &hKey);
	if (lRet != ERROR_SUCCESS)
	{
		printf("Cannot Find %s\n", REG_RUN);
		return -1;
	}
	if (hKey == NULL)
	{
		printf("Open Key Failed\n");
		return -1;
	}
	int i = 0;
	char szValueName[MAXBYTE] = { 0 };
	DWORD dwNameSize = MAXBYTE;
	char szValueKey[MAXBYTE] = { 0 };
	DWORD dwKeySize = MAXBYTE;
	DWORD dwType = 0;

	while (1)
	{
		lRet = RegEnumValue(hKey, i, szValueName, &dwNameSize, NULL, 
			&dwType, (LPBYTE)szValueKey, &dwKeySize);
		if (lRet != ERROR_NO_MORE_ITEMS)
		{
			printf("---Find %d item\n", i);
			break;
		}
		printf("%03d --- %s : %s\n", i, szValueName, szValueKey);

		ZeroMemory(szValueName, MAXBYTE);
		ZeroMemory(szValueKey, MAXBYTE);
		dwNameSize = MAXBYTE;
		dwKeySize = MAXBYTE;
		++i;

	}

	// 向注册表中追加一项内容
	RegSetValueEx(hKey, "keyName", 0, REG_SZ, (const unsigned char*)"keyValue", 9);


	RegCloseKey(hKey);

	getchar();
	return 0;
}

```

## 服务相关API
### API一览
```C++
OpenSCManager
CloseServiceHandle
EnumServicesStatus
OpenService
ControlService
```

### 服务的类型
大体上分为Win32应用程序服务 和 驱动程序服务, 对应的宏值分别为:
SERVICE_WIN32 和 SERVICE_DRIVER
这两个宏值也是其他宏值的组合

### 枚举服务
```C++
#include <windows.h>
#include <stdio.h>

int printServiceList(DWORD dwServiceType)
{
	SC_HANDLE hSCM = OpenSCManager(NULL, NULL, SC_MANAGER_ALL_ACCESS);
	if (NULL == hSCM)
	{
		printf("OpenSCManager Error\n");
		return -1;
	}

	DWORD ServiceCount = 0;
	DWORD dwSize = 0;
	LPENUM_SERVICE_STATUS lpInfo;

	BOOL bRet = EnumServicesStatus(hSCM, dwServiceType,
		SERVICE_STATE_ALL, NULL, 0, &dwSize,
		&ServiceCount, NULL);
	//第一次必定失败, 原因应该是ERROR_MORE_DATA
	//因为送入的buff是NULL
	if (!bRet && GetLastError() == ERROR_MORE_DATA)
	{
		printf("expected!!!\n");
		//分配缓冲区
		lpInfo = (LPENUM_SERVICE_STATUS)(new BYTE[dwSize]);
		bRet = EnumServicesStatus(hSCM,
			dwServiceType, SERVICE_STATE_ALL,
			(LPENUM_SERVICE_STATUS)lpInfo,
			dwSize, &dwSize, &ServiceCount, NULL);
		if (!bRet)
		{
			CloseServiceHandle(hSCM);
			printf("EnumServicesStatus Error\n");
			return -1;
		}
		//遍历数据, 打印
		for (DWORD i = 0; i < ServiceCount; ++i)
		{
			printf("%s : %s : %d\n", lpInfo[i].lpDisplayName, lpInfo[i].lpDisplayName, lpInfo[i].ServiceStatus.dwCurrentState);
		}
		delete[] lpInfo;
		CloseServiceHandle(hSCM);
	}
	else
	{
		printf("NaNi!!! unexpected result!!!\n");
	}
	return 0;
}

int main(int argc, char* argv[])
{
	printServiceList(SERVICE_WIN32);
	getchar();
	return 0;
}
```

### 服务的启动和停止
```C++

int startAndStopService(const char* serviceName)
{
	SC_HANDLE hSCM = OpenSCManager(NULL, NULL, SC_MANAGER_ALL_ACCESS);
	if (NULL == hSCM)
	{
		printf("OpenSCManger Error\n");
		return -1;
	}
	SC_HANDLE hSCService = OpenService(hSCM, serviceName, SERVICE_ALL_ACCESS);
	BOOL bRet = StartService(hSCService, 0, NULL);
	if (bRet)
	{
		printf("Service Start Success\n");
		printf("Running...\n");
		Sleep(3);
		printf("Stop...\n");
		SERVICE_STATUS ServiceStatus;
		ControlService(hSCService, SERVICE_CONTROL_STOP, &ServiceStatus);
		if (bRet)
		{
			printf("Stop Success\n");
		}
		else
			printf("Stop Failed\n");
	}
	else
		printf("Service Start Failed\n");

	CloseServiceHandle(hSCService);
	CloseServiceHandle(hSCM);
	return 0;
}

int main(int argc, char* argv[])
{
	//printServiceList(SERVICE_WIN32);
	startAndStopService("AdobeFlashPlayerUpdateSvc");
	getchar();
	return 0;
}
```

## 进程相关API
### API一览
```C++
WinExec
CreateProcess
```

### 示例
使用WinExec打开进程
```C++
WinExec("C:\\windows\\system32\\notepad.exe", SW_SHOW);
```
使用CreateProcess打开进程
```C++
#define EXEC_FILE "C:\\windows\\system32\\notepad.exe"

int main(int argc, char* argv[])
{
	//WinExec(EXEC_FILE, SW_SHOW);
	PROCESS_INFORMATION pi = { 0 };
	STARTUPINFO si = { 0 };

	BOOL bRet = CreateProcess(EXEC_FILE, NULL, NULL, NULL, FALSE,
		NULL, NULL, NULL, &si, &pi);
	if (!bRet)
	{
		printf("CreateProcess Error\n");
		return -1;
	}
	CloseHandle(pi.hThread);
	CloseHandle(pi.hProcess);
	return 0;
}
```













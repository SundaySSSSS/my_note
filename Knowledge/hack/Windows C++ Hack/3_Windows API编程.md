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
WinExec()
CreateProcess()
GetWindowThreadProcessId() //通过hWnd获取pid
OpenProcess()
TerminateProcess()

//使用以下函数必须包含Tlhelp32.h
//进程枚举
CreateToolhelp32Snapshot()
Process32First()
Process32Next()
//线程枚举
CreateToolhelp32Snapshot()
Thread32First()
Thread32Next()
//进程中DLL枚举
CreateToolhelp32Snapshot()
Module32First()
Module32Next()

//暂停/恢复进程
SuspendThread() <-进程恢复就是操作进程的所有线程
ResumeThread()
```

### 示例
#### 打开进程
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

#### 关闭进程
下面的例子可以关闭一个记事本进程(title必须为"无标题 - 记事本")
```C++

int ProcessUtils::closeProcess(string title)
{
	HWND hWnd = FindWindow(NULL, title.c_str());
	if (hWnd == NULL)
		return -1;
	DWORD dwPid = 0;
	GetWindowThreadProcessId(hWnd, &dwPid);
	if (dwPid == 0)
		return -1;
	HANDLE hHandle = OpenProcess(PROCESS_ALL_ACCESS, FALSE, dwPid);
	if (hHandle == NULL)
		return -1;
	BOOL bRet = TerminateProcess(hHandle, 0);
	if (bRet)
	{
		MessageBox(NULL, "成功", NULL, MB_OK);
	}
	CloseHandle(hHandle);
	return 0;
}

int main(int argc, char** argv)
{
	string title = "无标题 - 记事本";
	int ret = ProcessUtils::closeProcess(title);
	getchar();
	return 0;
}
```

#### 进程枚举
```C++
int ProcessUtils::listAllProcess()
{
	//创建进程快照
	HANDLE hSnap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
	if (hSnap == INVALID_HANDLE_VALUE)
	{
		printf("CreateToolhelp32Snapshot Error");
		return -1;
	}
	PROCESSENTRY32 Pe32 = { 0 };
	Pe32.dwSize = sizeof(PROCESSENTRY32);
	BOOL bRet = Process32First(hSnap, &Pe32);
	int i = 0;
	while (bRet)
	{
		printf("%03d : pid = %d, %s\n", i, Pe32.th32ProcessID, Pe32.szExeFile);
		bRet = Process32Next(hSnap, &Pe32);
		++i;
	}
	CloseHandle(hSnap);
	return 0;
}
```

#### 指定进程中加载的DLL枚举
```C++
int ProcessUtils::listDllInProcess(int pid)
{
	int nPid = pid;
	if (nPid == 0)
		return -1;
	MODULEENTRY32 Me32 = { 0 };
	Me32.dwSize = sizeof(MODULEENTRY32);

	//创建模块快照
	HANDLE hSnap = CreateToolhelp32Snapshot(TH32CS_SNAPMODULE, nPid);
	if (hSnap == INVALID_HANDLE_VALUE)
	{
		printf("CreateToolhelp32Snapshot error\n");
		return -1;
	}

	BOOL bRet = Module32First(hSnap, &Me32);
	while (bRet)
	{
		printf("module: %s, path = %s\n", Me32.szModule, Me32.szExePath);
		bRet = Module32Next(hSnap, &Me32);
	}
	CloseHandle(hSnap);
	return 0;
}
```
上面的程序无法打开系统进程加载的动态库
为解决这个问题, 可以将权限提升至"SeDebugPrivilege"

#### 提升权限, 以枚举DLL
```C++

int ProcessUtils::ImprovePrivilege()
{
	HANDLE hToken = NULL;
	BOOL bRet = OpenProcessToken(GetCurrentProcess(), TOKEN_ALL_ACCESS, &hToken);
	if (bRet)
	{
		TOKEN_PRIVILEGES tp;
		tp.PrivilegeCount = 1;
		LookupPrivilegeValue(NULL, SE_DEBUG_NAME, &tp.Privileges[0].Luid);
		tp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED;
		AdjustTokenPrivileges(hToken, FALSE, &tp, sizeof(tp), NULL, NULL);
		CloseHandle(hToken);
		return 0;
	}
	return -1;
}
```
即使加上上面代码后, 仍然需要以管理员权限运行程序, 才能正常打开

#### 暂停/恢复进程
```C++

int ProcessUtils::suspendResumeThread(int pid, int ctl)
{
	int nPid = pid;
	if (nPid <= 0)
		return -1;
	//遍历进程中的所有线程
	HANDLE hSnap = CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, nPid);
	if (hSnap == INVALID_HANDLE_VALUE)
	{
		printf("CreateToolhelp32Snapshot Error\n");
		return -1;
	}

	THREADENTRY32 Te32 = { 0 };
	Te32.dwSize = sizeof(THREADENTRY32);
	BOOL bRet = Thread32First(hSnap, &Te32);
	while (bRet)
	{
		if (Te32.th32OwnerProcessID == nPid)
		{
			HANDLE hThread = OpenThread(THREAD_ALL_ACCESS, FALSE, Te32.th32ThreadID);
			if (ctl == 0)
			{	//暂停线程
				DWORD ret = SuspendThread(hThread);
				printf("suspend thread...ret = %d\n", ret);
			}
			else if (ctl == 1)
			{	//恢复线程
				
				DWORD ret = ResumeThread(hThread);
				printf("resume thread... ret = %d\n", ret);
			}
			CloseHandle(hThread);
		}
		bRet = Thread32Next(hSnap, &Te32);
	}
	CloseHandle(hSnap);
	return 0;
}
```
多次suspend线程, 也需要同样的resume次数才能让线程恢复
可以查阅ResumeThread返回值的意义

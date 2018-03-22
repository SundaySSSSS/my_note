# [LinuxC]获取进程工作路径

```
//获取当前目录
int GetWorkPath(char *workPath,int pathLen)
{
	//工作目录长度
	int nLen = 0;
	//循环变量
	int i=0;
	int nIndex = 0;
	char filePath[255];
	if(workPath == NULL)
		return 0;
	pid_t pid = getpid();
    	snprintf(filePath, 255, "/proc/%d/exe", pid);
	//获取当前可执行程序全路径
	nLen = readlink(filePath,workPath,pathLen);
	for(i=0; i<nLen; i++)
	{
		if(workPath[i] == '/')
			nIndex = i;
	}
	workPath[nIndex] = 0x00;
	return 1;
}


```

# [LinuxC]获取目录剩余空间

```
/**
	函数功能：得到一个目录的剩余空间M
	参数：rootpath 需要获得剩余空间大小的目录
	返回值：该目录剩余的大小空间 M
*/
long long File_GetFreeSpace(const char *rootpath)
{
	int ret = 0;
	struct statfs diskInfo;
	ret = statfs(rootpath, &diskInfo);
	if(ret == -1)
		return -1;
	unsigned long long blocksize = diskInfo.f_bsize;    //每个block里包含的字节数
	unsigned long long totalsize = blocksize * diskInfo.f_blocks;   //总的字节数，f_blocks为block的数目
	unsigned long long freeDisk = diskInfo.f_bfree * blocksize; //剩余空间的大小
	unsigned long long availableDisk = diskInfo.f_bavail * blocksize;   //可用空间大小
//	printf("Disk_free = %llu MB = %llu GB\n"
//			"Disk_available = %llu MB = %llu GB\n",
//			freeDisk>>20, freeDisk>>30, availableDisk>>20, availableDisk>>30);
	return (freeDisk>>20);
}


```

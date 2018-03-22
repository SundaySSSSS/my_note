# [LinuxC]设置系统时间

```c
/************************************************
设置操作系统时间
参数:*dt数据格式为"2006-4-20 20:30:30"
调用方法:
    char *pt="2006-4-20 20:30:30";
    SetSystemTime(pt);
**************************************************/
int SetSystemTime(char *dt)
{
    int year, mon, day, hour, min, sec;
    	struct tm _tm;
    	struct timeval tv;
    	time_t timep;
    	sscanf(dt, "%d-%d-%d %d:%d:%d", &year,
    		    &mon, &day,&hour,
    		    &min, &sec);
    	_tm.tm_sec = sec;
    	_tm.tm_min = min;
    	_tm.tm_hour = hour;
    	_tm.tm_mday = day;
    	_tm.tm_mon = mon - 1;
    	_tm.tm_year = year - 1900;

    	timep = mktime(&_tm);
    	tv.tv_sec = timep;
    	tv.tv_usec = 0;
    	if(settimeofday (&tv, (struct timezone *) 0) < 0)
    	{
        		printf("Set system datatime error!\n");
        		return -1;
    	}
    	return 0;
}
```

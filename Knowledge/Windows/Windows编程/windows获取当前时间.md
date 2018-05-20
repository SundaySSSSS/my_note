# windows获取当前时间
## 使用C标准库（精确到秒级）：
```C++
#include <time.h>
#include <stdio.h>
int main( void )
{
time_t t = time(0);
char tmp[64];
strftime( tmp, sizeof(tmp), "%Y/%m/%d %X %A 本年第%j天 %z",localtime(&t) );
puts( tmp );
return 0;
}
```
其中 time_t 定义如下：
```C++
#ifndef _TIME_T_DEFINED
typedef long time_t;        /* time value */
#define _TIME_T_DEFINED     /* avoid multiple def's of time_t */
#endif
time_t time(time_t * timer);//获得日历时间（Calendar Time）
```
如果你已经声明了参数timer，你可以从参数timer返回现在的日历时间，同时也可以通过返回值返回现在的日历时间，即从一个时间点（例如：1970年 1月1日0时0分0秒）到现在此时的秒数。如果参数为空（NULL），函数将只通过返回值返回现在的日历时间;

## 使用Windows API-----GetLocalTime函数（精确到毫秒级）：
```C++
#include <windows.h>
#include <stdio.h>
int main( void )
{
SYSTEMTIME sys;
GetLocalTime( &sys );
printf( "%4d/%02d/%02d %02d:%02d:%02d.%03d 星期%1d\n", sys.wYear,   ys.wMonth,  sys.wDay, sys.wHour, sys.wMinute, sys.wSecond,sys.wMilliseconds,sys.wDayOfWeek);
return 0;
}
```
其中SYSTEMTIME的定义如下：
```C++
typedef struct _SYSTEMTIME {
WORD wYear;
WORD wMonth;
WORD wDayOfWeek;
WORD wDay;
WORD wHour;
WORD wMinute;
WORD wSecond;
WORD wMilliseconds;
} SYSTEMTIME, *PSYSTEMTIME, *LPSYSTEMTIME;
```
## 使用Windows API（精确到微秒级）：
如果想提高精度，可以使用QueryPerformanceCounter和QueryPerformanceFrequency。这两个函数不是在每个 系统中都支持。对于支持它们的系统中，可以获得低于1ms的精度。Windows 内部有一个精度非常高的定时器, 精度在微秒级, 但不同的系统这个定时器的频率不同, 这个频率与硬件和操作系统都可能有关。利用 API 函数 QueryPerformanceFrequency 可以得到这个定时器的频率。利用 API 函数 QueryPerformanceCounter 可以得到定时器的当前值。根据要延时的时间和定时器的频率, 可以算出要延时的时间定时器经过的周期数。在循环里用 QueryPerformanceCounter 不停的读出定时器值, 一直到经过了指定周期数再结束循环, 就达到了高精度延时的目的。
```C++
LARGE_INTEGER m_nFreq;
LARGE_INTEGER m_nTime;
QueryPerformanceFrequency(&m_nFreq); // 获取时钟周期
QueryPerformanceCounter(&m_nTime);//获取当前时间
printf(" time:%lld us",(m_lm.QuadPart*1000000/m_nFreq.QuadPart));//m_nFreq.QuadPart为:次数/s，这样就可以获得毫秒级别的了。
```
LARGE_INTEGER的定义为：
```C++
#if defined(MIDL_PASS)
typedef struct _LARGE_INTEGER {
#else // MIDL_PASS
typedef union _LARGE_INTEGER {
struct {
DWORD LowPart;
LONG HighPart;
};
struct {
DWORD LowPart;
LONG HighPart;
} u;
#endif //MIDL_PASS
LONGLONG QuadPart;
} LARGE_INTEGER;
 
```

```C++
 /////////////////////////////////////////////////
#include <iostream>
#include <windows.h>
using namespace    std;
////////////////////////////////////////////////
void main()
{
    _LARGE_INTEGER time_start;    /*开始时间*/
    _LARGE_INTEGER time_over;        /*结束时间*/
    double dqFreq;                /*计时器频率*/
    LARGE_INTEGER f;            /*计时器频率*/
    QueryPerformanceFrequency(&f);
    dqFreq=(double)f.QuadPart;
    QueryPerformanceCounter(&time_start);
    Sleep(1000);/*循环耗时*/
    QueryPerformanceCounter(&time_over); 
    cout<<((time_over.QuadPart-time_start.QuadPart)/dqFreq)<<endl;//单位为秒，精度为1000 000/（cpu主频）微秒
}
```
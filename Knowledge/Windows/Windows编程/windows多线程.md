# windows多线程
## 基本使用

```C++
#include <windows.h>
#include <stdio.h>
 
static int number=10;
CRITICAL_SECTION CriticalSection;
 
DWORD WINAPI ThreadOne(LPVOID lpParameter)
{
    printf("窗口1售票开始:\n");
    while(1)
    {
         EnterCriticalSection(&CriticalSection);  
         if(number>0)
         {
             printf("窗口1售出第%d张票...\n",number);
             number--;
             Sleep(1000);        
         }
         LeaveCriticalSection(&CriticalSection);
         Sleep(100);
    }
    return 0;
}
 DWORD WINAPI ThreadTwo(LPVOID lpParameter)
 {
     printf("窗口2售票开始:\n");
     while(1)
     {
         EnterCriticalSection(&CriticalSection);
         if(number>0)
         {
             printf("窗口2售出第%d张票...\n",number);
             Sleep(1000);
             number--;
         }
         LeaveCriticalSection(&CriticalSection);
         Sleep(100);
     }
     return 0;
 }
 
 
 int main()
 {
     HANDLE HOne,HTwo;
     InitializeCriticalSection(&CriticalSection);
     printf("***********************vpoet******************\n");
     HOne=CreateThread(NULL,0,ThreadOne,NULL,0,NULL);
     HTwo=CreateThread(NULL,0,ThreadTwo,NULL,0,NULL);
     CloseHandle(HOne);
     CloseHandle(HTwo);
     while(TRUE)
     {
         if(number==0)
         {
             printf("不好意思,票卖完了!\n");
             DeleteCriticalSection(&CriticalSection);
             return 0;
         }
         else
         {
             continue;
         }    
     }
     
     return 0;
 }
```

## 等待线程终止
```C++
 WaitForSingleObject(handle, INFINITE);	//handle为CreateThread的返回值
 ```
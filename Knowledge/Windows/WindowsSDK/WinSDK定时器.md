# WinSDK定时器
#### **定时器使用步骤**
##### **1, 初始化**
在初始化时, 调用SetTimer
函数原型:
```
WINUSERAPI
UINT_PTR
WINAPI
SetTimer(
    _In_opt_ HWND hWnd,
    _In_ UINT_PTR nIDEvent,
    _In_ UINT uElapse,
    _In_opt_ TIMERPROC lpTimerFunc);
```
例如:
``` 
#define ID_MY_TIMER (1) 
SetTimer(hwnd, ID_MY_TIMER, 1000, NULL);	//1秒后触发

```
或者注册回调函数, 例如:
```
void CALLBACK MyTimerCallBack(HWND hwnd, UINT message, UINT iTimerID, DWORD dwTime)
{
	/* Do Something */
}
SetTimer(hwnd, ID_MY_TIMER, 1000, MyTimerCallBack);
```

##### **2, 处理超时**
如果没有在SetTimer时指定回调函数, 则需要处理WM_TIMER消息
如果已经设定回调函数, 则超时处理写在回调函数中
##### **3, 销毁计时器**
在不需要计时器时, 调用KillTime进行销毁
例如:
```
KillTimer(hwnd, ID_MY_TIMER);
```
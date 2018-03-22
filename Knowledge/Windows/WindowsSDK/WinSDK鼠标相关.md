# WinSDK鼠标相关

```

鼠标
fMouse = GetSystemMetrics(SM_MOUSEPRESENT)
//判断是否连接鼠标, 如果鼠标已经被安装, fMouse的值是非0, 否则为0

cButtons = GetSystemMetrics(SM_CMOUSEBUTTONS);
//判断鼠标的按钮个数

鼠标消息
WM_MOUSEMOVE
WM_LBUTTONDOWN WM_LBUTTONUP WM_LBUTTONDBLCLK
WM_MBUTTONDOWN WM_MBUTTONUP WM_MBUTTONDBLCLK
WM_RBUTTONDOWN WM_RBUTTONUP WM_RBUTTONDBLCLK

x坐标 GET_X_LPARAM(lParam)或LOWORD(lParam)
y坐标 GET_Y_LPARAM(lParam)或HIWORD(lParam)

wParam标记鼠标按键的状态
wParam & MK_LBUTTON == 1  鼠标左键按下
MK_MBUTTON
MK_RBUTTON
MK_SHIFT
MK_CONTROL
```
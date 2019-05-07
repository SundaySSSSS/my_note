# WinSDK按钮
按钮作为window的一种, 可以通过CreateWindow来进行创建
如下代码创建了一个最基本的push button, 按下后会触发WM_COMMAND消息

#### **PushButton代码**
此代码显示了一个按钮, 按下后显示一个消息框
```

#include <windows.h>

#define WINDOW_WIDTH 800
#define WINDOW_HEIGHT 600


/* 全局变量定义区 */
char* g_szApplicationName = "AppName";
char* g_szWindowClassName = "windowClassName";

/* 消息回调函数 */
LRESULT CALLBACK WindowProc(HWND   hwnd,
	UINT   msg,
	WPARAM wParam,
	LPARAM lParam)
{
	HDC hdc;
	PAINTSTRUCT ps;
	RECT rect;

	switch (msg)
	{
	case WM_CREATE:
		CreateWindow(TEXT("Button"), TEXT("PUSHBUTTON"), 
			WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON, 
			30, 30, 200, 50,
			hwnd, (HMENU)1, 
			((LPCREATESTRUCT)lParam)->hInstance, NULL);
		return 0;
	case WM_COMMAND:    //按钮被按下后的响应
		MessageBox(hwnd, TEXT("button pressed"), TEXT("Info"), MB_OK);
		return 0;
	case WM_PAINT:
		hdc = BeginPaint(hwnd, &ps);
		GetClientRect(hwnd, &rect);
		DrawText(hdc, TEXT("This is a window program"), -1, &rect,
			DT_SINGLELINE | DT_CENTER | DT_VCENTER);
		EndPaint(hwnd, &ps);
		break;
	case WM_DESTROY:
		//终了程序,发送WM_QUIT消息  
		PostQuitMessage(0);
		break;
	}

	return DefWindowProc(hwnd, msg, wParam, lParam);
}


int WINAPI WinMain(HINSTANCE hInstance,
	HINSTANCE hPrevInstance,
	LPSTR     szCmdLine,
	int       iCmdShow)
{
	HWND hWnd;	//窗口句柄
	WNDCLASSEX winclass;	//窗口类对象

							//窗口类对象的初始化
	winclass.cbSize = sizeof(WNDCLASSEX);
	winclass.style = CS_HREDRAW | CS_VREDRAW;
	winclass.lpfnWndProc = WindowProc;
	winclass.cbClsExtra = 0;
	winclass.cbWndExtra = 0;
	winclass.hInstance = hInstance;
	winclass.hIcon = LoadIcon(NULL, IDI_APPLICATION);
	winclass.hCursor = LoadCursor(NULL, IDC_ARROW);
	winclass.hbrBackground = NULL;
	winclass.lpszMenuName = NULL;
	winclass.lpszClassName = g_szWindowClassName;
	winclass.hIconSm = LoadIcon(NULL, IDI_APPLICATION);

	//注册窗口类
	if (!RegisterClassEx(&winclass))
	{
		MessageBox(NULL, "Registration Failed!", "Error", 0);
		return 0;
	}

	//创建窗口  
	hWnd = CreateWindowEx(NULL,                 // extended style
		g_szWindowClassName,  // window class name
		g_szApplicationName,  // window caption
		WS_OVERLAPPEDWINDOW,  // window style
		0,                    // initial x position
		0,                    // initial y position
		WINDOW_WIDTH,         // initial x size
		WINDOW_HEIGHT,        // initial y size
		NULL,                 // parent window handle
		NULL,                 // window menu handle
		hInstance,            // program instance handle
		NULL);                // creation parameters

							  //容错处理
	if (!hWnd)
	{
		MessageBox(NULL, "CreateWindowEx Failed!", "Error!", 0);
		return 0;
	}

	//显示窗口
	ShowWindow(hWnd, iCmdShow);
	UpdateWindow(hWnd);

	MSG msg;
	while (GetMessage(&msg, NULL, 0, 0))
	{
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}

	return msg.wParam;
}


```

#### **其他类型按钮展示:**
如下代码显示了常见按钮样式, 执行效果如下图
![这里写图片描述](http://img.blog.csdn.net/20170625172958443?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzIxODkwNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
```


#include <windows.h>

#define WINDOW_WIDTH 800
#define WINDOW_HEIGHT 600

struct
{
	int iStyle;
	TCHAR *szText;
} button[] = {	//按钮的样式
	BS_PUSHBUTTON,		TEXT("PUSHBUTTON"),
	BS_DEFPUSHBUTTON,	TEXT("BS_DEFPUSHBUTTON"),
	BS_CHECKBOX,		TEXT("BS_CHECKBOX"),
	BS_AUTOCHECKBOX,	TEXT("BS_AUTOCHECKBOX"),
	BS_RADIOBUTTON,		TEXT("BS_RADIOBUTTON"),
	BS_3STATE,			TEXT("BS_3STATE"),
	BS_AUTO3STATE,		TEXT("BS_AUTO3STATE"),
	BS_GROUPBOX,		TEXT("BS_GROUPBOX"),
	BS_USERBUTTON,		TEXT("BS_USERBUTTON"),
	BS_AUTORADIOBUTTON,	TEXT("BS_AUTORADIOBUTTON"),
	BS_PUSHBOX,			TEXT("BS_PUSHBOX"),
	BS_OWNERDRAW,		TEXT("BS_OWNERDRAW"),
};

#define BUTTON_NUM (sizeof button / sizeof button[0])


/* 全局变量定义区 */
char* g_szApplicationName = "AppName";
char* g_szWindowClassName = "windowClassName";

/* 消息回调函数 */
LRESULT CALLBACK WindowProc(HWND   hwnd,
	UINT   msg,
	WPARAM wParam,
	LPARAM lParam)
{
	HDC hdc;
	PAINTSTRUCT ps;
	RECT rect;
	static int cxChar, cyChar;
	int i;

	switch (msg)
	{
	case WM_CREATE:
		cxChar = LOWORD(GetDialogBaseUnits());
		cyChar = HIWORD(GetDialogBaseUnits());

		for (i = 0; i < BUTTON_NUM; ++i)
		{
			CreateWindow(TEXT("Button"), button[i].szText,
				WS_CHILD | WS_VISIBLE | button[i].iStyle,
				cxChar, cyChar * (1 + 2 * i),
				20 * cxChar, 2 * cyChar, 
				hwnd, (HMENU)i,
				((LPCREATESTRUCT)lParam)->hInstance, NULL);
		}
		
		return 0;
	case WM_COMMAND:
		MessageBox(hwnd, TEXT("button pressed"), TEXT("Info"), MB_OK);
		return 0;
	case WM_PAINT:
		hdc = BeginPaint(hwnd, &ps);
		GetClientRect(hwnd, &rect);
		DrawText(hdc, TEXT("This is a window program"), -1, &rect,
			DT_SINGLELINE | DT_CENTER | DT_VCENTER);
		EndPaint(hwnd, &ps);
		break;
	case WM_DESTROY:
		//终了程序,发送WM_QUIT消息  
		PostQuitMessage(0);
		break;
	}

	return DefWindowProc(hwnd, msg, wParam, lParam);
}


int WINAPI WinMain(HINSTANCE hInstance,
	HINSTANCE hPrevInstance,
	LPSTR     szCmdLine,
	int       iCmdShow)
{
	HWND hWnd;	//窗口句柄
	WNDCLASSEX winclass;	//窗口类对象

							//窗口类对象的初始化
	winclass.cbSize = sizeof(WNDCLASSEX);
	winclass.style = CS_HREDRAW | CS_VREDRAW;
	winclass.lpfnWndProc = WindowProc;
	winclass.cbClsExtra = 0;
	winclass.cbWndExtra = 0;
	winclass.hInstance = hInstance;
	winclass.hIcon = LoadIcon(NULL, IDI_APPLICATION);
	winclass.hCursor = LoadCursor(NULL, IDC_ARROW);
	winclass.hbrBackground = NULL;
	winclass.lpszMenuName = NULL;
	winclass.lpszClassName = g_szWindowClassName;
	winclass.hIconSm = LoadIcon(NULL, IDI_APPLICATION);

	//注册窗口类
	if (!RegisterClassEx(&winclass))
	{
		MessageBox(NULL, "Registration Failed!", "Error", 0);
		return 0;
	}

	//创建窗口  
	hWnd = CreateWindowEx(NULL,                 // extended style
		g_szWindowClassName,  // window class name
		g_szApplicationName,  // window caption
		WS_OVERLAPPEDWINDOW,  // window style
		0,                    // initial x position
		0,                    // initial y position
		WINDOW_WIDTH,         // initial x size
		WINDOW_HEIGHT,        // initial y size
		NULL,                 // parent window handle
		NULL,                 // window menu handle
		hInstance,            // program instance handle
		NULL);                // creation parameters

							  //容错处理
	if (!hWnd)
	{
		MessageBox(NULL, "CreateWindowEx Failed!", "Error!", 0);
		return 0;
	}

	//显示窗口
	ShowWindow(hWnd, iCmdShow);
	UpdateWindow(hWnd);

	MSG msg;
	while (GetMessage(&msg, NULL, 0, 0))
	{
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}

	return msg.wParam;
}

```
#### **处理按钮按下**
如下代码修改自fishc讲解的示例代码
代码运行效果如下:
![这里写图片描述](http://img.blog.csdn.net/20170625173313062?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzIxODkwNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
在菜单中选择后, 点击提交按钮会弹出对话框, 显示选择的内容
点击[随便]按钮, 会随机选择一个, 并禁止在此选择
```
#include <windows.h>
#include <stdlib.h>
#include <time.h>

#define WINDOW_WIDTH 800
#define WINDOW_HEIGHT 600

#define FOOD_NUM 4
#define GROUP_BUTTON_ID (FOOD_NUM + 1)
#define PUSH_BUTTON_COMMIT_ID (FOOD_NUM + 2)
#define PUSH_BUTTON_RANDOM_ID (FOOD_NUM + 3)


/* 全局变量定义区 */
TCHAR* g_szApplicationName = "吃什么???";
TCHAR* g_szWindowClassName = "windowClassName";

/* 消息回调函数 */
LRESULT CALLBACK WindowProc(HWND   hwnd,
	UINT   msg,
	WPARAM wParam,
	LPARAM lParam)
{
	RECT rect;
	TCHAR* foods[FOOD_NUM] = { TEXT("恐龙肉"), TEXT("蓝鲸腿"), TEXT("章鱼舌"), TEXT("凤凰蛋") };
	static HWND hwndButton[FOOD_NUM] = { 0 };
	static int cxChar, cyChar;
	static int choosed = -1;

	switch (msg)
	{
	case WM_CREATE:
		cxChar = LOWORD(GetDialogBaseUnits());
		cyChar = HIWORD(GetDialogBaseUnits());

		//修改窗口尺寸
		GetWindowRect(hwnd, &rect);
		MoveWindow(hwnd, rect.left, rect.top, 27 * cxChar, 13 * cyChar, TRUE);
		for (int i = 0; i < FOOD_NUM; ++i)
		{
			hwndButton[i] = CreateWindow(TEXT("button"), foods[i], 
				BS_AUTORADIOBUTTON | WS_CHILD | WS_VISIBLE, 
				2 * cxChar, cyChar * (2 + 2 * i), 
				10 * cxChar, 7 * cyChar / 4,
				hwnd, (HMENU)i,
				((LPCREATESTRUCT)lParam)->hInstance, NULL);
		}
		CreateWindow(TEXT("button"), "菜单：",
			BS_GROUPBOX | WS_CHILD | WS_VISIBLE,
			cxChar, cyChar / 2,
			12 * cxChar, 10 * cyChar,
			hwnd, (HMENU)GROUP_BUTTON_ID,
			((LPCREATESTRUCT)lParam)->hInstance, NULL);
		CreateWindow(TEXT("button"), "提交",
			BS_PUSHBUTTON | WS_CHILD | WS_VISIBLE,
			14 * cxChar, cyChar,
			10 * cxChar, 7 * cyChar / 4,
			hwnd, (HMENU)PUSH_BUTTON_COMMIT_ID,
			((LPCREATESTRUCT)lParam)->hInstance, NULL);
		CreateWindow(TEXT("button"), "随便",
			BS_PUSHBUTTON | WS_CHILD | WS_VISIBLE,
			14 * cxChar, 3 * cyChar,
			10 * cxChar, 7 * cyChar / 4,
			hwnd, (HMENU)PUSH_BUTTON_RANDOM_ID,
			((LPCREATESTRUCT)lParam)->hInstance, NULL);
		return 0;
	case WM_COMMAND:
	{
		int id = LOWORD(wParam);
		if (id < FOOD_NUM)
		{
			choosed = id;
		}
		switch (id)
		{
		case PUSH_BUTTON_COMMIT_ID:	//选择按钮
			if (choosed == -1)
			{
				MessageBox(hwnd, TEXT("尚未选择！！！"), TEXT("警告"), MB_OK);
			}
			else
			{
				MessageBox(hwnd, foods[choosed], TEXT("你选择的食物"), MB_OK);
			}
			break;
		case PUSH_BUTTON_RANDOM_ID:	//随便按钮
			if (choosed != -1)
			{	//取消上一个按钮的选中状态(给子窗口发送消息来实现)
				SendMessage(GetDlgItem(hwnd, choosed), BM_SETCHECK, BST_UNCHECKED, 0);
			}
			srand((unsigned int) time(NULL));
			choosed = rand() % FOOD_NUM;
			//设置单选按钮为选中状态(给子窗口发送消息来实现)
			SendMessage(GetDlgItem(hwnd, choosed), BM_SETCHECK ,BST_CHECKED, 0);
			//之后把食物选项和随便按钮禁用
			for (int i = 0; i < FOOD_NUM; ++i)
			{
				EnableWindow(GetDlgItem(hwnd, i), FALSE);
			}
			EnableWindow(GetDlgItem(hwnd, PUSH_BUTTON_RANDOM_ID), FALSE);
			break;
		default:
			return DefWindowProc(hwnd, msg, wParam, lParam);
		}
	}
		return 0;

	case WM_DESTROY:
		//终了程序,发送WM_QUIT消息  
		PostQuitMessage(0);
		break;
	}

	return DefWindowProc(hwnd, msg, wParam, lParam);
}


int WINAPI WinMain(HINSTANCE hInstance,
	HINSTANCE hPrevInstance,
	LPSTR     szCmdLine,
	int       iCmdShow)
{
	HWND hWnd;	//窗口句柄
	WNDCLASSEX winclass;	//窗口类对象

							//窗口类对象的初始化
	winclass.cbSize = sizeof(WNDCLASSEX);
	winclass.style = CS_HREDRAW | CS_VREDRAW;
	winclass.lpfnWndProc = WindowProc;
	winclass.cbClsExtra = 0;
	winclass.cbWndExtra = 0;
	winclass.hInstance = hInstance;
	winclass.hIcon = LoadIcon(NULL, IDI_APPLICATION);
	winclass.hCursor = LoadCursor(NULL, IDC_ARROW);
	winclass.hbrBackground = (HBRUSH)(COLOR_BTNFACE + 1);	//窗口背景颜色设置为按钮的颜色
	winclass.lpszMenuName = NULL;
	winclass.lpszClassName = g_szWindowClassName;
	winclass.hIconSm = LoadIcon(NULL, IDI_APPLICATION);

	//注册窗口类
	if (!RegisterClassEx(&winclass))
	{
		MessageBox(NULL, "Registration Failed!", "Error", 0);
		return 0;
	}

	//创建窗口  
	hWnd = CreateWindowEx(NULL,                 // extended style
		g_szWindowClassName,  // window class name
		g_szApplicationName,  // window caption
		WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU,  // window style
		0,                    // initial x position
		0,                    // initial y position
		WINDOW_WIDTH,         // initial x size
		WINDOW_HEIGHT,        // initial y size
		NULL,                 // parent window handle
		NULL,                 // window menu handle
		hInstance,            // program instance handle
		NULL);                // creation parameters

							  //容错处理
	if (!hWnd)
	{
		MessageBox(NULL, "CreateWindowEx Failed!", "Error!", 0);
		return 0;
	}

	//显示窗口
	ShowWindow(hWnd, iCmdShow);
	UpdateWindow(hWnd);

	MSG msg;
	while (GetMessage(&msg, NULL, 0, 0))
	{
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}

	return msg.wParam;
}

```
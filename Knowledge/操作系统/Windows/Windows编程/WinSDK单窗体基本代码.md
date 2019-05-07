
# Windows SDK 单窗口基本代码

#### **使用方法:**
在VS中建立一个空的工程, 添加一个main.cpp文件, 将下方代码粘贴进去, 即可运行

#### **单窗口基本代码:**
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
#### **增加双缓冲窗体的代码:**
在此窗口上进行描画不会发生闪烁

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
	//存储用户窗口的宽和高
	static int cxClient, cyClient;

	//用于创建后备缓冲
	static HDC		hdcBackBuffer;
	static HBITMAP	hBitmap;
	static HBITMAP	hOldBitmap;

	switch (msg)
	{
	case WM_CREATE:
	{
		RECT rect;

		GetClientRect(hwnd, &rect);

		cxClient = rect.right;
		cyClient = rect.bottom;

		//将窗口移动到屏幕中央
		int scrWidth, scrHeight;
		scrWidth = GetSystemMetrics(SM_CXSCREEN);
		scrHeight = GetSystemMetrics(SM_CYSCREEN);
		GetWindowRect(hwnd, &rect);
		MoveWindow(hwnd, (scrWidth - rect.right) / 2, (scrHeight - rect.bottom) / 2, 
			rect.right - rect.left, rect.bottom - rect.top, FALSE);

		//后备缓冲区相关处理
		hdcBackBuffer = CreateCompatibleDC(NULL);
		HDC hdc = GetDC(hwnd);
		hBitmap = CreateCompatibleBitmap(hdc, cxClient, cyClient);
		hOldBitmap = (HBITMAP)SelectObject(hdcBackBuffer, hBitmap);
		//销毁处理
		ReleaseDC(hwnd, hdc);
	}
	break;
	case WM_KEYUP:
		//按下Esc退出
		switch (wParam)
		{
		case VK_ESCAPE:
			PostQuitMessage(0);
			break;
		}
		break;
	case WM_PAINT:
		PAINTSTRUCT ps;
		BeginPaint(hwnd, &ps);
		//对界面进行描画, 这里只是涂上黑色
		BitBlt(hdcBackBuffer,
			0,
			0,
			cxClient,
			cyClient,
			NULL,
			NULL,
			NULL,
			BLACKNESS);

		BitBlt(ps.hdc, 0, 0, cxClient, cyClient, hdcBackBuffer, 0, 0, SRCCOPY);
		EndPaint(hwnd, &ps);

		//描画延迟
		Sleep(10);
		break;
	case WM_SIZE:
	{
		//变更窗口大小时的处理
		cxClient = LOWORD(lParam);
		cyClient = HIWORD(lParam);

		SelectObject(hdcBackBuffer, hOldBitmap);
		DeleteObject(hBitmap);
		HDC hdc = GetDC(hwnd);
		hBitmap = CreateCompatibleBitmap(hdc,
			cxClient,
			cyClient);

		ReleaseDC(hwnd, hdc);
		SelectObject(hdcBackBuffer, hBitmap);
	}
	break;
	case WM_DESTROY:
		//清除并销毁后备缓冲区
		SelectObject(hdcBackBuffer, hOldBitmap);
		DeleteDC(hdcBackBuffer);
		DeleteObject(hBitmap);

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
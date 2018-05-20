# WinSDK实例_康威生命游戏(一)
### **生命游戏简介**

> 生命游戏其实是一个零玩家游戏，它包括一个二维矩形世界，这个世界中的每个方格居住着一个活着的或死了的细胞。一个细胞在下一个时刻生死取决于相邻八个方格中活着的或死了的细胞的数量。如果相邻方格活着的细胞数量过多，这个细胞会因为资源匮乏而在下一个时刻死去；相反，如果周围活细胞过少，这个细胞会因太孤单而死去。实际中，你可以设定周围活细胞的数目怎样时才适宜该细胞的生存。如果这个数目设定过低，世界中的大部分细胞会因为找不到太多的活的邻居而死去，直到整个世界都没有生命；如果这个数目设定过高，世界中又会被生命充满而没有什么变化。实际中，这个数目一般选取2或者3；这样整个生命世界才不至于太过荒凉或拥挤，而是一种动态的平衡。这样的话，游戏的规则就是：当一个方格周围有2或3个活细胞时，方格中的活细胞在下一个时刻继续存活；即使这个时刻方格中没有活细胞，在下一个时刻也会“诞生”活细胞。在这个游戏中，还可以设定一些更加复杂的规则，例如当前方格的状况不仅由父一代决定，而且还考虑祖父一代的情况。你还可以作为这个世界的上帝，随意设定某个方格细胞的死活，以观察对世界的影响。
在游戏的进行中，杂乱无序的细胞会逐渐演化出各种精致、有形的结构；这些结构往往有很好的对称性，而且每一代都在变化形状。一些形状已经锁定，不会逐代变化。有时，一些已经成形的结构会因为一些无序细胞的“入侵”而被破坏。但是形状和秩序经常能从杂乱中产生出来。

(引用自百度百科)
### **程序界面**

![](http://img.blog.csdn.net/20170625211944927?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzIxODkwNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

### **使用的知识点**

1. windows窗口的建立
2. 按钮
3. 定时器
4. C++基础内存操作

### **具体实现**
整个程序分为两部分:
1. 底层数据管理
2. 界面描绘和控制逻辑
#### **1, 底层数据管理**
为了使逻辑结构可移植, 使用C++编写了类CWorld, 不涉及任何界面绘图操作
##### **基本思路:**
建立两块内存分别用于:
1. 记录当前细胞分布
2. 记录下一回合细胞分布

每一回合(Turn)的计算方法如下:
每个细胞的生死遵循下面的原则：
1． 如果一个细胞周围有3个细胞为生（一个细胞周围共有8个细胞），则该细胞为生（即该细胞若原先为死，则转为生，若原先为生，则保持不变） 。
2． 如果一个细胞周围有2个细胞为生，则该细胞的生死状态保持不变；
3． 在其它情况下，该细胞为死（即该细胞若原先为生，则转为死，若原先为死，则保持不变）

接口代码(World.h):
```
#ifndef _LIFE_GAME_WORLD_H_
#define _LIFE_GAME_WORLD_H_

typedef struct _SCell
{
	int isAlive;
} 
SCell;
/* 注意:
	细胞的坐标是从0开始的
*/
class CWorld
{
private:
	int m_width;
	int m_height;
	SCell* m_map1;	//地图buffer1
	SCell* m_map2;	//地图buffer2
	SCell* m_cur_map;	//当前地图
	SCell* m_new_map;	//下一轮使用的地图
	void setCurCell(int x, int y, int isAlive);
	void setNewCell(int x, int y, int isAlive);
	int getAroundCellNum(int x, int y);	//获得某个位置周围存活的细胞数量
	int isPosValid(int x, int y);	//判定输入位置是否有效, 1-有效 0-无效
	void swapMap(void) { SCell* temp = m_cur_map; m_cur_map = m_new_map; m_new_map = temp; }	//交换地图
	SCell* getCell(SCell* buf, int x, int y) { return buf + y * m_width + x; };	//从地图buffer中获取某坐标的细胞指针
public:
	CWorld(int width, int height);
	~CWorld();
	void ramdomInit(void);	//随机初始化地图
	void killAll(void);		//杀死所有细胞
	void nextTurn(void);	//进入下一回合
	int getCellAlive(int x, int y); //获取细胞存活状态 , 返回值:1-存活, 0-死亡 -1-出错
	int setCellAlive(int x, int y, int isAlive);	//设置细胞存活状态 , 返回值:0-成功 负值-失败
	int getWidth() { return m_width; }		//获得当前地图宽度
	int getHeight() { return m_height; }	//获得当前地图高度
};

#endif /* _LIFE_GAME_WORLD_H_ */
```

具体实现代码:(World.cpp)
```
#include <time.h>
#include "World.h"
#include "global.h"


void CWorld::setCurCell(int x, int y, int isAlive)
{
	if (isPosValid(x, y) == 0)
	{
		return;
	}
	else
	{
		SCell* cell = getCell(m_cur_map, x, y);
		if (cell - m_cur_map >= m_width * m_height)
		{
			return;
		}
		cell->isAlive = isAlive;
	}
}

void CWorld::setNewCell(int x, int y, int isAlive)
{
	if (isPosValid(x, y) == 0)
	{
		return;
	}
	else
	{
		SCell* cell = getCell(m_new_map, x, y);
		if (cell - m_new_map >= m_width * m_height)
		{
			return;
		}
		cell->isAlive = isAlive;
	}
}

int CWorld::getAroundCellNum(int x, int y)
{
	int count = 0;

	if (isPosValid(x, y) == 0)
	{	//输入不合法
		return -1;
	}
	//尝试目标位置周围的八个相邻位置
	for (int i = x - 1; i <= x + 1; ++i)
	{
		for (int j = y - 1; j <= y + 1; ++j)
		{
			if (i == x && j == y)
			{
				continue;
			}
			if (isPosValid(i, j) == 1)
			{
				if (getCellAlive(i, j) == 1)
				{
					count++;
				}
			}
		}
	}

	return count;
}

int CWorld::isPosValid(int x, int y)
{
	if (x >= m_width || x < 0 || y >= m_height || y < 0)
	{
		return 0;
	}
	return 1;
}

CWorld::CWorld(int width, int height)
{
	m_width = width;
	m_height = height;
	m_map1 = (SCell *) new SCell[m_width * m_height];
	m_map2 = (SCell *) new SCell[m_width * m_height];
	m_cur_map = m_map1;
	m_new_map = m_map2;
	killAll();
}


CWorld::~CWorld()
{
	delete[] m_map1;
	delete[] m_map2;
}

void CWorld::ramdomInit()
{
	killAll();
	
	srand((unsigned)time(NULL)); //用时间做种，每次产生随机数不一样

	for (int i = 0; i < m_width; ++i)
	{
		for (int j = 0; j < m_height; ++j)
		{
			int isAlive = rand() % 2;  //产生0或1的随机数
			setCurCell(i, j, isAlive);
		}
		
	}
	
}

void CWorld::killAll(void)
{
	if (m_cur_map != NULL && m_new_map != NULL)
	{
		for (int i = 0; i < m_width; ++i)
		{
			for (int j = 0; j < m_height; ++j)
			{
				setCurCell(i, j, 0);
				setNewCell(i, j, 0);
			}
		}
	}
	
}

/*
每个细胞的生死遵循下面的原则：
1． 如果一个细胞周围有3个细胞为生（一个细胞周围共有8个细胞），则该细胞为生（即该细胞若原先为死，则转为生，若原先为生，则保持不变） 。
2． 如果一个细胞周围有2个细胞为生，则该细胞的生死状态保持不变；
3． 在其它情况下，该细胞为死（即该细胞若原先为生，则转为死，若原先为死，则保持不变）
*/
void CWorld::nextTurn(void)
{
	int aroundNum = 0;
	for (int i = 0; i < m_width; ++i)
	{
		for (int j = 0; j < m_height; ++j)
		{
			aroundNum = getAroundCellNum(i, j);
			if (aroundNum == 2)
			{
				setNewCell(i, j, getCellAlive(i, j));
			}
			else if (aroundNum == 3)
			{
				setNewCell(i, j, 1);
			}
			else
			{
				setNewCell(i, j, 0);
			}
		}
	}
	swapMap();
}

int CWorld::getCellAlive(int x, int y)
{
	if (isPosValid(x, y) == 0)
	{
		return -1;
	}
	SCell* cell = getCell(m_cur_map, x, y);
	return cell->isAlive;
}

int CWorld::setCellAlive(int x, int y, int isAlive)
{
	if (isPosValid(x, y) == 0)
	{
		return -1;
	}
	if (isAlive != 0 && isAlive != 1)
	{
		return -2;
	}
	SCell* cell = getCell(m_cur_map, x, y);
	cell->isAlive = isAlive;
	return 0;
}

```

#### **2, 界面描绘和控制逻辑**
main.cpp代码如下:

```
#include <time.h>
#include "global.h"
#include "World.h"

#define WORLD_TIMER_ID (1)	//定时器ID
#define WORLD_TIMER_ELAPSE (1000)	//定时器超时时间

#define RANDOM_BTN_ID (1)
#define START_BTN_ID (2)
#define PAUSE_BTN_ID (3)
#define NEXT_BTN_ID (4)
#define KILL_ALL_BTN_ID (5)

class CWorld *g_world = NULL;	//全局世界指针

//定时器超时回调函数
void CALLBACK WorldTimerCallBack(HWND hwnd, UINT message, UINT iTimerID, DWORD dwTime);
//描画函数
void CleanWorld(HDC hdc);
void DrawWorld(CWorld* world, int world_w, int world_h, HDC hdc);
void DrawCell(CWorld* world, HDC hdc);
void DrawGrid(HDC hdc, int w, int h);

void CreateButton(HWND hwnd, HINSTANCE hInstance);

/* 全局变量定义区 */
char* g_szApplicationName = "LifeGame";
char* g_szWindowClassName = "This Is My Window Class";

/* 消息回调函数 */
LRESULT CALLBACK WindowProc(HWND   hwnd,
	UINT   msg,
	WPARAM wParam,
	LPARAM lParam)
{
	//存储用户窗口的宽和高
	static int cxClient, cyClient;
	//界面字体宽高
	static int cxChar, cyChar;

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
		MoveWindow(hwnd, (scrWidth - rect.right) / 2, (scrHeight - rect.bottom) / 2, rect.right - rect.left, rect.bottom - rect.top, FALSE);

		//创建世界和生物
		g_world = new CWorld(WORLD_WIDTH, WORLD_HEIGHT);
		DrawWorld(g_world, WORLD_WIDTH, WORLD_HEIGHT, GetDC(hwnd));
		CreateButton(hwnd, ((LPCREATESTRUCT)lParam)->hInstance);
		EnableWindow(GetDlgItem(hwnd, START_BTN_ID), TRUE);	//启用开始按钮
		EnableWindow(GetDlgItem(hwnd, PAUSE_BTN_ID), FALSE);	//禁用暂停按钮
		EnableWindow(GetDlgItem(hwnd, NEXT_BTN_ID), TRUE);	//启用下一步按钮
		EnableWindow(GetDlgItem(hwnd, KILL_ALL_BTN_ID), TRUE);	//启用杀死所有按钮

		//后备缓冲区相关处理
		hdcBackBuffer = CreateCompatibleDC(NULL);
		HDC hdc = GetDC(hwnd);
		hBitmap = CreateCompatibleBitmap(hdc, cxClient, cyClient);
		hOldBitmap = (HBITMAP)SelectObject(hdcBackBuffer, hBitmap);
		//销毁处理
		ReleaseDC(hwnd, hdc);
		
		}
		break;
	case WM_COMMAND:    //按钮被按下后的响应
	{
		int button_id = LOWORD(wParam);
		switch (button_id)
		{
		case RANDOM_BTN_ID: //随机初始化按钮按下
			g_world->ramdomInit();
			DrawWorld(g_world, WORLD_WIDTH, WORLD_HEIGHT, GetDC(hwnd));
			break;
		case START_BTN_ID:	//开始按钮按下
			SetTimer(hwnd, WORLD_TIMER_ID, WORLD_TIMER_ELAPSE, WorldTimerCallBack);	//启动计时器
			EnableWindow(GetDlgItem(hwnd, RANDOM_BTN_ID), FALSE);	//禁用随机生成按钮
			EnableWindow(GetDlgItem(hwnd, START_BTN_ID), FALSE);	//禁用开始按钮
			EnableWindow(GetDlgItem(hwnd, PAUSE_BTN_ID), TRUE);	//启用暂停按钮
			EnableWindow(GetDlgItem(hwnd, NEXT_BTN_ID), FALSE);	//禁用下一步按钮
			EnableWindow(GetDlgItem(hwnd, KILL_ALL_BTN_ID), FALSE);	//禁用杀死所有按钮
			break;
		case PAUSE_BTN_ID:	//暂停按钮按下
			KillTimer(hwnd, WORLD_TIMER_ID);	//销毁计时器
			EnableWindow(GetDlgItem(hwnd, RANDOM_BTN_ID), TRUE);	//启用随机生成按钮
			EnableWindow(GetDlgItem(hwnd, START_BTN_ID), TRUE);	//启用开始按钮
			EnableWindow(GetDlgItem(hwnd, PAUSE_BTN_ID), FALSE);	//禁用暂停按钮
			EnableWindow(GetDlgItem(hwnd, NEXT_BTN_ID), TRUE);	//启用下一步按钮
			EnableWindow(GetDlgItem(hwnd, KILL_ALL_BTN_ID), TRUE);	//启用杀死所有按钮
			break;
		case NEXT_BTN_ID:	//下一步按钮按下
			g_world->nextTurn();
			DrawWorld(g_world, WORLD_WIDTH, WORLD_HEIGHT, GetDC(hwnd));
			break;
		case KILL_ALL_BTN_ID:	//杀死所有细胞按钮按下
			g_world->killAll();
			DrawWorld(g_world, WORLD_WIDTH, WORLD_HEIGHT, GetDC(hwnd));
			break;
		default:
			break;
		}
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
		//将后备缓冲区涂上黑色背景
		BitBlt(hdcBackBuffer,
				0,
				0,
				cxClient,
				cyClient,
				NULL,
				NULL,
				NULL,
				BLACKNESS);

		//描画世界
		DrawGrid(hdcBackBuffer, WORLD_WIDTH, WORLD_HEIGHT);
		DrawCell(g_world, hdcBackBuffer);

		BitBlt(ps.hdc, 0, 0, cxClient, cyClient, hdcBackBuffer, 0, 0, SRCCOPY);
		EndPaint(hwnd, &ps);
		break;
	case WM_SIZE:
	{
		//变更窗口大小时的处理
		cxClient = LOWORD(lParam);
		cyClient = HIWORD(lParam);
		//改变世界的大小
		//world->setWorldSize(cxClient, cyClient);

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
		//销毁世界
		delete g_world;

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

//超时后回调函数
void CALLBACK WorldTimerCallBack(HWND hwnd, UINT message, UINT iTimerID, DWORD dwTime)
{
	g_world->nextTurn();
	DrawWorld(g_world, WORLD_WIDTH, WORLD_HEIGHT, GetDC(hwnd));
}

//描画整个世界
void DrawWorld(CWorld * world, int world_w, int world_h, HDC hdc)
{
	CleanWorld(hdc);
	DrawGrid(hdc, world_w, world_h);
	DrawCell(world, hdc);
}

//将世界涂成黑色(背景色)
void CleanWorld(HDC hdc)
{
	HPEN BlackPen = CreatePen(PS_SOLID, 1, RGB(0, 0, 0));
	HBRUSH BlackBrush = CreateSolidBrush(RGB(0, 0, 0));
	SelectObject(hdc, BlackPen);
	SelectObject(hdc, BlackBrush);
	Rectangle(hdc, 0, 0, WORLD_WIDTH * CELL_SIZE, WORLD_HEIGHT * CELL_SIZE);
	DeleteObject(BlackPen);
	DeleteObject(BlackBrush);
}

//描画所有细胞
void DrawCell(CWorld* world, HDC hdc)
{
	HPEN BluePen = CreatePen(PS_SOLID, 1, RGB(0, 0, 128));
	HBRUSH BlueBrush = CreateSolidBrush(RGB(0, 0,128));
	SelectObject(hdc, BluePen);
	SelectObject(hdc, BlueBrush);
	for (int i = 0; i < world->getWidth(); ++i)
	{
		for (int j = 0; j < world->getHeight(); ++j)
		{
			if (world->getCellAlive(i, j) == 1)
			{
				Rectangle(hdc, i * CELL_SIZE, j * CELL_SIZE, i * CELL_SIZE + CELL_SIZE, j * CELL_SIZE + CELL_SIZE);
			}
		}
	}

	DeleteObject(BluePen);
	DeleteObject(BlueBrush);
}

//描画网格
void DrawGrid(HDC hdc, int w, int h)
{
	HPEN GrayPen = CreatePen(PS_SOLID, 1, RGB(128, 128, 128));
	//HBRUSH GreenBrush = CreateSolidBrush(RGB(0, 255, 0));
	SelectObject(hdc, GrayPen);
	//SelectObject(hdc, GreenBrush);
	for (int i = 0; i <= w; ++i)
	{
		MoveToEx(hdc, i * CELL_SIZE, 0, NULL);
		LineTo(hdc, i * CELL_SIZE, h * CELL_SIZE);
	}
	for (int i = 0; i <= h; ++i)
	{
		MoveToEx(hdc, 0, i * CELL_SIZE, NULL);
		LineTo(hdc, w * CELL_SIZE, i * CELL_SIZE);
	}

	DeleteObject(GrayPen);
	//DeleteObject(GreenBrush);
}

void CreateButton(HWND hwnd, HINSTANCE hInstance)
{
	RECT rect;
	GetClientRect(hwnd, &rect);
	int cxClient = rect.right;

	/* 建立按钮 */
	int cxChar = LOWORD(GetDialogBaseUnits());
	int cyChar = HIWORD(GetDialogBaseUnits());
	//开始按钮
	int button_w = cxChar * 12;
	int button_h = cyChar * 2;
	int button_x = cxClient - cxChar * 15;
	int random_btn_y = cyChar * 1;
	int start_btn_y = random_btn_y + button_h + cyChar;
	int pause_btn_y = start_btn_y + button_h + cyChar;
	int next_btn_y = pause_btn_y + button_h + cyChar;
	int kill_all_btn_y = next_btn_y + button_h + cyChar;

	CreateWindow(TEXT("Button"), TEXT("随机初始化"),
		WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
		button_x, random_btn_y, button_w, button_h,
		hwnd, (HMENU)RANDOM_BTN_ID,
		hInstance, NULL);
	CreateWindow(TEXT("Button"), TEXT("开始"),
		WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
		button_x, start_btn_y, button_w, button_h,
		hwnd, (HMENU)START_BTN_ID,
		hInstance, NULL);
	CreateWindow(TEXT("Button"), TEXT("暂停"),
		WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
		button_x, pause_btn_y, button_w, button_h,
		hwnd, (HMENU)PAUSE_BTN_ID,
		hInstance, NULL);
	CreateWindow(TEXT("Button"), TEXT("下一步"),
		WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
		button_x, next_btn_y, button_w, button_h,
		hwnd, (HMENU)NEXT_BTN_ID,
		hInstance, NULL);
	CreateWindow(TEXT("Button"), TEXT("杀死所有"),
		WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
		button_x, kill_all_btn_y, button_w, button_h,
		hwnd, (HMENU)KILL_ALL_BTN_ID,
		hInstance, NULL);
}


```

最后, 附上global.h代码

```
#pragma once

#include <windows.h>
#include <iostream>

#define WINDOW_WIDTH  800
#define WINDOW_HEIGHT 600
#define WORLD_WIDTH 30
#define WORLD_HEIGHT 20
#define CELL_SIZE 20

```

程序还有一些地方需要改进, 将在下次进行


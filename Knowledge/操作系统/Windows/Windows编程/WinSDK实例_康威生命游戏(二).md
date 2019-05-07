# WinSDK实例_康威生命游戏(二)
### **目标**
1, 增加地图编辑功能, 在暂停模式下点击地图, 会生成/销毁一个细胞
2, 增加读取存档功能, 如下图为读取了一个[高斯帕滑翔机枪]的存档
![这里写图片描述](http://img.blog.csdn.net/20170710210212855?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzIxODkwNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

3, 追加设置界面, 如下图
![这里写图片描述](http://img.blog.csdn.net/20170710210012947?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzIxODkwNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

### **继承CWorld类, 增加描画功能**
增加CWorldController类, 继承CWorld
CWorld类只进行数据运算和保存
CWorldController类在CWorld的基础上增加在Windows下的描画

CWorldController声明如下:

```
//世界管理器, 在CWorld类上增加描画方法
class CWorldController : public CWorld
{
private:
	int m_cell_size;
	void CleanWorld(HDC hdc);
	void DrawGrid(HDC hdc);
	void DrawCell(HDC hdc);
public:
	CWorldController(int width, int height, int cell_size) : CWorld(width, height) { m_cell_size = cell_size; };
	~CWorldController() { ; };
	int GetCellSize() { return m_cell_size; };

	void DrawWorld(HDC hdc);
	int  GetCellIndexFromScreenPos(int x, int y, int* i, int* j);
	void GetWorldInfo(int* width, int* height, int* cell_size) 
		{ *width = GetWidth(); *height = GetHeight(); *cell_size = m_cell_size; };
};
```
### **地图编辑功能**
1, 需要通过鼠标点击的位置找到对应的细胞
故实现了CWorldController类中的GetCellIndexFromScreenPos方法

```
//通过屏幕坐标找到此坐标的细胞
//返回值: 
//	-1-失败 0-成功
int CWorldController::GetCellIndexFromScreenPos(int x, int y, int* i, int* j)
{
	*i = x / m_cell_size;
	*j = y / m_cell_size;
	if (*i >= GetWidth() || *j >= GetHeight() ||
		*i < 0 || *j < 0)
	{
		return -1;
	}
	else
	{
		return 0;
	}
}
```
2, 修改细胞存活属性, 并重绘
在主界面的消息回调中增加如下代码
```
case WM_LBUTTONDOWN:	//鼠标左键按下
	{
		int x = LOWORD(lParam);
		int y = HIWORD(lParam);
		int i = 0;
		int j = 0;
		if (g_world_ctrl->GetCellIndexFromScreenPos(x, y, &i, &j) < 0)
		{	//点击的坐标不在任何细胞上, 不做任何操作
			return 0;
		}
		g_world_ctrl->setCellAlive(i, j, 1 ^ g_world_ctrl->getCellAlive(i, j));
		g_world_ctrl->DrawWorld(GetDC(hwnd));
	}
	break;
```
### **地图存储功能**
1, 地图文件的定义
所有的地图均为json格式, 存储地图的宽高, 细胞尺寸和具体地图信息, 如下所示(一个脉冲星的地图)

```
{
	"Map Head":	{
		"width":	30,
		"height":	20,
		"cell size":	20
	},
	"Map Data":	{
		"line 0":	"0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0",
		"line 1":	"0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0",
		"line 2":	"0:0:0:0:0:0:0:0:0:0:0:0:0:1:1:0:0:0:0:0:1:1:0:0:0:0:0:0:0:0",
		"line 3":	"0:0:0:0:0:0:0:0:0:0:0:0:0:0:1:1:0:0:0:1:1:0:0:0:0:0:0:0:0:0",
		"line 4":	"0:0:0:0:0:0:0:0:0:0:0:1:0:0:1:0:1:0:1:0:1:0:0:1:0:0:0:0:0:0",
		"line 5":	"0:0:0:0:0:0:0:0:0:0:0:1:1:1:0:1:1:0:1:1:0:1:1:1:0:0:0:0:0:0",
		"line 6":	"0:0:0:0:0:0:0:0:0:0:0:0:1:0:1:0:1:0:1:0:1:0:1:0:0:0:0:0:0:0",
		"line 7":	"0:0:0:0:0:0:0:0:0:0:0:0:0:1:1:1:0:0:0:1:1:1:0:0:0:0:0:0:0:0",
		"line 8":	"0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0",
		"line 9":	"0:0:0:0:0:0:0:0:0:0:0:0:0:1:1:1:0:0:0:1:1:1:0:0:0:0:0:0:0:0",
		"line 10":	"0:0:0:0:0:0:0:0:0:0:0:0:1:0:1:0:1:0:1:0:1:0:1:0:0:0:0:0:0:0",
		"line 11":	"0:0:0:0:0:0:0:0:0:0:0:1:1:1:0:1:1:0:1:1:0:1:1:1:0:0:0:0:0:0",
		"line 12":	"0:0:0:0:0:0:0:0:0:0:0:1:0:0:1:0:1:0:1:0:1:0:0:1:0:0:0:0:0:0",
		"line 13":	"0:0:0:0:0:0:0:0:0:0:0:0:0:0:1:1:0:0:0:1:1:0:0:0:0:0:0:0:0:0",
		"line 14":	"0:0:0:0:0:0:0:0:0:0:0:0:0:1:1:0:0:0:0:0:1:1:0:0:0:0:0:0:0:0",
		"line 15":	"0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0",
		"line 16":	"0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0",
		"line 17":	"0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0",
		"line 18":	"0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0",
		"line 19":	"0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0"
	}
}
```
2, 创建CMapController类对地图进行控制

```
class CMapController
{
public:
	CWorldController* ReadMapFile(string filePath);
	int SaveMapFile(CWorldController* worldCtrl, string filePath);
	CWorldController* CreateWorldCtrlByMap(const string& mapJsonStr);	//根据地图信息创建一个世界管理器
	BOOL GetLoadFilePathByFileBrowser(HWND hwnd, string& filePath);		//从文件浏览器中获取文件名, 用于加载地图
	BOOL GetSaveFilePathByFileBrowser(HWND hwnd, string& filePath);		//从文件浏览器中获取文件名, 用于保存地图
private:
	int WorldData2Json(CWorldController* worldCtrl, string& outStr);	//将世界管理器中信息转化为地图json串
	void initOpenFileName(OPENFILENAME& ofn);

};
```
地图中的json数据的生成使用CJson.
详见http://blog.csdn.net/u013218907/article/details/51702947


### **设置界面封装**
由于不打算使用MFC, 所以只能自己造轮子, 重新写界面相关的方法
对于设置界面, 主要需要如下五个方法:
1, 注册

```
void OptionWinRegister(HINSTANCE hInstance);
```

2, 创建

```
int OptionWinCreate(HINSTANCE hInstance);
```

3, 显示

```
void OptionWinShow(void);	//显示设置窗口

```

4, 隐藏

```
void OptionWinHide(void);	//隐藏设置窗口
```

5, 初始化界面参数

```
//将数据放入编辑框内
void OptionSetInfo(int world_w, int world_h, int cell_size, int turn_time);
```
具体实现中只是对基本windows API进行了封装, 不再展示

[代码下载](http://download.csdn.net/download/u013218907/9894417)





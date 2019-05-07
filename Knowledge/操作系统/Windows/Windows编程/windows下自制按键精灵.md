# windows下自制按键精灵

具体可参见附件中的代码压缩包
主要代码如下
```C++

// QuickMarcoDlg.h : 头文件
//

#pragma once
#include <list>
#include "afxwin.h"
using namespace std;

typedef enum 
{	//命令头, 按键, 鼠标左键, 或是鼠标右键
	CMD_KEY,
	CMD_LBUTTON,
	CMD_RBUTTON,
} CmdHead;

typedef union
{	//鼠标位置 或 键盘键值
	POINT mousePoint;
	TCHAR key;
} CmdContent;


typedef struct
{
	CmdHead cmdHead;
	CmdContent cmdContent;
} MyCmd, *pMyCmd;

// CQuickMarcoDlg 对话框
class CQuickMarcoDlg : public CDialog
{
// 构造
public:
	CQuickMarcoDlg(CWnd* pParent = NULL);	// 标准构造函数

// 对话框数据
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_QUICKMARCO_DIALOG };
#endif

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV 支持


// 实现
protected:
	HICON m_hIcon;

	// 生成的消息映射函数
	virtual BOOL OnInitDialog();
	afx_msg void OnPaint();
	afx_msg void OnCancel();
	afx_msg HCURSOR OnQueryDragIcon();
	DECLARE_MESSAGE_MAP()
	

private:
	ATOM HotKeyMousePointID;
	ATOM HotKeyExecID;
	void OnHotKey(WPARAM wParam);
	void UpdateCmdListUI();
//public:
	virtual BOOL PreTranslateMessage(MSG* pMsg);
	list<pMyCmd> m_CmdList;	//命令链表
	afx_msg void OnBnClickedClean();
	CListBox m_CmdListBox;
	CStatic m_Tips;
	afx_msg void OnBnClickedLbutton();
	CEdit m_XPos;
	CEdit m_YPos;
	void ShowRGB(POINT point);
public:
	afx_msg void OnBnClickedRbutton();
	afx_msg void OnBnClickedKey();
	CEdit m_Key;
	afx_msg void OnBnClickedExecute();
	CStatic m_RGB;
};

```


```C++

// QuickMarcoDlg.cpp : 实现文件
//

#include "stdafx.h"
#include "QuickMarco.h"
#include "QuickMarcoDlg.h"
#include "afxdialogex.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CQuickMarcoDlg 对话框



CQuickMarcoDlg::CQuickMarcoDlg(CWnd* pParent /*=NULL*/)
	: CDialog(IDD_QUICKMARCO_DIALOG, pParent)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CQuickMarcoDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	DDX_Control(pDX, IDC_CMD_LIST, m_CmdListBox);
	DDX_Control(pDX, IDC_TIPS, m_Tips);
	DDX_Control(pDX, IDC_X, m_XPos);
	DDX_Control(pDX, IDC_Y, m_YPos);
	DDX_Control(pDX, IDC_EDIT3, m_Key);
	DDX_Control(pDX, IDC_RGB, m_RGB);
}

BEGIN_MESSAGE_MAP(CQuickMarcoDlg, CDialog)
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDC_CLEAN, &CQuickMarcoDlg::OnBnClickedClean)
	ON_BN_CLICKED(IDC_LBUTTON, &CQuickMarcoDlg::OnBnClickedLbutton)
	ON_BN_CLICKED(IDC_RButton, &CQuickMarcoDlg::OnBnClickedRbutton)
	ON_BN_CLICKED(IDC_KEY, &CQuickMarcoDlg::OnBnClickedKey)
	ON_BN_CLICKED(IDC_EXECUTE, &CQuickMarcoDlg::OnBnClickedExecute)
END_MESSAGE_MAP()


// CQuickMarcoDlg 消息处理程序

BOOL CQuickMarcoDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// 设置此对话框的图标。  当应用程序主窗口不是对话框时，框架将自动
	//  执行此操作
	SetIcon(m_hIcon, TRUE);			// 设置大图标
	SetIcon(m_hIcon, FALSE);		// 设置小图标

	// TODO: 在此添加额外的初始化代码
	//注册系统级快捷键F6和F8
	HotKeyMousePointID = GlobalAddAtom(_T("getMousePoint")) - 0xC00;	//获得唯一ID()
	if (!RegisterHotKey(this->GetSafeHwnd(), HotKeyMousePointID, 0, VK_F6))	//定义快捷键F6
	{
		::MessageBox(this->GetSafeHwnd(), _T("注册系统热键F6失败"), _T("Error"), MB_OK);
	}
	else
	{
		//::MessageBox(this->GetSafeHwnd(), _T("注册系统热键F6成功"), _T("Info"), MB_OK);
	}
	HotKeyExecID = GlobalAddAtom(_T("getExeCommand")) - 0xC00;	//获得唯一ID()
	if (!RegisterHotKey(this->GetSafeHwnd(), HotKeyExecID, 0, VK_F8))	//定义快捷键F8
	{
		::MessageBox(this->GetSafeHwnd(), _T("注册系统热键F8失败"), _T("Error"), MB_OK);
	}
	else
	{
		//::MessageBox(this->GetSafeHwnd(), _T("注册系统热键F8成功"), _T("Info"), MB_OK);
	}

	return TRUE;  // 除非将焦点设置到控件，否则返回 TRUE
}

// 如果向对话框添加最小化按钮，则需要下面的代码
//  来绘制该图标。  对于使用文档/视图模型的 MFC 应用程序，
//  这将由框架自动完成。

void CQuickMarcoDlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // 用于绘制的设备上下文

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// 使图标在工作区矩形中居中
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// 绘制图标
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

//当用户拖动最小化窗口时系统调用此函数取得光标
//显示。
HCURSOR CQuickMarcoDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}

void CQuickMarcoDlg::OnCancel()
{
	UnregisterHotKey(this->GetSafeHwnd(), HotKeyMousePointID);
	UnregisterHotKey(this->GetSafeHwnd(), HotKeyExecID);
	CDialog::OnCancel();
}

//按下F6或F8时的操作
void CQuickMarcoDlg::OnHotKey(WPARAM wParam)
{
	if (wParam == HotKeyMousePointID)
	{
		POINT curPos;
		if (GetCursorPos(&curPos))
		{
			CString tmp;
			tmp.Format(_T("%d"), curPos.x);
			m_XPos.SetWindowTextW(tmp);
			tmp.Format(_T("%d"), curPos.y);
			m_YPos.SetWindowTextW(tmp);
			ShowRGB(curPos);
		}
		else
		{
			::MessageBox(this->GetSafeHwnd(), _T("获取鼠标位置失败"), _T("info"), MB_OK);
		}
	}
	else if (wParam == HotKeyExecID)
	{
		list<pMyCmd>::iterator iter = m_CmdList.begin();
		for (; iter != m_CmdList.end(); iter++)
		{
			pMyCmd tmp = *iter;
			switch (tmp->cmdHead)
			{
			case CMD_KEY:
				//发送键盘按下和按键弹起的消息
				keybd_event(tmp->cmdContent.key, 0, 0, 0);
				keybd_event(tmp->cmdContent.key, 0, KEYEVENTF_KEYUP, 0);
				break;
			case CMD_LBUTTON:
				SetCursorPos(tmp->cmdContent.mousePoint.x, tmp->cmdContent.mousePoint.y);
				mouse_event(MOUSEEVENTF_LEFTDOWN, 
					tmp->cmdContent.mousePoint.x, tmp->cmdContent.mousePoint.y, 0, 0);
				mouse_event(MOUSEEVENTF_LEFTUP,
					tmp->cmdContent.mousePoint.x, tmp->cmdContent.mousePoint.y, 0, 0);
				break;
			case CMD_RBUTTON:
				SetCursorPos(tmp->cmdContent.mousePoint.x, tmp->cmdContent.mousePoint.y);
				mouse_event(MOUSEEVENTF_RIGHTDOWN,
					tmp->cmdContent.mousePoint.x, tmp->cmdContent.mousePoint.y, 0, 0);
				mouse_event(MOUSEEVENTF_RIGHTUP,
					tmp->cmdContent.mousePoint.x, tmp->cmdContent.mousePoint.y, 0, 0);
				break;
			default:
				break;
			}
		}
	}

	return;
}


BOOL CQuickMarcoDlg::PreTranslateMessage(MSG* pMsg)
{
	// TODO: 在此添加专用代码和/或调用基类
	if (pMsg->message == WM_HOTKEY)
	{
		//::MessageBox(this->GetSafeHwnd(), _T("hahaha"), _T("HAHAH"), MB_OK);
		OnHotKey(pMsg->wParam);
	}


	return CDialog::PreTranslateMessage(pMsg);
}

//清空按钮点击回调
void CQuickMarcoDlg::OnBnClickedClean()
{
	// TODO: 在此添加控件通知处理程序代码
	m_CmdList.clear();
	m_CmdListBox.ResetContent();
	m_Tips.SetWindowText(_T("请按F6进行鼠标位置捕获,或按下F8进行指令集运行"));

}

//插入鼠标左键消息
void CQuickMarcoDlg::OnBnClickedLbutton()
{
	// TODO: 在此添加控件通知处理程序代码
	CString temp;
	temp.Empty();
	m_XPos.GetWindowText(temp);
	int x = _ttoi(temp);
	temp.Empty();
	m_YPos.GetWindowText(temp);
	int y = _ttoi(temp);
	if (x && y)
	{
		pMyCmd tmp = new MyCmd();
		tmp->cmdHead = CMD_LBUTTON;
		tmp->cmdContent.mousePoint.x = x;
		tmp->cmdContent.mousePoint.y = y;
		m_CmdList.push_back(tmp);
		UpdateCmdListUI();
	}
	else
	{
		::MessageBox(this->GetSafeHwnd(), _T("请先设置鼠标坐标"), _T("Info"), MB_OK);
	}
}

void CQuickMarcoDlg::OnBnClickedRbutton()
{
	// TODO: 在此添加控件通知处理程序代码
	CString temp;
	temp.Empty();
	m_XPos.GetWindowText(temp);
	int x = _ttoi(temp);
	temp.Empty();
	m_YPos.GetWindowText(temp);
	int y = _ttoi(temp);
	if (x && y)
	{
		pMyCmd tmp = new MyCmd();
		tmp->cmdHead = CMD_RBUTTON;
		tmp->cmdContent.mousePoint.x = x;
		tmp->cmdContent.mousePoint.y = y;
		m_CmdList.push_back(tmp);
		UpdateCmdListUI();
	}
	else
	{
		::MessageBox(this->GetSafeHwnd(), _T("请先设置鼠标坐标"), _T("Info"), MB_OK);
	}
}


void CQuickMarcoDlg::OnBnClickedKey()
{
	// TODO: 在此添加控件通知处理程序代码
	CString temp;
	temp.Empty();
	m_Key.GetWindowText(temp);
	temp.MakeUpper();
	WCHAR vk = temp.GetAt(0);
	if (vk)
	{
		pMyCmd tmp = new MyCmd();
		tmp->cmdHead = CMD_KEY;
		tmp->cmdContent.key = vk;	//英文字母的VK值等于大写ASCII的值
		m_CmdList.push_back(tmp);
		UpdateCmdListUI();
	}
	else
	{
		::MessageBox(this->GetSafeHwnd(), _T("输入的键盘按键有误"), _T("Info"), MB_OK);
	}
}

void CQuickMarcoDlg::UpdateCmdListUI()
{
	CString tips;
	tips.Format(_T("当前存储了 %d条命令"), m_CmdList.size());
	m_Tips.SetWindowTextW(tips);

	m_CmdListBox.ResetContent();

	list<pMyCmd>::iterator iter = m_CmdList.begin();
	for (; iter != m_CmdList.end(); iter++)
	{
		pMyCmd tmp = *iter;
		CString listinfo;
		listinfo.Empty();
		switch (tmp->cmdHead)
		{
		case CMD_KEY:
			listinfo.Format(_T("按键 - %c"), tmp->cmdContent.key);
			break;
		case CMD_LBUTTON:
			listinfo.Format(_T("在坐标X = %d, Y = %d 处点击鼠标左键"), 
					tmp->cmdContent.mousePoint.x, tmp->cmdContent.mousePoint.y);
			break;
		case CMD_RBUTTON:
			listinfo.Format(_T("在坐标X = %d, Y = %d 处点击鼠标右键"),
				tmp->cmdContent.mousePoint.x, tmp->cmdContent.mousePoint.y);
			break;
		default:
			break;
		}
		m_CmdListBox.AddString(listinfo);
	}
	//定位到最后一行
	m_CmdListBox.SetCurSel(m_CmdListBox.GetCount() - 1);
}


void CQuickMarcoDlg::OnBnClickedExecute()
{
	// TODO: 在此添加控件通知处理程序代码
	OnHotKey(HotKeyExecID);
}

void CQuickMarcoDlg::ShowRGB(POINT point)
{
	HDC displayDC = CreateDC(_T("DISPLAY"), NULL, NULL, NULL);
	DWORD colorRef = GetPixel(displayDC, point.x, point.y);
	DeleteDC(displayDC);

	CString tmp;
	tmp.Empty();
	tmp.Format(_T("color = %d, R =  %d, G = %d, B = %d"), colorRef, 
		colorRef & 0xff, (colorRef>>8) & 0xff, (colorRef >> 16) & 0xff);
	m_RGB.SetWindowTextW(tmp);
}


```
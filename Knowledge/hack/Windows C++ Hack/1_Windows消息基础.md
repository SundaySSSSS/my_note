# 1_Windows消息基础

## windows消息基础示例
打开, 关闭记事本
修改记事本标题, 获取记事本标题
```C++
void CWinMsgDlg::OnBnClickedBtnOpenNotepad()
{
	WinExec("notepad.exe", SW_SHOW);
}

void CWinMsgDlg::OnBnClickedBtnCloseNotepad()
{
	HWND hWnd = ::FindWindow(L"Notepad", NULL);
	if (hWnd == NULL)
	{
		AfxMessageBox(L"没有找到记事本");
		return;
	}
	::SendMessage(hWnd, WM_CLOSE, NULL, NULL);
}

void CWinMsgDlg::OnBnClickedBtnModifyTitle()
{
	HWND hWnd = ::FindWindow(NULL, L"无标题 - 记事本");
	if (hWnd == NULL)
	{
		AfxMessageBox(L"没有找到记事本");
		return;
	}
	wchar_t *pCaptionText = L"消息测试";
	::SendMessage(hWnd, WM_SETTEXT, (WPARAM)0, (LPARAM)pCaptionText);
}

void CWinMsgDlg::OnBnClickedBtnGetTitle()
{
	HWND hWnd = ::FindWindow(L"Notepad", NULL);
	if (hWnd == NULL)
	{
		AfxMessageBox(L"没有找到记事本");
		return;
	}
	wchar_t pCaptionText[MAXBYTE] = { 0 };
	::SendMessage(hWnd, WM_GETTEXT, (WPARAM)MAXBYTE, (LPARAM)pCaptionText);
	AfxMessageBox(pCaptionText);
}

```

## 寻找窗口信息的方法
使用VS中的spy++
工具->spy++

## 模拟键盘鼠标操作
如下程序向指定程序(这里是notepad++)发送了一个F5键
```C++
void CWinMsgDlg::OnBnClickedBtnTest()
{
	wchar_t* captionStr = L"C:\\Desktop\\新建文本文档.txt - Notepad++"; //窗口标题

	//找到浏览器窗口
	HWND hWnd = ::FindWindow(NULL, captionStr);
	if (hWnd != NULL)
	{
		::PostMessage(hWnd, WM_KEYDOWN, VK_F5, 1);
		Sleep(50);
		::PostMessage(hWnd, WM_KEYUP, VK_F5, 1);
	}
	else
		AfxMessageBox(L"未找到指定窗口");
}
```

## 通过API的方式模拟键盘鼠标操作
```C++

void CWinMsgDlg::OnBnClickedBtnSimKeyMouse()
{
	wchar_t* captionStr = L"C:\\Desktop\\新建文本文档.txt - Notepad++"; //窗口器标题
	HWND hWnd = ::FindWindow(NULL, captionStr);
	if (hWnd != NULL)
	{
		::SetForegroundWindow(hWnd);	//将焦点给找到的窗体
		keybd_event('A', 0, 0, 0);
		Sleep(100);
		keybd_event('B', 0, 0, 0);
		Sleep(100);
		keybd_event('C', 0, 0, 0);
		Sleep(100);
		keybd_event('D', 0, 0, 0);
		Sleep(100);
		keybd_event('E', 0, 0, 0);
		Sleep(100);
		keybd_event('F', 0, 0, 0);
		Sleep(100);

		//得到窗口在屏幕上的坐标
		POINT pt = { 0 };
		::ClientToScreen(m_hWnd, &pt);
		//设置鼠标的位置
		SetCursorPos(pt.x + 100, pt.y + 300);
		mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0);
		Sleep(100);
		mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0);
		Sleep(100);
	}
	else
		AfxMessageBox(L"未找到指定窗口");
}
```

## 通过消息实现进程间通信
### 传递数值型数据
发送端:
```C++
#define WM_UMSG (WM_USER + 1)    //自定义消息
//发送消息
void CWinMsgDlg::OnBnClickedBtnMsgComm()
{
	int nNum1 = 1;
	int nNum2 = 2;
	HWND hWnd = ::FindWindow(NULL, L"WinMsg");	//找到目标窗口
	::SendMessage(hWnd, WM_UMSG, (WPARAM)nNum1, (LPARAM)nNum2);
}
```
接收端:
```C++

#define WM_UMSG (WM_USER + 1)

BEGIN_MESSAGE_MAP(CWinMsgDlg, CDialogEx)
	ON_WM_PAINT()
	ON_MESSAGE(WM_UMSG, &CWinMsgDlg::RecvMsg) //<-注册消息
END_MESSAGE_MAP()


//接收消息
LRESULT CWinMsgDlg::RecvMsg(WPARAM wParam, LPARAM lParam)
{
	int nNum1 = static_cast<int>(wParam);
	int nNum2 = static_cast<int>(lParam);
	int sum = nNum1 + nNum2;
	CString str;
	str.Format(L"%d", sum);
	AfxMessageBox(str);
	return 0;
}
```

## 传递字符串型的短消息
发送端:
```C++
//发送消息
void CWinMsgDlg::OnBnClickedBtnMsgComm()
{
	int nNum1 = 1;
	int nNum2 = 2;
	HWND hWnd = ::FindWindow(NULL, L"WinMsg");	//找到目标窗口

	CString strText = L"发送字符串测试";

	//填充COPYDATASTRUCT结构体
	COPYDATASTRUCT cds;
	cds.dwData = 0;
	cds.cbData = CStringA(strText).GetLength();
	cds.lpData = strText.GetBuffer(cds.cbData);
	//m_hWnd为发送窗口的成员(CWnd的成员)
	::SendMessage(hWnd, WM_COPYDATA, (WPARAM)m_hWnd, (LPARAM)&cds);
}
```

接收端:
1, 在类向导中创建响应WM_COPYDATA的消息响应函数
2, 加入如下代码
```C++
BOOL CWinMsgDlg::OnCopyData(CWnd* pWnd, COPYDATASTRUCT* pCopyDataStruct)
{
	DWORD dwPid = 0;
	::GetWindowThreadProcessId(pWnd->m_hWnd, &dwPid);

	CString strText;
	strText.Format(L"PID = %d : %s", dwPid, pCopyDataStruct->lpData);
	AfxMessageBox(strText);

	return CDialogEx::OnCopyData(pWnd, pCopyDataStruct);
}
```

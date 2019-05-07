# MFC对话框使用标签页控件

```
MFC对话框使用标签页控件

1、使用VS2008创建一个MFC对话框。
2、在主对话框资源上添加一个标签页控件Tab Control，关联一个变量CTabCtrl m_myTablCtrl;
3、创建两个对话框资源，属性设置：
Border:    none   // 边界为空
Style:     Child  //子窗口
4、为这两个对话框关联两个对话框类。
5、在主对话框类添加两个子对话框对象成员。
[cpp] view plain copy
       CDialog1 m_dlg1;  
CDialog2 m_dlg2;  
  
CDialog * m_paDlg[2];  
int m_nCurTab;  
6、在主对话框的OnInitDialog()函数中添加
//添加标签
[cpp] view plain copy
m_myTablCtrl.InsertItem(0, _T("中国"));  
lCtrl.InsertItem(1, _T("日本"));  
//创建子对话框窗口
[cpp] view plain copy
m_dlg1.Create(IDD_DIALOG1,&m_myTablCtrl);  
m_dlg2.Create(IDD_DIALOG2,&m_myTablCtrl);  
  
m_paDlg[0] = &m_dlg1;  
m_paDlg[1] = &m_dlg2;  
//设置子对话框窗口的位置
[cpp] view plain copy
CRect rc;     
m_myTablCtrl.GetClientRect(&rc);  
rc.top  += 23;    
rc.left  += 3;  
rc.bottom -= 3;     
rc.right -= 3;  
  
m_dlg1.MoveWindow(&rc);  
m_dlg2.MoveWindow(&rc);  
//显示一个子对话框窗口
[cpp] view plain copy
m_dlg1.ShowWindow(SW_SHOW);     
m_myTablCtrl.SetCurSel(0);  
7、添加标签页控件的切换标签响应函数
[cpp] view plain copy
void CpageDlg::OnTcnSelchangeTab1(NMHDR *pNMHDR, LRESULT *pResult)  
{
    // TODO: 在此添加控件通知处理程序代码
    *pResult = 0;

    int nNewSel = m_myTablCtrl.GetCurSel();

    if (m_nCurTab != nNewSel)
    {
        m_paDlg[m_nCurTab]->ShowWindow(SW_HIDE);
        m_paDlg[nNewSel]->ShowWindow(SW_SHOW);
        m_nCurTab = nNewSel;
    }
    return;
}

8、在子对话框窗口上添加编辑框，并关联一个对象。在主对话框窗口上添加一个按钮，并添加消息响应函数。
[cpp] view plain copy
void CpageDlg::OnBnClickedButton1()  
{  
    // TODO: 在此添加控件通知处理程序代码  
    CString str;  
    m_dlg1.m_edit.GetWindowText(str);  
    str+=_T("中aA1");  
    m_dlg1.m_edit.SetWindowText(str);  
}  
 
总结：
标签页控件主要是让多个界面切换显示。界面设置，按原有的一样
```


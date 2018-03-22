# [MFC]定时器

```
#define TRAFFIC_TIMER 1

初始化为1秒调用一次
SetTimer(TRAFFIC_TIMER, 1000, 0);

void CTrafficLightToolDlg::OnTimer(UINT_PTR nIDEvent)
{
	if (nIDEvent == TRAFFIC_TIMER)
	{
		//定时器被触发
	}
	CDialog::OnTimer(nIDEvent);
}

//销毁
KillTimer(TRAFFIC_TIMER);


```

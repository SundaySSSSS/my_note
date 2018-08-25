# C#线程控制界面控件

如果创建控件的线程之外的其他线程试图访问该控件, 则系统会抛出InvalidOperationException异常
解决方法有:

1,  禁用此警告

``` C#
Control.CheckForIllegalCrossThreadCalls = false;
```

2,  可以利用委托(Delegate)和事件(Event)解决此问题

例如:
一个让界面中listBox显示一条记录的函数

```C#
private delegate void showMsgDelegate(string msg);

private void showMsg(string msg)
{
    if (listBoxMsg.InvokeRequired)    //返回true说明当前线程和控件所在线程不同
    {
        showMsgDelegate d = showMsg;
        listBoxMsg.Invoke(d, msg);
    }
    else
    {
        listBoxMsg.Items.Add(msg + "\r\n");
    }
}
```



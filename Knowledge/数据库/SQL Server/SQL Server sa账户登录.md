# SQL Server sa账户登录

1.安全性 -> 登录名 -> sa（双击或者右击选“属性”），左栏“常规”里面修改密码，“状态”里面“登录”下面选择启用，然后“确定”。

2.右单击“服务器”（就是数据库上面的那个, 树形结构的根）选择“属性”，找到“安全性”选择SQL于Windows混合模式，确定退出。

3.再右单击“服务器”选择“重新启动”。
这样以后你就可以退出来重新用sa登录了。
from tkinter import *

root = Tk()

#用表格的方式布局控件
Label(root, text = "账户：").grid(row = 0, column = 0)
Label(root, text = "密码：").grid(row = 1, column = 0)

e1 = Entry(root)

def m_test():
    if e2.get() == "good":
        print("OK")
        return True
    else:
        print("NG")
        e2.delete(0, END)
        return False

def m_invalid():
    print("try again!")
       
#密码输入框要求显示*，并且必须为good,当失去焦点时进行验证,验证函数注册在validatecommand里
#validatecommand为False时，会调用invalidcommand
e2 = Entry(root, show = "*", validate = "focusout",
           validatecommand = m_test, invalidcommand = m_invalid)
e1.grid(row = 0, column = 1, padx = 10, pady = 5)
e2.grid(row = 1, column = 1, padx = 10, pady = 5)

def m_show():
    print("账户：%s" % e1.get())
    print("密码：%s" % e2.get())

Button(root, text = "确认", width = 10, command = m_show)\
             .grid(row = 3, column = 0, sticky = W, padx = 10, pady = 5)
#quit方法要想正常退出，需要双击打开py文件，在IDE里启动不好使
Button(root, text = "退出", width = 10, command = root.quit)\
             .grid(row = 3, column = 1, sticky = E, padx = 10, pady = 5)

mainloop()

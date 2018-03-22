from tkinter import *

root = Tk()

root.title("这个周末去干啥？")
Options = ["去沙漠滑冰", "去火星度假", "在海底遛狗","洗洗睡吧。。。"]
#记录到底选了什么
selected = []

for opt in Options:
    #创建一个变量用于存储用户的选择
    selected.append(IntVar())
    #创建多选按钮
    temp = Checkbutton(root, text = opt, variable = selected[-1])
    #挂在最左边（用WESN表示上下左右（东南西北））
    temp.pack(anchor = W)

def m_callback():
    for sel in selected:
        print(sel.get())
        

mButton = Button(root, text = "决定就是你了！", command = m_callback)
mButton.pack()

mainloop()

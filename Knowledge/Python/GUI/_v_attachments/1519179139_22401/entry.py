from tkinter import *

root = Tk()

e = Entry(root)
e.pack(padx = 20, pady = 20)

#清空
e.delete(0, END)
#插入默认文本
e.insert(0,"defaults")



mainloop()

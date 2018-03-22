from tkinter import *

root = Tk()

w = Canvas(root, width = 200, height = 200)
w.pack()

#红色虚线
line1 = w.create_line(0, 100, 200, 100, fill = "red", dash = (4, 4))
#黄色竖线
line2 = w.create_line(100, 0, 100, 200, fill = "yellow")
#蓝色正方形
rect1 = w.create_rectangle(50, 50, 150, 150, fill = "blue")

#改变坐标
w.coords(line1, 0 , 50, 200, 50)
#改变设定
w.itemconfig(rect1, fill = 'green')
#删除
w.delete(line2)

Button(root, text = "删除全部", command = (lambda x = ALL:w.delete(x))).pack()

#显示文本
w.create_text(100, 100, text = "text")

mainloop()

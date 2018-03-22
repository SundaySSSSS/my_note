from tkinter import *

root = Tk()

photo = PhotoImage(file = "nuclear.gif")
#compound 让文字显示在图片之上
imgLabel = Label(root, text = "Warning\n!!!!!",
                 justify = LEFT, image = photo,
                 compound = CENTER, font = ("微软雅黑", 20),
                 fg = "yellow")
imgLabel.pack()

mainloop()

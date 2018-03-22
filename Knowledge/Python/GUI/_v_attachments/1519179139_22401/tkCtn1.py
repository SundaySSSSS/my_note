from tkinter import *

def m_callback():
    var.set("Run!Quick!")
    

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set("Warning! \nnuclear weapon detected!")

textLabel = Label(frame1, textvariable = var,
                  justify = LEFT,
                  padx = 10)
textLabel.pack(side = LEFT)

#不支持jpg格式。。。
photo = PhotoImage(file = "nuclear.gif")
imgLabel = Label(frame1, image = photo)
imgLabel.pack(side = RIGHT)

mButton = Button(frame2, text = "Help!", command = m_callback)
mButton.pack()

frame1.pack(padx = 10, pady = 10)
frame2.pack(padx = 10, pady = 10)


mainloop()

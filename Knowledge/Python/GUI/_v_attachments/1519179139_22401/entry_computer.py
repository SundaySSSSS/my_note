from tkinter import *

master = Tk()

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

def test(content):
    return content.isdigit()
        

testCMD = master.register(test)
e1 = Entry(master, textvariable = v1, validate = "key", \
           validatecommand = (testCMD, '%P')).grid(row = 0, column = 0)

Label(master, text = "+").grid(row = 0, column = 1)

e1 = Entry(master, textvariable = v2, validate = "key", \
           validatecommand = (testCMD, '%P')).grid(row = 0, column = 2)

Label(master, text = "=").grid(row = 0, column = 3)

e3 = Entry(master, textvariable = v3, state = "readonly").grid(row = 0, column = 4)

def m_calc():
    result = int(v1.get()) + int(v2.get())
    v3.set(str(result))

Button(master, text = "Compute", command = m_calc).grid(row = 1, column = 0)

mainloop()

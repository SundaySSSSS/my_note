import tkinter as tk

class APP:
    def __init__(self, master):
        #一个框架，通常用于给控件分组
        frame = tk.Frame(master)
        #设置对齐方式和边距
        frame.pack(side = tk.LEFT, padx = 10, pady = 10)

        #创建一个按钮，设置文言和前景色, 设置点击按钮后触发的事件
        self.button = tk.Button(frame,text = "say hello", fg = "blue",
                                command = self.say_hello)
        self.button.pack()

    def say_hello(self):
        print("hello world!")
        
root = tk.Tk()
app = APP(root)

root.mainloop()

import tkinter as tk

#top level, root window
app = tk.Tk()
app.title("CXY demo")

mLabel = tk.Label(app,text="this is a label")
#自动调节组件尺寸
mLabel.pack()

app.mainloop()

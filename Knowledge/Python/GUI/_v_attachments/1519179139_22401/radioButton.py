from tkinter import *

root = Tk()

v = IntVar()

#variable一组Radiobutton必须用一个变量，比如选中Two时，v的值就为后面的value的值，即2
Radiobutton(root, text = "One", variable = v, value = 1).pack(anchor = W)
Radiobutton(root, text = "Two", variable = v, value = 2).pack(anchor = W)
Radiobutton(root, text = "Three", variable = v, value = 3).pack(anchor = W)
Radiobutton(root, text = "Four", variable = v, value = 4).pack(anchor = W)

#做一个LabelFrame来存放单选按钮
group = LabelFrame(root, text = "你认为最厉害的人是谁？", padx = 5, pady = 5)
group.pack(padx = 10, pady = 10)

Options = [
    ("超人", 1),
    ("孙悟空", 2),
    ("比尔盖茨", 3),
    ("你自己", 4),
         ]

v = IntVar()
v.set(1)

#indicatoron = False使前面不再是小圆圈的形式，fill = X为横向填充
for name, num in Options:
    b = Radiobutton(group, text = name, variable = v, value = num, indicatoron = False)
    b.pack(fill = X)
    
mainloop()

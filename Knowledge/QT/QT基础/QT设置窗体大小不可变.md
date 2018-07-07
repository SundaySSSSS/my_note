# QT设置窗体大小不可变

方法1, 在窗体的构造函数中添加如下代码
```C++
setFixedSize(this->width(), this->height()); 
```

方法2, 设置窗体的最大和最小宽度一致。
在窗体属性的minimumSize和maximumSize处设置
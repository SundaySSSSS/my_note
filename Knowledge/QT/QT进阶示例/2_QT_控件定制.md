# QT_控件定制
此示例在上一个示例的基础上完成
## 按钮的定制示例
在按钮上右键->改变样式表...
加入如下qss(语法类似css)
``` CSS
QPushButton
{
    border:none;
	  background-color: rgb(172, 34, 27);
    border-top-right-radius:5pt;
}
QPushButton:hover
{
    background-color: rgb(252, 1, 7);
}
QPushButton:pressed
{
    background-color: rgb(128, 0, 2);
}
```
其中
hover表示鼠标放悬浮在按钮上时
pressed表示按下时
border-top-right-radius:5pt;表示右上角设置为圆角

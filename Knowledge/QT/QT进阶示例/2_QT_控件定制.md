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
    border-top-right-radius:5px;
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

## 关于最大化的问题
### 最大化失败
最外层需要有一个布局
如果没布局, 内部带阴影的Widget不会随着整体窗体变大而变化

### 最大化,再恢复后阴影消失
解决方案:
在最大化时取消margin
`this->ui->vlMain->setMargin(0)`
恢复后复原margin
`this->ui->vlMain->setMargin(9)`
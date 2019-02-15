# QDialog添加最大最小按钮

``` C++
Qt::WindowFlags flags = Qt::Dialog;
flags |=Qt::WindowMinMaxButtonsHint;
flags |=Qt::WindowCloseButtonHint;
setWindowFlags(flags);
```

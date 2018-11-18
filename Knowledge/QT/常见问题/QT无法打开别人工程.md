# QT无法打开别人工程


打不开其他人的 工程。
```
Could not find qmake configuration file default. 
分析文件E:/QPlot/QPlot.pro时发生错误，放弃中。 
(Error while parsing file /*.pro. Giving up.)
```
解决方案：

`I assume it will work as you expect if you go to “Tools” -> “Options…” -> “Build & Run” -> “Kits” and make a Qt-5-based kit the default. `
（选择auto-detected的那个kits，点击按键“make default”即可。）


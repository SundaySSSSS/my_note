# QT个性化颜色配置
测试环境Qt5.5.1 mingw

工具->选项->文本编辑器->通用高亮器
在此界面中，有“语法高亮定义文件”路径和备用路径， 例如：
`C:\Users\root\AppData\Roaming\QtProject\qtcreator\generic-highlighter`
和
`C:\Qt\Qt5.5.1\Tools\QtCreator\share\qtcreator\generic-highlighter`
在这两个目录上，退一级，找到styles文件夹， 把dark_copy.xml(附件中）拷贝到styles目录中（一般拷贝到路径中后退一级的styles中就行）
重启QT可以在字体颜色中找到Dark_cxy的配色方案

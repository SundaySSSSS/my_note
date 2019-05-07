# gedit乱码问题

运行dconf-editor
如果没有, 先`apt-get install dconf-editor`
展开/org/gnome/gedit/preferences/encodings
在candidate-encodings的Value中加入['GB18030', 'UTF-8', 'CURRENT', 'ISO-8859-15', 'UTF-16']

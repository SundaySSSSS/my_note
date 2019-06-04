# emacs使用中文输入法
最简单的就是直接在命令窗口输入：

`LC_CTYPE="zh_CN.utf8";emacs`

或者(使用了这个方法, 好使)
>> 编辑`/etc/environment`文件。

`sudo gedit /etc/environment`

>> 在后面加上，
`LC_CTYPE="zh_CN.utf8"`

>> 保存，重启计算机，然后更改输入法激活快捷键，比如Shift-Space，因为Ctrl-Space是emacs默认快捷键，然后打开emacs，就可以切换输入法，输入了。


>> 如果计算机没有相关编码，请使用下面方法安装。
```
sudo locale-gen zh_CN.GBK
sudo locale-gen zh_CN.GB2312
sudo locale-gen zh_CN.GB18030
```

```
sudo dpkg-reconfigure locales
sudo locale-gen
```
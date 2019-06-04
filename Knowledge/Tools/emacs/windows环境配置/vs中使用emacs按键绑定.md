# vs中使用emacs按键绑定
VS 2008中自带了emacs风格键绑定，VS 2010时就没了，不过微软仍然以插件的形式提供该功能，到了VS 2012，干脆连这个插件也没了。
好在VS 2010的那个插件改一改还能在VS 2012里继续用。

下载VS 2010的插件：http://visualstudiogallery.msdn.microsoft.com/09dc58c4-6f47-413a-9176-742be7463f92
得到EmacsEmulations.vsix
将扩展名改为zip
解压后编辑其中的文件extension.vsixmanifest
将其中10.0改为11.0
(VS2012是11.0, 如果是VS2013, 需要改为12.0)
保存
然后重新压缩刚才解压得到东西产生EmacsEmulations.zip
（特别注意：一定要确保这个压缩包点开之后就能看到文件extension.vsixmanifest，而不是文件夹EmacsEmulations, 可以选中所有文件, 再压缩, 否则rar会创建一层文件夹）
将扩展名改为vsix
然后执行start EmacsEmulations.vsix
弹出对话框后选择用VS 2012打开
然后，将刚才解开得到的文件夹中的文件Emacs.vsk复制到`...\Microsoft Visual Studio 11.0\Common7\IDE`下。
```
注意, 要区分Program Files和Program Files(x86), VS2013要放到Program Files(x86)里的VS文件夹中!
```
然后启动VS 2012
在TOOLS > Options... > Enviroment > Keyboard > Apply the following additional keyboard mapping scheme中选择Emacs

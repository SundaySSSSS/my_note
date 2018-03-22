# 修改jupyter notebook默认路径
找到jupyter notebook的安装路径
如果是随Anaconda一起安装的, 通常在Anaconda安装目录中的Scripts下
例如
`E:\Anaconda\Scripts`
在命令行中cd到此路径下, 输入
```
jupyter notebook --generate-config
```
会提示jupyter notebook将配置文件生成到哪个目录中了
找到此配置文件, 通常名为
`jupyter_notebook_config.py`
找到此配置文件中的
```
#c.NotebookApp.notebook_dir = ''
```
改为需要的默认路径,并去掉注释 如
```
c.NotebookApp.notebook_dir = 'E:\\MyDocument\\notes\\JupyterNotebook'
```
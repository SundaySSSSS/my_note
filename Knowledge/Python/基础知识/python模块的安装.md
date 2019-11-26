# python模块的安装
## 源码包的安装
通常是下载源码, 例如`beautifulsoup4-4.3.2.tar.gz`
解压之后, 里面会有`setup.py`文件
直接在此目录下`python setup.py install`即可

## whl安装
### 自动安装
下载whl文件后， 在命令行中：
`pip install xxx.whl`

### 手动安装
以requests模块为例, 下载
`requests-2.7.0-py2.py3-none-any.whl`文件
将后缀改为zip
解压缩
将解压出来的`requests-2.7.0.dist-info`和`requests`两个文件夹, 复制到python安装目录的`lib`下即可
## pip安装
比如要安装request模块
直接`pip install requests`即可

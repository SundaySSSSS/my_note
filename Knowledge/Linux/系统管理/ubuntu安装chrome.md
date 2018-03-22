# ubuntu安装chrome
安装谷歌浏览器，只需要三行代码：
打开终端，输入
cd /tmp
对于谷歌Chrome32位版本，使用如下链接：

wget https://dl.google.com/linux/direct/google-chrome-stable_current_i386.deb

对于64位版本可以使用如下链接下载：

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
下载完后，运行如下命令安装。

sudo dpkg -i google-chrome*; sudo apt-get -f install
然后，就可以去搜索使用了。 

但是如果使用root登陆, chrome是无法启动的, 需要进行如下处理:
```
# whereis google-chrome  
google-chrome: /usr/bin/google-chrome /usr/share/man/man1/google-chrome.1.gz  
# vim /usr/bin/google-chrome
```
将 `exec -a "$0" "$HERE/chrome" "$@"`  改为
`exec -a "$0" "$HERE/chrome" "$@" --user-data-dir --no-sandbox`

以后只要 google-chrome 就可以打开Chrome了
# vim插件
## 如何安装插件
### vim-plug
#### 安装vim-plug
使用插件管理器:
推荐使用vim-plug
vim-plug的地址:
`https://github.com/junegunn/vim-plug`
按照官方github上的命令, 在Unix上, 使用如下命令即可:
```
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

在vimrc中加入如下内容
``` vimscript
call plug#begin('~/.vim/plugged')
" 要安装的脚本
call plug#end()
```

#### 使用vim-plug安装插件
以vim-startify插件为例
在github上找到本插件, 在主页上写明了如果使用vim-plug, 则粘贴如下内容到vim-plug配置中即可
```
Plug 'mhinz/vim-startify'
```
在命令模式下执行:
```
:PlugInstall
```
之前添加的Plug就会被自动安装


## 如何搜寻插件
大部分插件都托管到了github上
或者直接google
或者在`https://vimawesome.com`上搜索

## 常用插件
### 美化插件
``` vimscript
" 修改启动界面
mhinz/vim-startify
" 状态栏美化
vim-airline/vim-airline
vim-airline/vim-airline-themes
" 增加代码缩进线
yggdroot/indentline
```

### 配色方案
``` vimscript
w0ng/vim-hybrid
altercation/vim-colors-solarized
morhetz/gruvbox
```
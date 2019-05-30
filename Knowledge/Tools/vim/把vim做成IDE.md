# 把vim做成IDE
## 目录浏览
使用nerdtree插件
https://github.com/scrooloose/nerdtree

``` vimscript
" 设置文件树
" 分别定义定位文件树, 启动文件树, 显示隐藏文件, 文件树忽略文件
nnoremap <leader>v :NERDTreeFind<cr>
nnoremap <leader>g :NERDTreeToggle<cr>
let NERDTreeShowHidden=1
let NERDTreeIgnore = [
    \ '\.git$', '\.DS_Store$' 
    \]
```

## 文件模糊查找
ctrlp插件
https://github.com/ctrlpvim/ctrlp.vim

``` vimscript
" 定义文件搜索插件(Ctrl-P)的快捷键为Ctrl-P
let g:ctrlp_map = '<c-p>'

```

easymotion插件
https://github.com/easymotion/vim-easymotion

## 成对编辑
vim-surround

## 模糊搜索
fzf
https://github.com/junegunn/fzf.vim

在vim-plug中加入如下内容进行安装
``` vimscript
" 多文件模糊搜索插件
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
Plug 'junegunn/fzf.vim'
```
使用
``` vimsrcipt
:Ag 要搜索的内容
```
进行搜索
在搜索结果中使用Ctrl-J和Ctrl-K进行上下移动, 回车跳转

## 搜索替换
``` vimscript
" 多文件搜索替换
Plug 'brooth/far.vim'
```

使用方法:
``` vimscript
:Far a b **/*.py
```
上面语句将a替换为b, 范围是**/*.py
执行后将生成预览, 如果没有问题, 则使用
``` vimscript
:Fardo
```

## go编码插件
https://github.com/fatih/vim-go

## python编码插件
https://github.com/python-mode/python-mode

## 浏览代码
使用tagbar插件
https://github.com/majutsushi/tagbar
tagbar插件依赖于Universal Ctags
在Mac上安装Ctags:
``` shell
brew tap universal-ctags/universal-ctags
brew install --HEAD universal-ctags
```

### 基本用法
启动:
`:TagbarToggle`

## 高亮感兴趣的单词
https://github.com/lfv89/vim-interestingwords
默认使用`<leader>`k来高亮显示当前光标所在的单词
官方说明:
```
Highlight with <Leader>k
Navigate with n and N
Clear highlights with <Leader>K
```


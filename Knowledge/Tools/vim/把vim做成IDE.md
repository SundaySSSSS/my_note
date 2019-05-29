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


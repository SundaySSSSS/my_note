# Vimrc
## Vimrc概述
Vimrc中, rc表示run command
Vimrc有系统级和用户级
系统级vimrc对所有用户都生效, 用户级vimrc仅对当前用户生效

通过`:version`可以看到系统级vimrc和用户vimrc的位置
例如:
```
系统 vimrc 文件: "$VIM/vimrc"
用户 vimrc 文件: "$HOME/.vimrc"
```

vimrc中每一行都是一个命令

让修改的vimrc文件在不关闭vim的情况下生效:
`:source ~/.vimrc`

## 基本语法
### 注释
```
" this is a comment
```

### 设置命令
```
" 显示每一行的行号
set number
" 隐藏行号
set nonumber
```

### map按键映射
``` vimsrcipt
map <F3> i<ul><CR><Space><Space><li></li><CR><Esc>I</ul><Esc>kcit
map <F4> <Esc>i<li></li><Esc>cit
```
上面的配置, 会让按下F3和F4时执行一串操作, 形成前端中经常使用的ul标签和li标签

### let赋值
``` vimscript
let mapleader=","
```

## 常见配置选项
``` vimscript
" 保留1000个历史记录
set history=1000
" 显示当前光标信息
set ruler
" 在查找的时候匹配值会被高亮显示
set hlsearch
" 自动缩进, 上一行有缩进, 另起一行时进行缩进
set autoindent
" 根据语言的语法自动缩进
set smartindent
" 使用空格代替tab
set expandtab
" 启用smart tab
set smarttab
" 让tab等于4个空格
set shiftwidth = 4
set tabstop = 4
```
# spacemacs基础

## 安装
### 最基础的安装方法 - 从github上克隆配置文件
可以在安装完毕emacs后， 直接从github上克隆
```
git clone https://github.com/syl20bnr/spacemacs.git ~/.emacs.d
```
在克隆完成后直接运行 Emacs. 在第一次使用 Spacemacs 时需要下载一些 Package, 然后在 Bootstrap 完成之后你需要进行如下一些配置:

使用哪种编辑方式, 包括 vim 方式(默认) 以及 emacs 方式.
使用哪种 Spacemacs distribution. 包括标准版(默认)以及基础版. 区别在于标准版包含非常多的功能, 而基础版只包含核心功能.
### 让下载加速的方法 - 更换源
在完成以上两个配置之后, 就会在 HOME 目录生成一个 ~/.spacemacs 配置文件. 然后 Spacemacs 会进行进一步的初始化, 下载更多的需要的 Package. 如果你需要使用 emacs-china 的配置源, 此时可以终止 emacs, 然后在`~/.spacemacs` 中的 `dotspacemacs/user-init` 函数中加入以下代码:
```lisp
(setq configuration-layer--elpa-archives
      '(("melpa-cn" . "http://elpa.zilongshanren.com/melpa/")
	("org-cn"   . "http://elpa.zilongshanren.com/org/")
	("gnu-cn"   . "http://elpa.zilongshanren.com/gnu/")))
```

## 


# emacs的搜索
## 使用ag进行多文件搜索
### 1, 安装silversearcher-ag

####Mac OS X 通过 Homebrew 安装
`brew install the_silver_searcher`

#### Ubuntu 下安装
`apt-get install silversearcher-ag`

#### windows下可以从这里下载
`https://github.com/k-takata/the_silver_searcher-win32/releases`
有时会被墙...
下载后, 将ag.exe所在目录放到系统环境变量Path中

### 2, 安装emacs中的helm-ag
在github上的配置中已经包含了安装helm-ag的代码
```lisp
(defvar cxy/packages ...
    helm-ag
    ...)
```

### 3, 修改emacs配置文件
在配置文件中加入快捷键绑定:
(global-set-key (kbd "C-c p s") 'helm-do-ag-project-root)
就可以在项目根目录进行搜索了
`helm-do-ag-project-root`的官方解释为:Call helm-ag at project root. helm-ag seems directory as project root where there is .git or .hg or .svn.

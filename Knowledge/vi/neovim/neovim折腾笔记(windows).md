# neovim折腾笔记(Windows)
## 折腾手顺
### 增加环境变量
这里是： `E:\Develop\nvim-win64\Neovim\bin` 

### 添加配置文件
这里是： `C:\Users\sxiny\AppData\Local\nvim`目录中， 添加自己的配置文件， 名称需要为init.vim

### 安装插件管理器vim-plug
``` cmd
md ~\AppData\Local\nvim\autoload
$uri = 'https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
(New-Object Net.WebClient).DownloadFile(
  $uri,
  $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath(
    "~\AppData\Local\nvim\autoload\plug.vim"
  )
)
```

上面的命令需要在windows powershell中运行

### 下载Universal Ctags
github下载， 解压并添加环境变量

### 下载Ag（the_silver_searcher）
github下载， 解压并添加环境变量

### 下载fzf.exe
github下载， 放到C:\Users\sxiny\.fzf\bin中
# emacs开发环境搭建(ECB)

## 安装emacs
编译emacs前的准备
```
apt-get install libgtk2.0-dev
apt-get install libxpm-dev
apt-get install libjpeg62-dev
apt-get install libgif-dev
apt-get install libtiff5-dev
apt-get install libncurses-dev
```

下载emacs源码
`emacs-24.3.tar.gz`
解压后
```
./configure
make
make install
```

如果正常则不会出错, emacs可以正常启动
如果`./configure`时提示少某些依赖包, 并且进行`apt-get install`后还是提示缺少某些包, 则可以按照提示添加选项`--with-xxx包-no`

## 安装并配置cedet
由于ECB和emacs自带的cedet不兼容, 会出各种错误, 所以直接下载源码包进行安装
下载源码包`cedet-1.1.tar.gz`
解压到`~/.emacs`中(目录可以任意指定, 但在.emacs文件中添加配置时要指定自己的位置)
再`make`
这里可能遇到Makefile文件时间戳的问题, 找到对应Makefile文件, `touch Makefile`即可

在`.emacs`中追加cedet的配置
```
;; Load CEDET
(load-file "~/.emacs.d/cedet-1.1/common/cedet.el")
(semantic-load-enable-code-helpers)
```

## 配置ecb
下载源码包`ecb-2.40.zip`
解压到`~/.emacs`(目录还是任意, 但在.emacs文件中添加配置时要指定自己的位置)
在`.emacs`中追加ecb的配置, 要在刚才cedet配置的后面
```
;; ECB config
(add-to-list 'load-path "~/.emacs.d/ecb-2.40")
(require 'ecb)
```

由于ecb对于cedet的版本支持为[1.0pre6, 1.0.9]
而低版本的cedet安装起来会出现一大堆错误, 故想办法让ecb闭嘴
在解压后的ecb中的`ecb-upgrade.el`文件中, 找到如下代码
```
;; check if vedet-version is correct  
when (or (not (boundp 'cedet-version))  
        (ecb-package-version-list<  
        (ecb-package-version-str2list cedet-version)  
         ecb-required-cedet-version-min)  
        (ecb-package-version-list<  
         ecb-required-cedet-version-max  
         (ecb-package-version-str2list cedet-version)))  
(setq version-error (concat "cedet ["  
                           cedet-required-version-str-min  
                           ", "  
                           cedet-required-version-str-max  
                          "]"))) 
```
将其注释掉(;;是注释)

然后在.emacs文件中追加如下配置:
```
(setq stack-trace-on-error t)
```

## 启动emacs并验证ECB是否正常
启动emacs, 在Tools->Start Code Browser(ECB)
如果不提示错误, 并且emacs被分割为一些小窗口, enjoy it





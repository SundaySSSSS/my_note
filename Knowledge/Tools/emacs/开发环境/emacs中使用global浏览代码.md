# emacs中使用global浏览代码

1， 下载global
linux上直接apt-get即可，但windows上global官网的下载链接国内访问不了，使用附件中的这个旧版本的吧

2， 解压缩， 把其中的bin目录放到windows环境变量中

3， 在emacs中安装ggtags
并加入如下配置

``` lisp
(setenv "PATH" (concat "C:/Users/root/emacs/global/bin;" (getenv "PATH")))
(add-to-list 'exec-path "C:/Users/root/emacs/global/bin")
(add-hook 'c-mode-common-hook
          (lambda ()
            (when (derived-mode-p 'c-mode 'c++-mode 'java-mode)
              (ggtags-mode 1))))

```

其中的目录要换成global中bin目录的位置
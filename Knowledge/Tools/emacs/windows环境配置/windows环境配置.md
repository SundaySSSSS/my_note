# windows环境配置
## 1, 下载并解压
下载emacs并解压（E:\Program Files\emacs 这是我的解压路径）

## 2, 设置系统环境变量
系统环境变量的path变量中增加 E:\Program Files\emacs 和 E:\Program Files\emacs\bin（替换成你的解压路径，如果你解压到C:\Program Files\emacs，你就在path变量中加入一条：C\Program Files\emacs ）。
## 3,修改注册表, 设置主目录
备注： emacs24.x的版本怎么试都不好使， 25版本的没问题
快捷键win+r，在弹出的框中输入regedit，回车后打开了注册表编辑器，找到其中HKEY_LOCAL_MACHINE -> SOFTWARE -> GUN(没有的话右击SOFTWARE->新建->项，并命名为GNU) ->Emacs(没有的话右击GUN->新建->项，并命名为Emacs)->右击Emacs->新建->字符串值, 将新建字符串条目的名称改为HOME，数据改为emacs的主目录【我的为E:\Program Files\emacs\emacs_configuration】）

最后在cmd中运行emacs -nw，查看安装效果。

## 4, 避免卡顿问题
### 方案一, 换字体
emacs25.x的windows版本默认情况下显示中文会非常卡顿
目前只有设置为宋体才能解决
添加:
```lisp
;; windows下只有宋体不卡
(set-default-font "宋体:pixelsize=18:foundry=unknown:weight=medium:slant=normal:width=normal:scalable=true")
```

### 方案二, 根本上修正
在windows上卡顿的本质原因是会频繁的触发垃圾回收, 故进行如下设置
```lisp
;; 设置垃圾回收，在Windows下，emacs25版本会频繁出发垃圾回收，所以需要设置
(when (eq system-type 'windows-nt)
  (setq gc-cons-threshold (* 512 1024 1024))
  (setq gc-cons-percentage 0.5)
  (run-with-idle-timer 5 t #'garbage-collect)
  ;; 显示垃圾回收信息，这个可以作为调试用
  ;; (setq garbage-collection-messages t)
)
```

## 5, 更换等宽字体
将附件中的字体复制到C:\Windows\Font

## 6, 配置ag, 用于文件搜索
将附件中的ag.exe放到任意环境变量路径上

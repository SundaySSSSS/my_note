# 定制emacs

## 定制emacs的基本方法
emacs会读取`.emacs`文件对自身进行配置,
可以通过修改`.emacs`文件来实现对emacs的定制
修改`.emacs`后, 如果不重启emacs, 需要将光标移动到修改处, 使用组合键`C-x C-e`(或者通过`M x eval-current-buffer RETURN`)运行本行LISP代码

定制emacs的方法有:
1, 注册自己写的函数
2, 设置emacs变量(`setq`方法)

## Lisp函数的基本形式
`(function-name arguments)`
例如:
向前移动一个单词的快捷键: `M-f`对应的函数为:
`(forward-word 1)`

## 键盘定制
### emacs键位机制
emacs中的键位映射(keymap)分为"全局键位映射"和"局部键位映射"
每一个mode都有自己的局部键位映射, 例如: 在C mode下, 当用户按下一个按键时, emacs会现在C mode的局部键位映射中查找改按键, 如果没有, 去全局的键位映射中查找
emacs的默认全局键位映射为`global-map`
### 修改键位映射
修改键位映射有如下三个函数
```lisp
(define-key keymap "keystroke" 'command-name)
(global-set-key "keystroke" 'command-name)
(local-set-key "keystroke" 'command-name)
```
上面的`keystroke`可以是一个或者多个字符
例如:
```lisp
(define-key global-map "\C-xl" 'goto-line)
(global-set-key "\C-xl" 'goto-line)
```
上面两句意义相同, 都是将按键`C-x l`绑定到`goto-line`函数上

## 变量
emacs变量分为局部值和默认值
在不同的编辑缓冲区, 局部值可以不同, 如果没有设定某些变量的局部值, 则使用emacs的默认值

### 设置变量的值
设置Emacs变量的基本方法:
```lisp
(setq 变量名 变量的值)    # 设置局部值
(setq-default 变量名 变量的值) # 设置默认值
```
例如:
设置变量`auto-save-interval`的值为800
```lisp
(setq auto-save-interval 800)
```
### 变量的值
#### 布尔值
Emacs lisp中, 真值用"t"来表示, 假用"nil"来表示
但很多情况下, 不是"nil"的任何值, 都可以表示真值

#### 字符串值
必须放在双引号内

#### 字符值
必须以?做前缀, 且不能放到双引号里, 例如:
```lisp
?x ?\C-c
```
上面为`x`和`C-c`的字符值

#### 符号值
以`开头, 后面跟着一个符号名, 例如:
```lisp
'never
```

#### 数据组
```lisp
(x . y)
```
把x和y配对组成一个数据组

## 加载程序包
基本格式:
```lisp
(autoload 'function "filename")
```
例如:
```lisp
(autoload 'ada-mode "ada")
```
意义: 让emacs在第一次调用ada-mode函数的时候加载ada程序包

## 增加mode
```lisp
(setq auto-mode-alist (cons '("\\.a$" . ada-mode) auto-mode-alist))
```
增则表达式`\\.a$`表示所有以
cons的意义目前还不知道






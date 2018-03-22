# LISP基础

## 变量
lisp的变量没有类型, 一个lisp变量可以取任何值

"原子项"是任意类型的值, 可以为:
* 整数: -2^27 ~ 2 ^27 -1 之间的任何数
* 浮点数
* 字符: lisp字符必须带有前导的?, 比如`?a`
* 字符串: 放在一对双引号中间, 特殊字符需要用\做转义
* 布尔值: 真值为t, `nil`表示假. 但大多数情况下非`nil`都表示真
* 符号: 即lisp语言中各种事物的名字, 比如变量名或函数名. 需要用带引号开头
或其他emacs特殊类型, 如编辑缓冲区, 窗口, 进程等

## 函数
### 基本形式
```lisp
(function-name argument1 argument2)
```
包括运算符函数, 例如:
```list
(>= 4 2)
```
### 函数的定义
#### 实例:
```lisp
(defun count-words-buffer ()
    (save-excursion
        (let ((count 0))
            (goto-char (point-min))
            (while (< (point) (point-max))
                (forward-word 1)
                (setq count (1+ count)))
            (message "buffer contains %d words." count))))
```
#### 解释:
##### save-excursion
基本形式:
```lisp
(save-excursion
    statement-block)
```
在语句块中引起的光标移动只在emacs内部执行, 不显示到屏幕上, 且退出该语句块后, 光标恢复到进入前的位置

##### defun
功能: 定义一个函数和他的参数, 返回值为一个符号, 即为定义的函数的名字
在定义函数时可以使用可选参数, 需要在可选参数前添加`&optional`关键字. 如果一个参数是可选的, 且没有赋值, 则取值为`nil`
##### let
基本格式:
```lisp
(let ((var1 value1) (var2 value2) (var3 value3) ...)
    statement-block)
```
功能:
1, 定义一个变量组成的列表
2, 给变量赋初值
3, 创建一个语句块, 语句块内部可以使用`let`定义的变量(相当于局部变量)
let语句块中定义的变量如果和全局变量有冲突, 在let块内, 使用let定义的局部变量
##### goto-char
emacs内部函数, 移动插入点(光标)
##### point point-min point-max
此三个都是emacs内部函数, 
point: 当前插入点位置
point-min: 当前缓冲区的第一个字符的位置
point-max: 当前缓冲区的最后一个字符的位置
##### while
基本形式:
```lisp
(while condition
    statement-block)
```
当`condition`为t时执行, 为`nil`时跳出
##### 1+
`(+1 var-name)`的简写, 对变量+1
##### message
在辅助输入区里显示一条消息, 类似于`printf`
例如:
```lisp
(message "buffer contains %d words." count)
```
%d-整数
%s-字符串或符号
%c-字符
%e-科学计数法表示的浮点数
%f-十进制小数表示的浮点数
%g-用最短字符串表示的浮点数

##### setq
基本形式
```lisp
(setq this var this value
    thatvar thatvalue
    theothervar theothervalue)
```
`setq`的返回值为最后一个赋值, 上例中为`theothervalue`
使用实例:
```lisp
(setq auto-save-interval 800)
```

### 函数文档
直接在函数第一行加入一个双引号包围的字符串即可
此字符串就是用户发来`C-h f`组合键(describe-function)时, 看到的帮助信息
例如:
```lisp
(defun count-words-buffer ()
    "Count the number of words in the current buffer"
    (interactive)
    (save-excursion
        (let ((count 0))
            (goto-char (point-min))
            (while (< (point) (point-max))
                (forward-word 1)
                (setq count (1+ count)))
            (message "buffer contains %d words." count))))
```

### 把LISP函数转化为Emacs命令
#### 使用intercative
需要把函数等级到Emacs中,
需要使用`interactive`函数
```lisp
(interactive "prompt-string")
```
且这条语句必须是函数中的第一条语句(文档之后)
作用: 将函数注册为emacs的一个命令, 注册后, 可以使用`ESC x 函数名`来进行执行
这个函数中提示字符串`prompt-string`是可选的
#### intercative的提示字符串
##### 例子
```lisp
(interactive "nPercent: ")
```
"nPercent: "中的"n"提示用户输入一个整数
"Percent: "是实际出现在输入区里的提示文字
##### 交互式函数的参数类型代码
b-一个现有缓冲区的名字
e-事件(鼠标动作或功能按键动作)
f-一个现有文件的名字
n-数字(整数)
s-字符串

B-一个可能不存在的缓冲区名字
F-一个可能不存在的文件的名字
N-如果命令在调用时带有一个前缀参数, 按前缀参数指示的情况办理, 否则就是数字
S-符号

##### 较复杂的例子
```lisp
(defun replace-string(from to)
    (interactive "sReplace string: \nsReplace string %s with: ")
    ...)
```
当被调用时, 会显示
```
Replace string:
```
用户输入`fred`, 回车后
提示
```
Replace fred with: 
```
输入`fread`, 回车后, 
参数`from`则被赋值为`fred`, 参数`to`被赋值为`fread`

## LISP语言的基础函数
### 基本运算
#### 算数运算
`+`
`-`
`*`
`/`
`% `   取余
`1+`    递增
`1-`    递减
`max`    最大值
`min`    最小值
#### 比较运算
`>` `<` `>=` `<=`
`/=` 不等于
`=` 等于, 用于数字和字符
`equal` 等于, 用于字符串和其他复杂的数据对象

#### 逻辑运算
`and` `or` `not`

### 语句块
#### progn
类似于C语言中的`{ }`
#### let
见函数定义部分的注解
#### let*
当在计算某些局部变量的值时(下例中为charpos)需要用到其他局部变量的值(下例中为size)时, 可以使用`let*`
例子:
前进到当前缓冲区百分比处的函数
```lisp
(defun goto-percent (pct)
    (interactive "nGoto percent: ")
    (let* ((size (point-max))
        (charpos (/ (* size pct) 100)))
    (goto-char charpos)))
```
更高效的形式
```lisp
(defun goto-percent (pct)
    (interactive "nGoto percent: ")
    (goto-char (/ (* pct (point-max)) 100)))
```

### 控制结构
#### while
见函数定义部分的注解
#### if
基本形式
```lisp
(if condition
    true-case
    false-block)
```
执行流程:
先对condition进行求值, 如果不是`nil`执行true-case部分
如果是`nil`, 执行false-block部分
`true-case`必须是单独一条语句, 可以为`progn`语句块
而`false-block`则是一个语句块, 且`false-block`可以被省略
例子:
```lisp
(setq termtype (getenv "TERM"))
;; 如果终端类型为vt200, vt100, xterm, 则..., 否则...
(if (or (equal termtype "vt200")
        (equal termtype "vt100")
        (equal termtype "xterm"))
    (progn
        ;; True, do something
        )
    (progn
        ;; False, do something
        )
```
#### cond
相当于C中的switch
基本形式
```lisp
(cond
    (condition1
        statement-block1)
    (condition2
        statement-block2)
    ...)
```
例如:
```lisp
(setq termtype (getenv "TERM"))
(cond 
    ((equal termtype "vt200")
        (setq type 1))
    ((equal termtype "xterm")
        (setq type 2))
```
## Emacs的内部函数
### 编辑缓冲区, 文本, 文本块
函数名称 | 返回值或执行的动作
----------|---------------------
point    |    光标的字符位置
point-min    |    最小字符位置(通常是1)
point-max    |    最大字符位置(通常是缓冲区的长度)
mark    |    文本块标记的字符位置
bolp    |    光标是否位于行首(取值为`t`或`nil`)
eolp    |     光标是否位于行尾
bobp    |    光标是否位于编辑缓冲区的开始
eobp    |    光标是否位于编辑缓冲区的末尾
insert    |    把任意个数的参数插入到编辑缓冲区光标位置之后
number-to-string    |    把一个数值参数转换为一个字符串
string-to-number    |    把一个字符串转换为一个数字
char-to-string    |   把一个字符参数转换为一个字符串
concat    |    把任意个数的字符串合并到一起
substring    |    给定一个字符串的两个整数索引start和end, 返回从start到end位置之前的字符串, 下标从0开始计算. 例如`(substring "appropriate" 2 5)`返回"pro"
aref    |    返回字符串指定位置的字符ascii码, 例如`(aref "appropriate", 3)`返回114, 即`r`的ascii码

## Emacs中的正则表达式
emacs代码中的正则表达式的转义字符为`\\`(不同于常规的单个反斜杠`\`)
但在辅助输入区中读入字符时, 转义字符为`\`



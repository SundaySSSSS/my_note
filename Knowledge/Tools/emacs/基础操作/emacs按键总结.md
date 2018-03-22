# emacs按键总结
## 1）与文件操作有关的命令
C-x C-f 查找文件并且在新缓冲区中打开
C-x C-v 读入另一个文件替换掉用C-x C-f打开的文件
C-x i 把文件插入到光标的当前位置
C-x C-s 保存文件
C-x C-w 把缓冲区内容写入一个文件
C-x C-c 退出Emacs

## 2）与光标移动操作有关的命令
C-f 光标前移一个字符（右）
C-b 光标后移一个字符（左）
C-p 光标前移一行（上）
C-n 光标后移一行（下）
M-f 前移一个单词
M-b 后移一个单词
C-a 移动到行首
C-e 移动到行尾
M-e 前移一个句子
M-a 后移一个句子
M-} 前移一个段落
M-{ 后移一个段落
C-v 屏幕上卷一屏
M-v 屏幕下卷一屏
C-x ] 前移一页
C-x [ 后移一页
M-< 前移到文件头
M->; 后移到文件尾
C-l 重新绘制屏幕，当前行放在画面中心
M-n 或者 C-u n 重复执行n次后续命令
按下M-x后在辅助输入区中输入"goto-line"跳到指定的行，输入"goto-char"跳到指定的字符

## 3）与文件删除操作有关的命令
C-d 删除光标位置上的字符
DEL 删除光标前面的字符
M-d 删除光标后面的单词
M-DEL 删除光标前面的单词
C-k 从光标位置删除到行尾
M-k 删除光标后面的句子
C-x DEL 删除光标前面的句子
C-y 恢复被删除的文本或者粘贴最近删除或复制的文本
C-w 删除文件块
C-u 0 C-k 删除从光标位置到行首
按下M-x后在辅助输入区中输入"kill-paragraph"删除光标后面的段落，按下"backward-kill-paragraph"删除光标前面的段落

## 4）与文本块操作有关的命令
C-@ 标记文本块的开始（或结束）位置
C-x C-x 互换插入点和文本标记的位置
C-w 或 SHIFT-DEL 删除文本块
M-w 复制文本块
M-h 标记段落
C-x C-p 标记页面
C-x h 标记整个缓冲区

## 5）与位置交换操作有关的命令
C-t 交换两个字符的位置
M-t 交换两个单词的位置
C-x C-t 交换两个文本行的位置
按下M-x后在辅助输入区中输入"transpose-sentences"交换两个句子的位置，按下"transpose-paragraph"交换两个段落的位置

## 6）与改变字母大小写操作有关的命令
M-c 单词首字母改为大写
M-u 单词的字母全部改为大写
M-l 单词的字母全部改为小写

## 7）与查找操作相关的命令
C-s 向前递增查找
C-r 向后递增查找
C-s C-w 开始递增查找，把光标位置的单词做查找字符串
C-s C-y 开始递增查找，把光标位置到行尾之间的文本做查找字符串
C-s M-y 开始递增查找，将clipboard的内容作为查找字符串
C-s return searchstring return 向前开始非递增查找操作
C-r return searchstring return 向后开始非递增查找操作
C-s return C-w 向前开始单词查找（不受换行符、空格、标点符号影响）
C-r return C-w 向后开始单词查找（不受换行符、空格、标点符号影响）

## 8 ) 与使用编辑缓冲区和窗口有关的命令
C-x b 如果输入一个新的文件名则新建一个文件并且编辑,否则打开该文件
C-x s 保存全部缓冲区
C-x k 删除缓冲区
M-x rename-buffer 重命名当前缓冲区
C-x C-q 把当前编辑缓冲区设置为只读属性
C-x 0 删除当前所在的窗口
C-x 1 当前缓冲区满屏显示
C-x 2 创建上下排列的窗口
C-x 3 创建左右排列的窗口
C-x o 在窗口之间移动
C-x ^ grow window taller
C-x { shrink window narrower
C-x } grow window wider

EMACS常用模式 
C和C++模式

=== 指定为C++模式的方法 ===

一般根据扩展名自动设定，不用指定，不过有时候若希望.h文件是C++模式的（缺省是C模式），在文件第一行（或其末尾）上加入

// -*- C++ -*-

=== 语法高亮 ===

不是C模式专有，M-x global-font-lock-mode RET 或在.emacs中加入(global-font-lock-mode t)。

=== 子模式 ===

auto-state 输入时自动缩进，自动换行

hungry-state Backspace时，自动删除尽可能多的空白和空行

C-c C-t 同时转换(开/关)auto-state和hungry-state子模式

C-c C-a 转换 auto-state 子模式

C-c C-d 转换 hungry-state 子模式

=== 编辑命令 ===

C-c . 设置缩进风格（按TAB键可列出可用的风格，缺省的为gnu，其缩进为2个字符；linux为8个；k&r为5个，java为4个）

TAB 重新缩进当前行

M-/ 自动补齐（缓冲区中能找得到的串）

M-; 行尾加入注释

C-c C-e 扩展宏

C-c C-c 注释掉整个区域

C-u C-c C-c 取消注释

C-c C-\ 将区域中的每一行结尾都加入一个'\'字符

C-M \ 自动缩进所选区域 

=== 编译和调试 ===

M-x compile RET 编译

M-x gdb RET 调试

C-x ` （出错信息中）下一个错误，一个窗口显示错误信息，另一个显示源码的出错位置

C-c C-c 转到出错位置

启动gdb调试器后，光标在源码文件缓冲区中时：

C-x SPC 在当前行设置断点

C-x C-a C-s step

C-x C-a C-n next

C-x C-a C-t tbreak

C-x C-a C-r continue
Dired模式

常用命令：

m : mark

u : unmark

d : mark delete

D : 立即删除

x : 执行删除

g : refresh

C : copy

R : move

+ : 创建目录
Hideshow minor mode

在编程时可以隐藏函数的实现。M-x hs-minor-mode

(setq hs-minor-mode-prefix [(contrl o)]) 可以改变复杂的命令前缀.

用法：

`C-c @ C-h' : Hide the current block (`hs-hide-block').

`C-c @ C-s' : Show the current block (`hs-show-block').

`C-c @ C-c' : Either hide or show the current block (`hs-toggle-hiding')

`C-c @ C-M-h' : Hide all top-level blocks (`hs-hide-all').

`C-c @ C-M-s' : Show everything in the buffer (`hs-show-all').
十六进制模式

查看文本的十六进制编码

M-x hexl-mode

C-c C-c 退出十六进制模式

ECB快捷键

C-c . g d 目录列表窗口
C-c . g s 源码窗口
C-c . g m 方法和变量窗口
C-c . g h 历史窗口
C-c . g l 最后选择过的编辑窗口
C-c . g 1 编辑窗口1
C-c . g n 编辑窗口n
C-c . l c 选择版面
C-c . l r 重画版面
C-c . l t 拴牢版面(锁定版面)
C-c . l w 拴牢可见的ecb窗口
C-c . \ 拴牢编绎窗口
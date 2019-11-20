# vim映射
## 什么是vim映射
把一个操作映射到另一个操作

当不满意现在的按键操作时, 可以使用映射
或向映射一些方便的快捷键

## 基本映射
基本映射就是在normal模式下的映射
用map就可以实现基本映射
`map - x`
将-映射为了x, 故按下-就会删除字符

unmap关键字可以取消映射

## 模式映射
normal, visual, insert模式都可以定义映射
关键字分别为:
```
nmap/vmap/imap
```
使用上面的映射只在自己的模式下有效

例如:
将Ctrl+D映射为insert模式下的删除一行
```
imap <c-d> <Esc>ddi
```

## 现有映射的问题
如果:
```
nmap - dd
nmap \ -
```
则会按下\时, 直接被解释为dd
故map系的命令有递归的风险
保证插件映射没有冲突很麻烦
故vim提供了非递归映射

## 非递归映射
对应的非递归映射如下
```
nnoremap/vnoremap/inoremap
nmap/vmap/imap
```

任何时候都应该用非递归映射
# Git忽略规则.gitignore

## 过滤规则
```
1）/mtk/               过滤整个文件夹
2）*.zip                过滤所有.zip文件
3）/mtk/do.c         过滤某个具体文件
```
注意:
如果表示本目录, 不能用`./test/`,需要用`test/`(实验结果, 原因不明)

被过滤掉的文件就不会出现在git仓库中（gitlab或github）了，当然本地库中还有，只是push的时候不会上传。

## 指定规则
.gitignore还可以指定要将哪些文件添加到版本管理中：
1）!*.zip
2）!/mtk/one.txt

唯一的区别就是规则开头多了一个感叹号，Git会将满足这类规则的文件添加到版本管理中。

产生这种规则的原因
假如我们只需要管理/mtk/目录中的one.txt文件，这个目录中的其他文件都不需要管理，那么我们就需要使用：
1）/mtk/
2）!/mtk/one.txt
假设我们只有过滤规则，而没有添加规则，那么我们就需要把/mtk/目录下除了one.txt以外的所有文件都写出来！

最后需要强调的一点是，如果你不慎在创建.gitignore文件之前就push了项目，那么即使你在.gitignore文件中写入新的过滤规则，这些规则也不会起作用，Git仍然会对所有文件进行版本管理。
简单来说，出现这种问题的原因就是Git已经开始管理这些文件了，所以你无法再通过过滤规则过滤它们。因此一定要养成在项目开始就创建.gitignore文件的习惯，否则一旦push，处理起来会非常麻烦。

## 配置语法
以斜杠“/”开头表示目录；
以星号“*”通配多个字符；
以问号“?”通配单个字符
以方括号“[]”包含单个字符的匹配列表；
以叹号“!”表示不忽略(跟踪)匹配到的文件或目录；

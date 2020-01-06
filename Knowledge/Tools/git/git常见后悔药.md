# git常见后悔药
## 将仓库代码恢复到工作区

使用命令:
``` shell
git checkout -- filename.c
```
如果是撤销所有文件
``` shell
git checkout -- *
```

## 将某个历史版本内容回复到工作区

## 撤销add操作
```
git rm -r 文件名 --cached
```

## 撤销commit

```
git reset --soft | --mixed | --hard <commit_id>
```
其中:
--mixed    会保留源码,只是将git commit和index 信息回退到了某个版本.
--soft   保留源码,只回退到commit信息到某个版本.不涉及index的回退,如果还需要提交,直接commit即可.
--hard    源码也会回退到某个版本,commit和index 都会回退到某个版本.(注意,这种方式是改变本地代码仓库源码)

一般情况下mixed即可, 
例如:
```
git reset --mixed 46e3e952
```

## 撤销push
```
git revert <commit_id>
```
revert 之后你的本地代码会回滚到指定的历史版本
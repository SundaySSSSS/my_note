# svn版本回退



在Windows里，先打开Log面板，根据想要回退的内容，然后选择`revert to this revision`或者`revert changes from this revision`
关于这2个操作的区别，在：http://www.iusesvn.com/bbs/thread-1825-1-1.html 有详细的解释。
下面引用过来：
譬如有个文件，有十个版本，假定版本号是1，2，3，4，5，6，7，8，9，10
`Revert to this revision`： 如果在版本6这里点击“Revert to this revision”，表示7～10的修改全部作废，历史倒退到了版本6那个年代。

`Revert changes from this revision`：如果在版本6这里点击“Revert changes from this revision”，表示版本6这个历史事件被抹杀了，只剩下9个历史事件了。
如果同时选择了6，7，8三个历史时期并点击“Revert changes from this revision”，表示抹杀6~8这仨历史时期。
同理，如果同时选择7～10，然后点击“Revert changes from   this revision”，则效果跟在版本6这里点击“Revert to this revision”是一样的。



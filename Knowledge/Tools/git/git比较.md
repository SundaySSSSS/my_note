# git比较
## 两个分支比较
假如有两个分支dev和master
1， 查看dev有， 而master没有的
`git log dev ^master`
反之同理
2， 查看dev中比master中多提交了哪些内容
`git log dev..master`
反之同理
3， 查看两个分支有哪些不一样
`git log --left-right dev...master`

例如（这里例子是QCP分支和master分支）
其中commit后的 < 表示都是QCP分支的内容， QCP分支比master多两个commit

``` git
$ git log --left-right QCP...master
commit < 533feea95ca3d2828d7920a57a9bb1d087ebbd00
Author: caoxy <sxinyus@126.com>
Date:   Thu Jan 3 16:34:08 2019 +0800

    保存一份防止丢失

commit < 2200f8701f60056f2e5512b82ea04e3c04d1f729
Author: caoxinyu <sxinyus@126.com>
Date:   Fri Aug 31 11:12:12 2018 +0800

    添加了QCustomPlot的时频图雏形

```
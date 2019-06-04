# org-mode语法

## 标题
*开头的行为标题
```
注意：
* 要位于每行的行首
* 之后要有一个空格，然后再输入标题
连续几个*就表示是第几级大纲，最多支持10级。
```

## 引用文字
引用文字的标签是#+BEGIN_EXAMPLE / #+END_EXAMPLE ，在这之间的文字会保留原有的格式。

## 字体
```
*粗体*
/斜体/
+删除线+
_下划线_
下标： H_2 O
上标： E=mc^2
```

## 引用代码
将代码片放入`#+BEGIN_SRC … #+END_SRC`即可
快速输入 #+BEGIN_SRC … #+END_SRC

用org-mode写文章的的时候，经常需要引用代码片段或者程序输出，这就需要输入 #+BEGIN_SRC ... #+END_SRC 或者 #+BEGIN_EXAMPLE ... #+END_EXAMPLE 。输入的次数多了，就会想办法自动化，要么是用宏，要么是手工写 elisp函数，要么是借助 yasnippets 或者 skeleton 框架来写代码片段（比如 Emacs中文网 就发过一篇 《GNU Emacs Org-mode 写作的几个快捷方式》 ，那是借助 skeleton 来实现的）。

但其实，org-mode已经内置了快速输入的方法: 输入 <s 再按TAB键 ，就会自动展开为 #+BEGIN_SRC ... #+END_SRC 。类似地，输入 <e 再按TAB键，就会自动展开为 #+BEGIN_EXAMPLE ... #+END_EXAMPLE 。

## 引用图片
```
#+CAPTION: title for the image
#+LABEL: fig:tag_for_img
      [[file:path/to/image.jpg]]
```

## 导出成其他格式
已经编辑好的 org mode 文档可以导出为其他格式。
C-c C-e a 导出为文本文件。
C-c C-e h 导出为 HTML 文件。

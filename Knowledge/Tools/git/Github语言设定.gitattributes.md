# Github语言设定.gitattributes

如果想要修改某种文件的归属
例如*.h文件让Github当做C++而不是C
可以建立一个.gitattributes文件, 在里面加入:
```
*.h linguist-language=C++
```
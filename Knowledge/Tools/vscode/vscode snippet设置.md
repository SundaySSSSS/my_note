# vscode snippet设置
以go语言为例,
在go.json中, 加入:
``` json
"pln": {
    "prefix": "pln"
    "body": "fmt.Println($0)",
    "description": "fmt.Println()"
}
```
重启VsCode, 输入pln即可转换为fmt.Println了
其中$0表示光标放在哪里
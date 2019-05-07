# ubuntu环境变量

当前用户, 临时环境变量
`export ABC=/root/`
可通过如下命令验证
`echo $ABC`

当前用户永久环境变量
在~/.bashrc中追加
```
PATH="/work/share/NVC200E/ti_tools/linux_devkit/bin:$PATH"
PATH="/work/share/6467_2009q1_ti_tools/arm-2009q1/bin:$PATH"
```

系统所有用户永久环境变量
在`/etc/profile`中追加

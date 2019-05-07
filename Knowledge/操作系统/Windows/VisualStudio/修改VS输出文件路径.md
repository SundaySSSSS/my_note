# 修改VS输出文件路径

在[属性]->[链接器]->[常规]中的[输出文件]中
默认应该为`$(OutDir)$(TargetName)$(TargetExt)`

可以修改为`$(SolutionDir)$(TargetName)$(TargetExt)`
将输出文件放到sln文件的目录下

同时, 要保持[配置属性]->[常规]中的输出目录和刚才设置的匹配
例如设置为`$(SolutionDir)`

也可以修改为:

# Excel宏

```
Sub 合并单元格()
'
' 合并单元格 宏
'
' 快捷键: Ctrl+Shift+D
'
    With Selection
        .HorizontalAlignment = xlGeneral
        .VerticalAlignment = xlCenter
        .WrapText = False
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = True
    End With
End Sub

```

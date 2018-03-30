# PyGame绘制文字

## 最基础打印
```
font = pygame.font.Font(None, 20) # None表示默认字体, 20是字号

font_sur = font.render("CXY", True, (255, 0, 0)) # True表示开启抗锯齿, (255, 0, 0)表示绘制红色字
screen.blit(font_sur, (0, 0))

```

## 获取行高
`line_height = font.get_linesize()`

## 显示中文
是否能够显示中文和使用的字体有关
在mac下, 可以使用Arial Unicode字体, 可以正常显示中文
```
font = pygame.font.Font("res/font/Arial Unicode.ttf", 40)
```
在python2中, 传入render的字符串需要加前缀u, 例如
```
font_sur = font.render(u"汉字", True, (255, 0, 0))
```

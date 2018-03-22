# PyGame绘制文字

## 最基础打印
```
font = pygame.font.Font(None, 20) # None表示默认字体, 20是字号

font_sur = font.render("CXY", True, (255, 0, 0)) # True表示开启抗锯齿, (255, 0, 0)表示绘制红色字
screen.blit(font_sur, (0, 0))

```

## 获取行高
`line_height = font.get_linesize()`

# Pygame色彩与绘图机制
## 更换碰撞球的背景色
```
# Unit PYG05: Pygame Wall Ball Game Version 9
import pygame, sys
 
pygame.init()
icon = pygame.image.load("PYG03-flower.png")
pygame.display.set_icon(icon)
size = width, height = 600, 400
speed = [1,1]
BLACK = 0, 0, 0
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Pygame壁球")
ball = pygame.image.load("PYG02-ball.gif")
ballrect = ball.get_rect()
fps = 300
fclock = pygame.time.Clock()
still = False
bgcolor = pygame.Color("black")
 
def RGBChannel(a):
    return 0 if a<0 else (255 if a>255 else int(a))
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1)* int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                still = True
        elif event.type == pygame.MOUSEBUTTONUP:
            still = False
            if event.button == 1:
                ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] == 1:
                ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)
    if pygame.display.get_active() and not still:
        ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left < 0  or ballrect.right >width:
        speed[0] = - speed[0]
        if ballrect.right > width and ballrect.right + speed[0] > ballrect.right:
            speed[0] = - speed[0]
    if ballrect.top < 0  or ballrect.bottom > height:
        speed[1] = - speed[1]
        if ballrect.bottom > height and ballrect.bottom + speed[1] > ballrect.bottom:
            speed[1] = - speed[1]
 
    bgcolor.r = RGBChannel(ballrect.left*255/width)
    bgcolor.g = RGBChannel(ballrect.top*255/height)
    bgcolor.b = RGBChannel(min(speed[0],speed[1])*255/max(speed[0],speed[1],1))
 
    screen.fill(bgcolor)
    screen.blit(ball,ballrect)
    pygame.display.update()
    fclock.tick(fps)
```

## 图形绘制实例
```
# Unit PYG05: Pygame Shape Draw Test
import pygame, sys
from math import pi
 
pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Pygame图形绘制")
GOLD = 255, 251, 0
RED = pygame.Color('red')
WHITE = 255, 255, 255
GREEN = pygame.Color('green')
 
#r1rect = pygame.draw.rect(screen, GOLD, (100,100,200,100), 5)
#r2rect = pygame.draw.rect(screen, RED, (210,210,200,100), 0)
 
e1rect = pygame.draw.ellipse(screen, GREEN, (50,50,500,300), 3)
c1rect = pygame.draw.circle(screen, GOLD, (200,180), 30, 5)
c2rect = pygame.draw.circle(screen, GOLD, (400,180), 30)
r1rect = pygame.draw.rect(screen, RED, (170, 130, 60, 10), 3)
r2rect = pygame.draw.rect(screen, RED, (370, 130, 60, 10))
plist = [(295,170), (285,250), (260,280), (340,280), (315,250), (305,170)]
l1rect = pygame.draw.lines(screen, GOLD, True, plist, 2)
a1rect = pygame.draw.arc(screen, RED, (200,220,200,100), 1.4*pi, 1.9*pi, 3)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
```

## 文字描绘
### 方法1, 使用render_to方法
```
# Unit PYG05: Pygame Font Draw
import pygame, sys
import pygame.freetype
 
pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Pygame文字绘制")
GOLD = 255, 251, 0
 
f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc", 36)
f1rect = f1.render_to(screen, (200,160), "世界和平", fgcolor=GOLD, size=50)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
```

### 方法1, 使用render方法
```
# Unit PYG05: Pygame Font Draw
import pygame, sys
import pygame.freetype
 
pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Pygame文字绘制")
GOLD = 255, 251, 0
 
f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc", 36)
f1surf, f1rect = f1.render("世界和平", fgcolor=GOLD, size=50)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
 
    screen.blit(f1surf, (200,160))
    pygame.display.update()
```

## 将碰撞球换位文字
### render_to版本
```
# Unit PYG05: Pygame Wall Ball Game Version 10
import pygame, sys
import pygame.freetype
 
pygame.init()
size = width, height = 600, 400
speed = [1,1]
GOLD = 255, 251, 0
BLACK = 0, 0, 0
pos = [230, 160]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame文字绘制")
f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc", 36)
f1rect = f1.render_to(screen, pos, "世界和平", fgcolor=GOLD, size=50)
fps = 300
fclock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if pos[0] < 0 or pos[0] + f1rect.width > width:
        speed[0] = - speed[0]
    if pos[1] <0 or pos[1] + f1rect.height > height:
        speed[1] = - speed[1]
    pos[0] = pos[0] + speed[0]
    pos[1] = pos[1] + speed[1]
 
    screen.fill(BLACK)
    f1rect = f1.render_to(screen, pos, "世界和平", fgcolor=GOLD, size=50)
    pygame.display.update()
    fclock.tick(fps)
```

### render版本
```
# Unit PYG05: Pygame Wall Ball Game Version 11
import pygame, sys
import pygame.freetype
 
pygame.init()
size = width, height = 600, 400
speed = [1,1]
GOLD = 255, 251, 0
BLACK = 0, 0, 0
pos = [230, 160]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame文字绘制")
f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc", 36)
f1surf, f1rect = f1.render("世界和平", fgcolor=GOLD, size=50)
fps = 300
fclock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if pos[0] < 0 or pos[0] + f1rect.width > width:
        speed[0] = - speed[0]
    if pos[1] <0 or pos[1] + f1rect.height > height:
        speed[1] = - speed[1]
    pos[0] = pos[0] + speed[0]
    pos[1] = pos[1] + speed[1]
 
    screen.fill(BLACK)
    f1surf, f1rect = f1.render("世界和平", fgcolor=GOLD, size=50)
    screen.blit(f1surf, (pos[0], pos[1]))
    pygame.display.update()
    fclock.tick(fps)
```
# PyGame基础

## 基本概念
### Surface对象
pygame中用来表示图像的对象


## 常用方法:
### 初始化
`pygame.init()`
### 设置窗口大小
使用set_mode方法返回一个窗体surface对象
`screen = pygame.display.set_mode((600, 400))`
### 设置窗口标题
`pygame.display.set_caption("Title")`
### 加载图片
使用load方法返回一个surface对象
`pic = pygame.image.load("pic.png")`
### 获得surface对象位置
`pos = sur.get_rect()`
### 移动surface对象
`speed = [2, -3]`
`sur = sur.move(speed)`
### 翻转surface
`sur = pygame.transform.flip(sur, True, True)`
flip的第二个和第三个参数表明是否在水平, 垂直方向上翻转
### 给surface填充颜色
`screen.fill((255, 255, 255))`
### 将一个surface绘制到另一个surface上
`screen.blit(pic, positon)`
### 更新界面
`pygame.display.flip()`

### 设置帧率
`clock = pygame.time.Clock()`

### 延迟
`pygame.time.delay(10)`
单位是毫秒

## 简单实例
下面的例子是一个碰撞球, 在球碰到边缘时, 被弹回
```python
# -*- coding: utf-8 -*-
import pygame
import sys

pygame.init()

size = width, height = 600, 400
speed = [-2, 1]
bg = (255, 255, 255)

#
clock = pygame.time.Clock()

# 指定窗口大小, 返回一个Surface对象
screen = pygame.display.set_mode(size)
# 指定窗口标题
pygame.display.set_caption("碰撞球")
# 加载图片
ball = pygame.image.load("ball.png")
# 获得图片的位置
position = ball.get_rect()

while True:
    # 检测是否有退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # 移动图像
    position = position.move(speed)
    if position.left < 0 or position.right > width:
        # 翻转图像
        ball = pygame.transform.flip(ball, True, False)
        # 反方向移动
        speed[0] = -speed[0]
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    # 填充背景
    screen.fill(bg)
    # 更新图像
    screen.blit(ball, position)
    # 更新界面
    pygame.display.flip()
    # 延迟
    # pygame.time.delay(10)
    # 设置帧率不高于200帧/秒
    clock.tick(200)
```




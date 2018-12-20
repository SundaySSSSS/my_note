# PyGame音乐播放

``` python
# -*- coding: utf-8 -*-
import pygame
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def main():
    pygame.init()
    pygame.mixer.init()

    # 绘制说明文字
    font = pygame.font.Font(None, 20)  # None表示默认字体, 20是字号
    font_sur = font.render("Space to pause/play music, Left and right switch music, D and B to play sound", True, (255, 0, 0))

    # 音乐相关文件名
    bg_music_name = ("weight of the world.mp3", "desert.mp3", "pleasure ground.mp3")
    MAX_MUSIC_NUM = 3  # 总共有几个背景音乐
    cur_music_id = 0  # 当前音乐id
    # 背景音乐相关
    pygame.mixer.music.load(bg_music_name[cur_music_id])
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()
    # 音效相关
    bird_sound = pygame.mixer.Sound("bird.wav")
    bird_sound.set_volume(0.9)
    dog_sound = pygame.mixer.Sound("dog.wav")
    dog_sound.set_volume(0.9)

    screen = pygame.display.set_mode((600, 200))
    pygame.display.set_caption("Sound And Music")

    clock = pygame.time.Clock()
    # 是否正在播放背景音乐
    is_playing = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    bird_sound.play()
                if event.key == pygame.K_d:
                    dog_sound.play()
                if event.key == pygame.K_SPACE:
                    is_playing = not is_playing
                    if is_playing:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()
                if event.key == pygame.K_LEFT:
                    pygame.mixer.music.pause()
                    cur_music_id -= 1
                    if cur_music_id < 0:
                        cur_music_id = MAX_MUSIC_NUM
                    pygame.mixer.music.load(bg_music_name[cur_music_id])
                    pygame.mixer.music.play()
                if event.key == pygame.K_RIGHT:
                    pygame.mixer.music.pause()
                    cur_music_id += 1
                    if cur_music_id >= MAX_MUSIC_NUM:
                        cur_music_id = 0
                    pygame.mixer.music.load(bg_music_name[cur_music_id])
                    pygame.mixer.music.play()

        # 填充背景
        screen.fill((0, 0, 0))
        # 显示文字
        screen.blit(font_sur, (0, 0))

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()

```
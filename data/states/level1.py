import pygame as pg
from data.components import mario
from .. import constants as c

# 游戏第一关的控制类
class Level1:
    def __init__(self):
        self.startup()

    def startup(self):
        # 创建Mario对象
        self.mario = mario.Mario()
        # 初始化Mario坐标
        self.setup_mario_location()
        # 将Mario加入精灵编组
        self.all_sprites = pg.sprite.Group(self.mario)

    # 设置Mario初始位置
    def setup_mario_location(self):
        self.mario.rect.x = 80
        self.mario.rect.bottom = c.SCREEN_HEIGHT - self.mario.rect.height


    def update(self, surface, keys, current_time):
        # 设置背景色为白色
        pg.display.get_surface().fill(c.BGCOLOR)
        # 调用精灵组的update方法,组内的每个对象都会调用自己的draw方法
        self.all_sprites.update(keys, current_time)
        # 调用精灵组的draw方法,组内的每个对象都会调用自己的draw方法
        self.all_sprites.draw(surface)











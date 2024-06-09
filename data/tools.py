import os
import pygame as pg
from . import constants as c
from data.states import level1
#功能：加载所有图像
#返回：包含所有图片的字典
def load_all_images(directory, colorkey=(255, 0, 255), accept=('.png','.jpg','.bmp')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img
    return graphics

# 整个游戏的控制类
class Control:
    def __init__(self):
        pg.init()
        #设置游戏标题
        pg.display.set_caption(c.ORIGINAL_CAPTION)
        #设置屏幕大小
        self.screen = pg.display.set_mode(c.SCREEN_SIZE)
        #游戏退出标志
        self.done = False
        #控制帧率
        self.clock = pg.time.Clock()
        #窗口标题
        self.caption = c.ORIGINAL_CAPTION
        #设置帧率
        self.fps = 60
        #控制窗口是否显示帧率
        self.show_fps = True
        #保存用户按下的按键
        self.keys = pg.key.get_pressed()
        # 获取所有图片
        c.GFX = load_all_images(os.path.join("resources", "graphics"))
        # 当前是第几关卡
        self.state = level1.Level1()
    #功能：事件循环函数
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
                self.toggle_show_fps(event.key)
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()

    #功能：控制是否显示帧率
    def toggle_show_fps(self, key):
        if key == pg.K_F5:
            self.show_fps = not self.show_fps

    #
    def update(self):
        current_time = pg.time.get_ticks()
        # 把游戏窗口传进去，调用level1的update函数，以更新Mario
        self.state.update(self.screen, self.keys, current_time)

    #功能：主函数
    def main(self):
        while not self.done:
            # 检测事件
            self.event_loop()
            # 调用control的update方法
            self.update()
            # 更新屏幕
            pg.display.update()
            # 设置帧率
            self.clock.tick(self.fps)
            # 如果显示帧率
            if self.show_fps:
                # 把窗口标题与帧率连接起来
                with_fps = "{}  -  {:.2f} FPS".format(self.caption,self.clock.get_fps())
                pg.display.set_caption(with_fps)


import pygame as pg
from .. import tools
from .. import constants as c


class Mario(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # 把mario图像对象传给self.sprite_sheet
        self.sprite_sheet = c.GFX['mario_bros']
        # 存放左右走的帧图像
        self.right_frames = []
        self.left_frames = []
        # 帧索引
        self.frame_index = 0
        # 加载mario图像
        self.load_from_sheet()
        # 创建mario的image对象
        self.image = self.right_frames[self.frame_index]
        # 得到mario对象的形状
        self.rect = self.image.get_rect()

    def get_image(self, x, y, width, height):
        # 在内存中创建一张黑色图片
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()
        # 把大的图片从x，y位置开始截取width, height大小的子图
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        # 防止背景变黑
        image.set_colorkey(c.BLACK)
        # 对图片缩放
        image = pg.transform.scale(image,
                                   (int(rect.width*c.SIZE_MULTIPLIER),
                                    int(rect.height*c.SIZE_MULTIPLIER)))
        return image

    def load_from_sheet(self):
        self.right_frames.append(self.get_image(178, 32, 12, 16))










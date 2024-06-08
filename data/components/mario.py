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

        # mario状态，脸朝向
        self.state = c.STAND
        self.facing_right = True

        # mario速度等设置
        self.x_vel = 0
        self.y_vel = 0
        self.walking_timer = 0
        self.max_x_vel = 4
        self.x_accel = c.SMALL_ACCEL

    # 更新Mario
    def update(self, keys, current_time):
        self.handle_state(keys, current_time)
        self.update_position()
        self.animation()

    # 更新mario位置
    def update_position(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

    # 播放动画
    def animation(self):
        if self.facing_right:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image = self.left_frames[self.frame_index]

    # mario状态变换
    def handle_state(self, keys, current_time):
        if self.state == c.STAND:
            self.standing(keys, current_time)
        elif self.state == c.WALK:
            self.walking(keys, current_time)

    # Mario站立状态
    def standing(self, keys, current_time):
        self.frame_index = 0
        self.x_vel = 0
        self.y_vel = 0
        if keys[pg.K_LEFT]:
            self.facing_right = False
            self.state = c.WALK
        elif keys[pg.K_RIGHT]:
            self.facing_right = True
            self.state = c.WALK
        else:
            self.state = c.STAND

    # Mario行走状态
    def walking(self,keys,current_time):
        if self.frame_index == 0:
            self.frame_index += 1
            self.walking_timer = current_time
        else:
            if (current_time - self.walking_timer > 115):
                if self.frame_index < 3:
                    self.frame_index += 1
                else:
                    self.frame_index = 1
                self.walking_timer = current_time
        # 加速效果
        if keys[pg.K_s]:
            self.max_x_vel = 6
        else:
            self.max_x_vel = 4

        if keys[pg.K_RIGHT]:
            self.facing_right = True
            if self.x_vel < 0:
                self.frame_index = 5
            self.x_accel = c.SMALL_ACCEL
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel

        elif keys[pg.K_LEFT]:
            self.facing_right = False
            self.x_accel = c.SMALL_ACCEL

            if self.x_vel > 0:
                self.frame_index = 5
            # 向左速度是负的，如果没达到最小的负的速度，继续向左
            # 比如 -3 > -4，那就继续减小
            if self.x_vel > (self.max_x_vel*-1):
                self.x_vel -= self.x_accel
        # 没有按键按下则停止
        else:
            if self.facing_right:
                if self.x_vel > 0:
                    self.x_vel -= self.x_accel
                else:
                    self.x_vel = 0
                    self.state = c.STAND
            else:
                if self.x_vel < 0:
                    self.x_vel += self.x_accel
                else:
                    self.x_vel = 0
                    self.state = c.STAND


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
        self.right_frames.append(self.get_image(178, 32, 12, 16))   # standing

        self.right_frames.append(self.get_image(80, 32, 15, 16))    # right walking 1
        self.right_frames.append(self.get_image(99, 32, 15, 16))    # right walking 2
        self.right_frames.append( self.get_image(114, 32, 15, 16))  # right walking 3

        self.right_frames.append(self.get_image(144, 32, 16, 16))   # right jump
        self.right_frames.append(self.get_image(130, 32, 14, 16))   # right skid

        for frame in self.right_frames:
            new_image = pg.transform.flip(frame,True,False)
            self.left_frames.append(new_image)







import pygame

from setting import Settings

class Ship:
    """管理飞船行为和属性的类。

       Attributes:
           image (pygame.Surface): 飞船图像。
           rect (pygame.Rect): 飞船的矩形区域。
           speed (float): 飞船移动速度（像素/帧）。
       """

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = Settings()

        self.ship_path = self.settings.ship_1

        self.image = pygame.image.load(self.ship_path)
        # 要对获取的飞船图片进行缩放

        # print(self.image.get_height())
        # print(self.image.get_width())
        if self.ship_path == self.settings.ship_2:
            self.image = pygame.transform.scale(self.image, (self.image.get_width() / 2, self.image.get_height() / 2))
        else:
            self.image = pygame.transform.scale(self.image, (self.image.get_width() / 6, self.image.get_height() / 6))

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.speed = self.settings.ship_speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def move_update(self):
        # if self.moving_right and self.rect.right < self.screen_rect.right:
        #     self.rect.x += self.speed
        # elif self.moving_left and self.rect.left > 0:
        #     self.rect.x -= self.speed
        #
        # elif self.moving_up and self.rect.top > self.screen_rect.top:
        #     self.rect.y -= self.speed
        # elif self.moving_down and self.rect.bottom < self.screen_rect.height:
        #     self.rect.y += self.speed

        """根据移动状态更新飞船位置。"""
        dx, dy = 0, 0
        if self.moving_right and self.rect.right < self.screen_rect.right:
            dx += self.speed
        if self.moving_left and self.rect.left > 0:
            dx -= self.speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            dy -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            dy += self.speed

        # 更新坐标并限制边界
        self.x += dx
        self.y += dy
        self.rect.x = self.x
        self.rect.y = self.y
        # self.rect.clamp_ip(self.screen_rec

    def reset_setting(self):
        """重置飞船到初始位置并清空移动状态。"""
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.settings = Settings()
        self.speed = self.settings.ship_speed_factor

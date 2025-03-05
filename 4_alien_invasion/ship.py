import pygame
from setting import Settings

class Ship:

    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        #要对获取的飞船图片进行缩放

        # print(self.image.get_height())
        # print(self.image.get_width())
        self.image = pygame.transform.scale(self.image,(self.image.get_width()/6,self.image.get_height()/6))

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.settings = Settings()
        self.speed = self.settings.ship_speed_factor


    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def move_update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
        elif self.moving_left and self.rect.left > 0:
            self.rect.x -= self.speed

        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= self.speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.rect.y += self.speed


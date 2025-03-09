import pygame
from pygame.examples.aliens import Alien
import random

from pygame.sprite import Sprite


class AlienBomb(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.aliens = ai_game.aliens

        self.image = pygame.image.load('./images/alien_bomb.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() / 2.5, self.image.get_height() / 2.5))
        self.rect = self.image.get_rect()
        self.create_bombs(ai_game)



    def create_bombs(self,ai_game):
        screen_rect = self.screen.get_rect()
        max_x = screen_rect.width - self.rect.width

        for _ in range(100):
            # 随机x坐标（确保在屏幕内）
            self.rect.x = random.randint(5, max_x - 5)
            # 固定在屏幕最顶部
            self.rect.y = ai_game.settings.status_bar_height + 8

            # 检查与现有外星人的碰撞
            if not any(self.rect.colliderect(alien.rect) for alien in self.aliens):
                break
        else:
            # 如果循环正常结束（未break），说明未找到合适位置
            self.kill()  # 直接销毁这个实例
            return

            # 存储精确的x坐标（用于平滑移动）
        # self.x = float(self.rect.x)




    def update(self):
        self.screen_rect = self.screen.get_rect()
        self.rect.y += self.settings.alien_bomb_speed_factor

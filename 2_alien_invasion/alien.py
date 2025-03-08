import random

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() / 10, self.image.get_height() / 10))
        self.rect = self.image.get_rect()

        # 获取屏幕尺寸
        screen_rect = self.screen.get_rect()
        max_x = screen_rect.width - self.rect.width

        # 获取现有外星人群组
        existing_aliens = ai_game.aliens
        self.alive = True

        # 尝试生成不重叠的位置（最多尝试100次）
        for _ in range(100):
            # 随机x坐标（确保在屏幕内）
            self.rect.x = random.randint(5, max_x - 5)
            # 固定在屏幕最顶部
            self.rect.y = ai_game.settings.status_bar_height + 8

            # 检查与现有外星人的碰撞
            if not any(self.rect.colliderect(alien.rect) for alien in existing_aliens):
                break
        else:
            # 如果循环正常结束（未break），说明未找到合适位置
            self.kill()  # 直接销毁这个实例
            return

        # 存储精确的x坐标（用于平滑移动）
        self.x = float(self.rect.x)

    def kill(self):
        self.alive = False
        super().kill()

    def update(self):
        self.screen_rect = self.screen.get_rect()
        self.rect.y += self.settings.alien_speed_factor

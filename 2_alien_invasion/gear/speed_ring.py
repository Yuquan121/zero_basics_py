import pygame
import random

class SpeedRing(pygame.sprite.Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/speed_ring.png')

        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))

        self.aliens = ai_game.aliens

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.create_ring(self)


    def create_ring(self, ai_game):
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




    def update(self):
        self.rect.y += self.settings.speed_necklace_speed_factor
        if self.rect.top > self.screen_rect.height:
            self.kill()


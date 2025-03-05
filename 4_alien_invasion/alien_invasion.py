import sys
import pygame
from setting import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    def __init__(self):
        pygame.init()
        # 时钟控制帧率
        self.clock = pygame.time.Clock()
        # 屏幕设置
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        pygame.display.set_caption(self.settings.caption)
        # 导入飞船
        self.ship = Ship(self)
        self.bullet = Bullet(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self.check_events()
            # 飞船运动
            self.ship.move_update()
            # 子弹运动
            self.update_bullets()
            # 每次循环重新绘制屏幕,并使最近绘制的屏幕可见
            self.update_screen()
            self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)


    def update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)




    def update_screen(self):
        """更新屏幕"""
        self.screen.fill(self.settings.bg_color)
        # 更新绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 更新绘制飞船
        self.ship.blitme()
        pygame.display.flip()

    def check_keydown_events(self, event):
        """响应按下"""
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.file_bullet()

    def check_keyup_events(self, event):
        """响应释放"""
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


    def file_bullet(self):
        """创建一颗子弹，并将其加入编组bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

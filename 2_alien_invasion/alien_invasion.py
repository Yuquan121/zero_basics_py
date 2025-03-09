import sys
import random

import pygame

from setting import Settings
from ship import Ship
from sprites.bullet import Bullet
from sprites.alien import Alien
from game_stats import GameStats
from sprites.alien_bomb import AlienBomb
from gear.speed_ring import SpeedRing


class AlienInvasion:
    def __init__(self):
        # 游戏开启标志
        self.game_active = True

        pygame.init()
        # 时钟控制帧率
        # 加载背景音乐（支持 .mp3 或 .ogg）
        pygame.mixer.music.load('music/12240.mp3')
        # 调整背景音乐音量（0.0 ~ 1.0）
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        self.clock = pygame.time.Clock()
        # 屏幕设置
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # 新增游戏区域定义（状态栏下方）
        self.game_area_rect = pygame.Rect(
            0,
            self.settings.status_bar_height,
            self.settings.screen_width,
            self.settings.screen_height - self.settings.status_bar_height
        )
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        pygame.display.set_caption(self.settings.caption)

        pygame.mixer.init()  # 初始化音频模块
        # 加载音效文件
        self.shoot_sound = pygame.mixer.Sound('music/shoot.mp3')
        self.shoot_sound.set_volume(0.2)  # 射击音效设为60%音量
        self.hit_sound = pygame.mixer.Sound('music/hurt1.mp3')
        self.hit_sound.set_volume(0.4)
        self.bomb_sound = pygame.mixer.Sound('music/output.wav')
        self.bomb_sound.set_volume(0)
        self.speed_ring_sound = pygame.mixer.Sound('music/golden.mp3')
        self.bomb_sound.set_volume(0.4)

        # 控制是否添加速度项链
        self.speed_ring_count = 0
        # 子弹数量
        self.bullet_allowed = self.settings.bullets_allowed

        # 外星人组设置
        self.last_alien_time = self.settings.last_alien_time  # 上次生成时间
        self.alien_interval = self.settings.alien_interval  # 生成间隔2秒
        self.batch_size_range = self.settings.batch_size_range  # 每批生成1-3个

        self.last_alien_bomb_time = self.settings.last_alien_bomb_time

        # 导入飞船
        self.ship = Ship(self)
        self.bullet = Bullet(self)
        self.bullets = pygame.sprite.Group()

        # 导入外星人组
        self.aliens = pygame.sprite.Group()

        # 导入外星炸弹组
        self.bombs = pygame.sprite.Group()
        # 导入速度装备组
        self.speed_ring = pygame.sprite.Group()

        self.game_stats = GameStats(self)

    def run_game(self):
        while True:
            while self.game_active:
                self.check_events()
                # 飞船运动
                self.ship.move_update()
                # 子弹运动
                self.update_bullets()
                # 外星人运动
                self.update_aliens()
                # 外星炸弹运动
                self.update_bombs()
                # 速度项链运动
                self.update_spreed()
                # 每次循环重新绘制屏幕,并使最近绘制的屏幕可见
                self.update_screen()
                self.clock.tick(60)

            self.handle_game_over()

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

            collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
            # 射中后获得金币
            for shoot_bullet, hit_aliens in collisions.items():
                self.game_stats.coin += len(hit_aliens) * 100

    def update_aliens(self):
        self.aliens.update()
        collided_alien = pygame.sprite.spritecollideany(self.ship, self.aliens)
        if collided_alien is not None:
            print("Ship Collision!!!")
            self.game_stats.collision_effects()
            self.aliens.remove(collided_alien)
            # self.game_active = False
            self.game_stats.ship_hp -= 50
            if self.game_over():
                self.game_active = False

        for alien in self.aliens.copy():
            if alien.rect.bottom >= self.settings.screen_height:
                self.aliens.remove(alien)
                self.game_stats.ship_hp -= 1
                self.hit_sound.play()
                # 屏幕抖动
                self.screen.scroll(5, 0)  # 向右抖动5像素
                pygame.display.update()
                pygame.time.delay(15)
                self.screen.scroll(-5, 0)  # 恢复

                if self.game_over():
                    self.game_active = False
                # print(len(self.aliens))

    def update_bombs(self):
        self.bombs.update()  # 更新位置
        # 移除超出屏幕的炸彈
        for bomb in self.bombs.copy():
            if bomb.rect.top >= self.settings.screen_height:
                self.bombs.remove(bomb)

        # 与飞船碰撞逻辑
        coll_bomb = pygame.sprite.spritecollideany(self.ship, self.bombs)
        if coll_bomb is not None:
            print("Ship Collision!!!")
            self.bombs.remove(coll_bomb)
            self.game_stats.ship_hp -= 100
            if self.game_over():
                self.game_active = False

    def update_spreed(self):
        self.speed_ring.update()
        for speed_necklace in self.speed_ring.copy():
            if speed_necklace.rect.bottom >= self.settings.screen_height:
                self.speed_ring.remove(speed_necklace)

        given_speed = pygame.sprite.spritecollideany(self.ship, self.speed_ring)
        if given_speed is not None:
            self.speed_ring_sound.play()
            self.ship.speed += self.settings.increase_speed_factor
            self.speed_ring.remove(given_speed)

    def update_screen(self):
        """更新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.game_stats.draw_status_bar()
        # 更新绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 更新绘制飞船
        self.ship.blitme()
        # 更新绘制外星人组
        self._create_fleet()
        self._create_alien_bombs()
        self._create_speed_ring()
        self.aliens.draw(self.screen)
        self.bombs.draw(self.screen)
        self.speed_ring.draw(self.screen)
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
        if len(self.bullets) < self.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.shoot_sound.play()

    def _create_fleet(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_alien_time >= self.alien_interval:
            self.last_alien_time = current_time
            # 随机生成外星人（每批1-2个）
            batch_size = random.randint(*self.batch_size_range)
            # 随着金币的加多难度加大
            dynamic_batch = min(batch_size + self.game_stats.coin // 2000, 5)
            # 尝试生成批次
            success_count = 0
            for _ in range(dynamic_batch):
                new_alien = Alien(self)
                if new_alien.alive:
                    self.aliens.add(new_alien)
                    success_count += 1

            # print(f"尝试生成{batch_size}个，成功{success_count}个")

    def _create_alien_bombs(self):
        """当游戏时间进行到30s时开始生成外星炸弹"""
        current_time = pygame.time.get_ticks()
        # 计算游戏已运行时间（当前时间 - 游戏启动时间）
        game_elapsed_time = current_time - self.game_stats.game_start_time
        if game_elapsed_time >= 30000:
            batch_size = random.randint(*self.settings.bomb_batch_size_range)
            #检查生成间隔
            if current_time - self.last_alien_bomb_time >= self.settings.alien_bomb_interval:
                self.last_alien_bomb_time = current_time
                # 随着金币加多难度加大
                dynamic_batch = min(batch_size + self.game_stats.coin // 1500, 6)
                for _ in range(dynamic_batch):
                    new_alien_bomb = AlienBomb(self)
                    self.bombs.add(new_alien_bomb)
                    self.bomb_sound.play()

    def _create_speed_ring(self):
        current_time = pygame.time.get_ticks()
        # 计算游戏已运行时间（当前时间 - 游戏启动时间）
        game_elapsed_time = current_time - self.game_stats.game_start_time
        if game_elapsed_time >= 20000 and self.speed_ring_count == 0:
            new_speed = SpeedRing(self)
            self.speed_ring.add(new_speed)
            self.speed_ring_count += 1

    def game_over(self):
        """只有HP到0游戏才结束"""
        if self.game_stats.ship_hp <= 0:
            self.game_active = False

    def handle_game_over(self):
        while not self.game_active:
            self.game_stats.draw_game_over()
            pygame.display.flip()

            # 处理退出事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.game_stats.reset_game_stats()


# 在屏幕显示下次生成倒计时
def show_cooldown(self):
    remaining = self.alien_interval - (pygame.time.get_ticks() - self.last_alien_time)
    if remaining < 0: remaining = 0
    # 绘制倒计时条...
    pass
    pygame.display.flip()  # 更新显示


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

from os import remove

import pygame

class GameStats:

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.ship = ai_game.ship
        self.ship_hp = 100  # 初始生命值
        self.coin = 0  # 初始得分
        self._load_status_images()

    def draw_game_over(self):
        #绘制背景
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((135, 206, 235))
        self.screen.blit(overlay, (0, 0))

        # 弹窗矩形
        popup_width, popup_height = 400, 200
        screen_rect = self.screen.get_rect()
        popup_rect = pygame.Rect(
            (screen_rect.centerx - popup_width // 2),  # 水平居中
            (screen_rect.centery - popup_height // 2),  # 垂直居中
            popup_width,
            popup_height
        )
        pygame.draw.rect(self.screen, (255, 255, 255), popup_rect, border_radius=10)

        # 显示文字
        font = pygame.font.Font(None, 36)
        # 第一行文字：Game Over
        text1 = font.render("Game Over", True, (255, 0, 0))
        text1_rect = text1.get_rect(center=(popup_rect.centerx, popup_rect.centery - 20))

        # 第二行文字：Press R to start a new game
        font_small = pygame.font.Font(None, 36)
        text2 = font_small.render("Press R to start a new game", True, (255, 0, 0))
        text2_rect = text2.get_rect(center=(popup_rect.centerx, popup_rect.centery + 30))
        # 绘制文字
        self.screen.blit(text1, text1_rect)
        self.screen.blit(text2, text2_rect)
        pygame.display.flip()  # 确保弹窗内容更新

    def _load_status_images(self):
        """加载状态栏需要的图标"""
        # 生命图标（❤️）
        self.heart_image = pygame.image.load('images/heart.png').convert_alpha()
        # 金币图标
        self.coin_image = pygame.image.load('images/coin.png').convert_alpha()
        # 时间图标（⏳）
        self.time_image = pygame.image.load('images/clock.jpg').convert_alpha()

        # 统一图标大小（根据状态栏高度调整）
        icon_size = (self.settings.status_bar_height - 5, self.settings.status_bar_height - 5)
        self.heart_image = pygame.transform.scale(self.heart_image, icon_size)
        self.coin_image = pygame.transform.scale(self.coin_image, icon_size)
        self.time_image = pygame.transform.scale(self.time_image, icon_size)

    def draw_status_bar(self):
        """绘制带图标的状态栏"""
        # 绘制背景
        status_rect = pygame.Rect(0, 0, self.settings.screen_width, self.settings.status_bar_height)
        pygame.draw.rect(self.screen, self.settings.status_bg_color, status_rect)

        # 布局参数
        x_padding = 20
        y_center = self.settings.status_bar_height // 2
        icon_text_spacing = 10  # 图标和文字间距

        # 绘制生命值（左侧）
        self._draw_status_item(
            image=self.heart_image,
            text=f"{self.ship_hp}",
            x=x_padding,
            y_center=y_center,
            icon_text_spacing=icon_text_spacing
        )

        # 绘制金币（中间）
        self._draw_status_item(
            image=self.coin_image,
            text=f"{self.coin}",
            x=self.settings.screen_width//2,
            y_center=y_center,
            icon_text_spacing=icon_text_spacing,
            align='center'
        )

        # 绘制时间（右侧）
        self._draw_status_item(
            image=self.time_image,
            text=f"{pygame.time.get_ticks()//1000}s",
            x=self.settings.screen_width - x_padding,
            y_center=y_center,
            icon_text_spacing=icon_text_spacing,
            align='right'
        )

    def _draw_status_item(self, image, text, x, y_center, icon_text_spacing=10, align='left'):
        """绘制单个状态项（图标+文字）"""
        # 创建文字表面
        font = pygame.font.Font(None, self.settings.status_font_size)
        text_surf = font.render(text, True, self.settings.status_font_color)

        # 计算整体宽度
        total_width = image.get_width() + icon_text_spacing + text_surf.get_width()

        # 根据对齐方式确定绘制位置
        if align == 'center':
            draw_x = x - total_width // 2
        elif align == 'right':
            draw_x = x - total_width
        else:  # left
            draw_x = x

        # 绘制图标
        icon_y = y_center - image.get_height() // 2
        self.screen.blit(image, (draw_x, icon_y))

        # 绘制文字
        text_x = draw_x + image.get_width() + icon_text_spacing
        text_y = y_center - text_surf.get_height() // 2
        self.screen.blit(text_surf, (text_x, text_y))


    def collision_effects(self):
        # 屏幕抖动
        self.screen.scroll(5, 0)  # 向右抖动5像素
        pygame.display.update()
        pygame.time.delay(50)
        self.screen.scroll(-5, 0)  # 恢复

        # 红屏效果
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((255, 0, 0, 128))
        self.screen.blit(overlay, (0, 0))
        pygame.display.flip()
        pygame.time.delay(100)


    def reset_game_stats(self):
        """重制游戏设置"""
        self.ai_game.aliens.empty()
        self.ai_game.bullets.empty()
        self.ship.reset_setting()
        self.ai_game.game_active = True
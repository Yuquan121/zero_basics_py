class Settings:

    def __init__(self):
        # 主屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)
        self.caption = 'Alien Invasion'


        # 状态栏配置
        self.status_bar_height = 40  # 状态栏高度
        self.status_bg_color = (30, 30, 30)  # 深灰色背景
        self.status_font_color = (255, 255, 255)  # 白色文字
        self.status_font_size = 24

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 60, 60)
        self.bullets_allowed = 5

        # 外星人设置
        self.fleet_direction = 1
        self.speedup_scale = 1.1
        self.alien_speed_factor = 1
        self.last_alien_time = 0
        self.alien_interval = 2000  # 生成间隔2秒
        self.batch_size_range = (1, 2)  # 每批生成1-3个

        #飞船设置
        self.ship_1 = 'images/ship.bmp'
        self.ship_2 = 'images/ship2.png'
        self.ship_3 = 'images/ship3.png'
        self.ship_speed_factor = 2

        #外星炸弹设置
        self.alien_bomb_speed_factor = 22
        self.last_alien_bomb_time = 28000
        self.alien_bomb_interval = 10000  # 生成间隔8秒
        self.bomb_batch_size_range = (1, 2)  # 每批生成1-2个

        #速度项链设置
        self.speed_necklace_speed_factor = 1
        self.increase_speed_factor = 1

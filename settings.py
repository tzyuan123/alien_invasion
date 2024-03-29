# -*- coding: utf-8 -*-
__author__ = 'Administrator'


class Settings():
    """存储《外星人入侵》 的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕位置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 100, 100, 255
        self.bullets_allowed = 30000

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction 为1 表示向右移动，为-1 表示想左移
        self.fleet_direction = 1


if __name__ == '__main__':
    pass

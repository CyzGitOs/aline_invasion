'''
Author: your name
Date: 2021-11-08 21:34:35
LastEditTime: 2021-11-08 23:48:19
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /DemoGame/ship.py
'''
"""
    创建飞机类
"""

import pygame


class Ship( ):

    def __init__( self, screen, settings ):
        """初始化飞船并设置其初始化位置"""
        #加载屏幕
        self.screen = screen
        
        #加载屏幕设置参数
        self.settings = settings
        
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load( 'images/aigei_com.png' )
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #将每艘新飞船放在屏幕的底部中央
        self.rect.centerx = self.screen_rect.centerx#  把飞船的中心放在屏幕的中心
        self.rect.bottom = self.screen_rect.bottom # 把飞船的底部放在屏幕的底部
        
        # 在飞船的属性center中存储小数值
        self.center = float( self.rect.centerx )
        
        #x下面是飞船的移动标志  True:表示按键一直按着   
        self.shipmove_up = False  #向上
        self.shipmove_down = False #向下
        self.shipmove_right = False #向右
        self.shipmove_left = False #向左
        
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
        
    def ship_update( self ):
        """更新飞船的位置"""
        if self.shipmove_up == True and self.rect.top >= 0:
            self.rect.centery -= self.settings.ship_sheep
            
        elif self.shipmove_down == True and self.rect.bottom <= self.settings.screen_heigth:
            self.rect.centery += self.settings.ship_sheep
            
        elif self.shipmove_left == True and self.rect.left >= 0:
            self.rect.centerx -= self.settings.ship_sheep
            
        elif self.shipmove_right == True and self.rect.right <= self.settings.screen_width:
            self.rect.centerx += self.settings.ship_sheep
            
        # 根据self.center更新rect对象ss
        # self.rect.centerx = self.center
        



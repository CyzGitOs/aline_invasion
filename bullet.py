'''
Author: your name
Date: 2021-11-08 23:55:34
LastEditTime: 2021-11-10 21:43:46
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /DemoGame/bullet.py
子弹的类
'''
import pygame
from pygame.sprite import Sprite


class Bullet( Sprite ):
    """一个对飞船发射的子弹进行管理的类"""
    
    def __init__( self, Setting, screen, ship ):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen
        
        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置 
        self.rect = pygame.Rect( 0, 0, Setting.bullet_width, 
                                Setting.bullet_heigth )
        self.rect.centerx = ship.rect.centerx  
        self.rect.top = ship.rect.top  #开始位置为飞船的矩形高度
        
        #存储用小数表示的子弹位置 
        self.bullet_y = float( self.rect.y )
        self.bullet_color = Setting.bullet_color #子弹颜色
        self.bullet_sheep = Setting.bullet_sheep  #子弹的移动速度
            
        
        
    def update( self ):
        """更新子弹"""
        #创建子弹
        
        
        #更新表示子弹位置的小数值
        self.bullet_y -= self.bullet_sheep
        #更新表示子弹的rect(矩形)的位置
        self.rect.y = self.bullet_y
    
    def draw_bullet( self ):
        """在屏幕上绘制子弹"""
        pygame.draw.rect( self.screen, self.bullet_color, self.rect )

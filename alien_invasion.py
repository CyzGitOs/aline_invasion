'''
Author: your name
Date: 2021-11-05 22:29:09
LastEditTime: 2021-11-09 23:16:16
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /DemoGame/alien_invasion.py
'''
"""
    主功能
"""
# import sys

import pygame

from settings import settings 
from ship import Ship
# from game_functions import check_events
import game_functions as game_fun
from pygame.sprite import Group





def Run_Game( ):
    #初始化游戏并创建一个屏幕对象
    pygame.init( )
    

    Setting = settings(  ) #创建一个设置类
    screen = pygame.display.set_mode( ( Setting.screen_width, 
                                    Setting.screen_heigth ) )#创建一个屏幕对象
    pygame.display.set_caption( "外星人" ) #窗口名称
    
    
    ship = Ship( screen, Setting ) #创建一件飞船
    #设置背景色
    # 创建一个用于存储子弹的编组
    bullets = Group()
    #开始游戏的主循环
    while True:
        game_fun.check_events( Setting, screen, ship, bullets ) #按键监控
        ship.ship_update()#
        bullets.update()#
        
        #删除已消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove( bullet )
        print(len(bullets))
        game_fun.game_updatescreen( screen, ship, Setting, bullets ) #更新显示
        
        




if __name__ == '__main__':    #程序开始
    Run_Game( )

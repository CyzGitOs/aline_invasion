'''
Author: your name
Date: 2021-11-08 22:20:29
LastEditTime: 2021-11-10 21:42:38
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /DemoGame/game_functions.py
Lllustrate: 写游戏的功能
'''
import pygame 
import sys
from ship import Ship
from bullet import Bullet


def check_keydown_events( event, Setting, screen, ship, bullet ):
    """响应按键"""
    if event.key == pygame.K_s: #按键按下
        ship.shipmove_down = True
    elif event.key == pygame.K_w:  
        ship.shipmove_up = True
    elif event.key == pygame.K_d:
        ship.shipmove_right = True
    elif event.key == pygame.K_a:
        ship.shipmove_left = True
    elif event.key == pygame.K_SPACE:
        # Setting.bullet_move = True
        #创建新子弹并将其加入到编组bullets中
        if len( bullet ) < Setting.bullet_allowed: #发射子弹的数量
            new_bullet = Bullet(Setting, screen, ship)
            bullet.add( new_bullet ) 
    elif event.key == pygame.K_ESCAPE:
        sys.exit()
    
    
        #按下esc键退出
        
    
def check_keyup_events(event, Setting, ship, bullet ):
    """响应松开"""
    if event.key == pygame.K_s: #按键松开
        ship.shipmove_down = False
    elif event.key == pygame.K_w:  
        ship.shipmove_up = False
    elif event.key == pygame.K_d:
        ship.shipmove_right = False
    elif event.key == pygame.K_a:
        ship.shipmove_left = False
    # elif event.key == pygame.K_SPACE:
    #     Setting.bullet_move = False

def check_events( Setting, screen, ship, bullet ):
    """响应鼠标和案件事件"""
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT: #触发屏幕关闭键
            sys.exit(1)
        elif event.type == pygame.KEYDOWN: #触发按键按下事件
            check_keydown_events( event, Setting, screen, ship, bullet )
            
        elif event.type == pygame.KEYUP: #触发按键松开事件
            check_keyup_events( event=event, Setting=Setting, ship=ship, bullet=bullet )
        
        else:  #打印飞机的坐标
            print("飞船的坐标：")
            print('x=',ship.rect.centerx, 'y=',ship.rect.centery)
    #创建子弹
    # if Setting.bullet_move == True:
    #     new_bullet = Bullet(Setting, screen, ship)
    #     bullet.add( new_bullet )




def game_updatescreen( screen, ship, Setting, bullet ):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每一次循环时都更新背景颜色(重新绘制屏幕)
    screen.fill( Setting.Bg_color )
    
    # 在飞船和外星人后面重绘所有子弹 
    for bullets in bullet.sprites():
        bullets.draw_bullet()
        
    ship.blitme()

    #让最近绘制的屏幕可见
    pygame.display.flip()
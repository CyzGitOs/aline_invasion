'''
Author: your name
Date: 2021-11-05 22:29:11
LastEditTime: 2021-11-10 21:43:44
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /DemoGame/settings.py
'''




class settings( ):
    """
        存储外星人的所有的类
    """

    def __init__( self ):
        """
            初始化控制游戏外观和飞船速度的属性
        """
        #屏幕设置
        self.screen_width = 1200 #屏幕的宽度
        self.screen_heigth = 600 #屏幕的高度
        self.Bg_color = ( 233, 244, 250 ) #背景颜色
        self.ship_sheep = 1.5 # 飞船的速度
        
        #子弹设置
        self.bullet_sheep = 0.5 #移动速度
        self.bullet_width = 3 #宽度
        self.bullet_heigth = 5 #高度
        self.bullet_color = 60, 60, 60 #颜色
        self.bullet_allowed = 3  #子弹发射的数量
        #子弹不断发射标志
        # self.bullet_move = False
        
        







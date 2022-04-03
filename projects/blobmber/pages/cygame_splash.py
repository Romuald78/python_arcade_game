import math

import arcade

from projects.blobmber.classes.Word import Word
from utils.gfx_sfx import createFixedSprite, createAnimatedSprite

class CyGameSplash():


    def __init__(self, W, H, manager):
        super().__init__()
        self.W = W
        self.H = H
        self.manager = manager

    def __moveBack(self):
        T = 2*math.pi*self.time
        xc = self.W/4
        rx = self.W/19
        self.bigTopLeft.center_x = math.cos(T/23)*rx + xc
        xc = self.W/6
        rx = self.W/23
        T += 73
        self.bigTopMid.center_x = math.cos(T/29)*rx + xc
        yc = self.H/10
        ry = self.H/17
        T += 53
        self.bottom.center_y = math.cos(T/19)*ry + yc
        xc = 4*self.W/5
        rx = self.W/17
        yc = 10*self.H/11
        ry = self.H/17
        T += 17
        self.topRight.center_x = math.cos(T/17)*rx + xc
        self.topRight.center_y = math.cos(T/13)*ry + yc
        xc = 6*self.W/7
        rx = self.W/11
        yc = self.H/6
        ry = self.H/11
        T += 23
        self.bottomRight.center_x = math.cos(T / 25) * rx + xc
        self.bottomRight.center_y = math.cos(T / 41) * ry + yc

    def setup(self):
        self.time = 0
        self.title = Word(self.W/2,self.H/2.0,"Blobber Man", self.W/12,self.W/12, (128,255,128,200), True, True)
        self.title.center_x = self.W//13
        self.title.center_y = self.H//1.25

        self.pressStart = Word(self.W/10, self.H/10, "Press Start", self.W/20, self.W/14, (255,255,0,200), blinking=True)
        self.pressStart.center_x = self.W//4
        self.pressStart.center_y = self.H//2.25

        params = {
            "filePath": "projects/blobmber/images/big_lava_top_left.png",
            "position": (self.W/4, self.H/2),
            "size": (self.W/2, self.H),
            "isMaxRatio" : True,
            "filterColor": (255,0,0,160)
        }
        self.bigTopLeft = createFixedSprite(params)
        params = {
            "filePath": "projects/blobmber/images/big_lava_top_mid.png",
            "position": (self.W/5, 3*self.H/4),
            "size": (self.W/2, self.H/2),
            "isMaxRatio" : True,
            "filterColor": (0,0,255,160)
        }
        self.bigTopMid = createFixedSprite(params)
        params = {
            "filePath": "projects/blobmber/images/lava_bottom.png",
            "position": (self.W / 2, self.H / 10),
            "size": (self.W / 3, self.H / 3),
            "isMaxRatio": True,
            "filterColor": (0, 255, 255, 160)
        }
        self.bottom = createFixedSprite(params)
        params = {
            "filePath": "projects/blobmber/images/lava_top_right.png",
            "position": (3*self.W/4, 10*self.H / 11),
            "size": (self.W / 3, self.H / 3),
            "isMaxRatio": True,
            "filterColor": (255, 255, 0, 160)
        }
        self.topRight = createFixedSprite(params)
        params = {
            "filePath": "projects/blobmber/images/lava_bottom_left.png",
            "position": (self.W/3, self.H / 3),
            "size": (self.W / 2, self.H / 2),
            "isMaxRatio": True,
            "filterColor": (255, 0, 255, 160),
            "flipH" : True
        }
        self.bottomRight = createFixedSprite(params)
        params = {
            "filePath": "projects/blobmber/images/bg.png",
            "position": (self.W/2, self.H / 2),
            "size": (self.W, self.H),
            "isMaxRatio": True,
            "filterColor": (0, 255, 0, 160),
        }
        self.bg = createFixedSprite(params)


    def update(self,deltaTime):
        self.time += deltaTime
        self.title.update(deltaTime)
        self.pressStart.update(deltaTime)
        self.__moveBack()

    def draw(self):
        self.bg.draw()
        self.topRight.draw()
        self.bigTopLeft.draw()
        self.bigTopMid.draw()
        self.bottom.draw()
        self.bottomRight.draw()
        self.title.draw()
        if self.time >= 3:
            self.pressStart.draw()
        if self.time <= 3:
            alpha = int(255*(2.5-self.time)/3)
            arcade.draw_rectangle_filled(self.W//2, self.H//2, self.W, self.H, (0,0,0,alpha))

    def onKeyEvent(self, key, isPressed):
        if key == arcade.key.SPACE and isPressed:
            self.setup()

    def onButtonEvent(self, gamepadNum, buttonName, isPressed):
        pass


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
        self.bigTopMid.center_x = math.cos(T/29)*rx + xc
        yc = self.H/10
        ry = self.H/17
        self.bottom.center_y = math.cos(T/19)*ry + yc
        xc = 4*self.W/5
        rx = self.W/17
        yc = 10*self.H/11
        ry = self.H/17
        self.topRight.center_x = math.cos(T/17)*rx + xc
        self.topRight.center_y = math.cos(T/13)*ry + yc
        xc = self.W/6
        rx = self.H/11
        yc = self.H/6
        ry = self.H/11
        self.bottomLeft.center_x = math.cos(T/25)*rx + xc
        self.bottomLeft.center_y = math.cos(T/41)*ry + yc

    def setup(self):
        self.time = 0
        self.title = Word(self.W/5.5,self.H/5.5,"Blobber Man", self.W/12,self.W/12, (128,255,128,200))
        self.title.center_x = self.W//11
        self.title.center_y = self.H//1.25

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
            "position": (self.W/6, 3*self.H/4),
            "size": (self.W/2, self.H/2),
            "isMaxRatio" : True,
            "filterColor": (0,0,255,160)
        }
        self.bigTopMid = createFixedSprite(params)
        params = {
            "filePath": "projects/blobmber/images/lava_bottom.png",
            "position": (self.W / 1.5, self.H / 10),
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
            "filterColor": (255, 255, 0, 128)
        }
        self.topRight = createFixedSprite(params)
        params = {
            "filePath": "projects/blobmber/images/lava_bottom_left.png",
            "position": (self.W/3, self.H / 3),
            "size": (self.W / 2, self.H / 2),
            "isMaxRatio": True,
            "filterColor": (255, 0, 255, 128)
        }
        self.bottomLeft = createFixedSprite(params)



    def update(self,deltaTime):
        self.time += deltaTime
        self.title.update(deltaTime)
        self.__moveBack()

    def draw(self):
        self.topRight.draw()
        self.bigTopLeft.draw()
        self.bigTopMid.draw()
        self.bottom.draw()
        self.bottomLeft.draw()
        self.title.draw()

    def onKeyEvent(self, key, isPressed):
        if isPressed:
            self.title.center_y = self.H/0.75

    def onButtonEvent(self, gamepadNum, buttonName, isPressed):
        pass


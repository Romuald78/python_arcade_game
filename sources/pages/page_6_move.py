import random

import arcade.key

from sources.utils import createAnimatedSprite, createFixedSprite
from random import randint


class Page6Move():

    def __init__(self, W, H):
        super().__init__()
        self.W = W
        self.H = H

    def setup(self):
        # ANIMATED SPRITES
        params = {
            "filePath": "images/characters/ninja.png",
            "spriteBox": (7, 1, 120, 120),
            "size"     : (240,240),
            "position": (self.W//2, self.H//2),
            "startIndex": 1,
            "endIndex": 6,
            "frameDuration": 1 / 20,
            "filterColor": (255, 255, 255, 255),
            "flipH": False,
        }
        self.runR = createAnimatedSprite(params)
        params["flipH"] = True
        self.runL = createAnimatedSprite(params)
        # FIXED SPRITES
        params = {
            "filePath": "images/characters/ninja_fix.png",
            "size"     : (240,240),
            "position": (self.W // 2, self.H // 2),
            "filterColor": (255, 255, 255, 255),
            "flipH": False,
        }
        self.idleR = createFixedSprite(params)
        params["flipH"] = True
        self.idleL = createFixedSprite(params)
        # move vars
        self.moveL = False
        self.moveR = False
        self.lastMoveL = False

    def update(self,deltaTime):
        # update animations for all
        self.runL.update_animation(deltaTime)
        self.runR.update_animation(deltaTime)
        # move sprites according to user key selection
        if self.moveL:
            self.idleL.center_x -= 10
        if self.moveR:
            self.idleL.center_x += 10
        # all sprites are at the same position
        self.idleR.center_x = self.idleL.center_x
        self.runL.center_x  = self.idleL.center_x
        self.runR.center_x  = self.idleL.center_x

    def draw(self):
        if self.moveL == self.moveR:
            if self.lastMoveL:
                self.idleL.draw()
            else:
                self.idleR.draw()
        elif self.moveL:
            self.runL.draw()
        else:
            self.runR.draw()

    def onKeyEvent(self, key, isPressed):
        if key== arcade.key.Q:
            self.moveL = isPressed
            self.lastMoveL = True
        if key == arcade.key.D:
            self.moveR = isPressed
            self.lastMoveL = False

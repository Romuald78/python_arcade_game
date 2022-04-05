import random

import arcade

from projects.blobmber.classes.constants import Constants
from utils.collisions import collision2Ellipses, collisionCircleEllipse
from utils.gfx_sfx import createAnimatedSprite


class Bubble():

    def __createExplosions(self):
        self.exploded = True
        # create center
        x = self.bubble.center_x
        y = self.bubble.center_y
        w = self.bubble.width
        h = self.bubble.height
        index = random.randint(0,1)
        params = {
            "filePath": "projects/blobmber/images/explosions.png",
            "position": (x, y),
            "size": (w, h),
            "spriteBox": (3, 2, 256, 256),
            "frameDuration": 1,
            "filterColor": self.clr,
            "startIndex": index,
            "endIndex": index,
            "flipH": [True, False][random.randint(0,1)],
            "flipV": [True, False][random.randint(0,1)],
        }
        center = createAnimatedSprite(params)
        center.angle = random.randint(0,360)
        self.explosions.append(center)
        # create explosions according to correct angle
        for angle in range(0, 360, 90):
            pass

    def __init__(self, x, y, w, h, clr, power, countdown):
        self.exploded = False
        self.clr = clr
        self.countdown = countdown
        self.power = power
        params = {
            "filePath": "projects/blobmber/images/bubble.png",
            "position": (x, y),
            "size": (w, h),
            "spriteBox": (5, 2, 144, 144),
            "frameDuration": Constants.BUBBLE_FRAME_SPEED,
            "filterColor" : clr,
            "startIndex": 0,
            "endIndex": 5,
            "flipH": False
        }
        self.bubble = createAnimatedSprite(params)
        self.bubble.angle = random.random()*360
        self.explosions = arcade.SpriteList()

    def update(self,deltaTime):
        self.countdown -= deltaTime
        self.bubble.update_animation(deltaTime)
        # generate explosions
        if self.countdown <= 0 and not self.exploded:
            self.__createExplosions()

    def draw(self):
        # TODO handle progressive creation of the explosions
        if self.countdown > 0:
            self.bubble.draw()
        else:
            self.explosions.draw()

        if Constants.DEBUG_PHYSICS:
            arcade.draw_circle_outline( self.bubble.center_x, self.bubble.center_y,
                                        self.bubble.width*Constants.BUBBLE_COLL_SIZE_COEF/2,
                                        (255,255,255))

    def can_reap(self):
        return False
#        return self.countdown <= 0

    def isOvalColliding(self, center, radiusX, radiusY):
        if not self.exploded:
            HW = self.bubble.width*Constants.BUBBLE_COLL_SIZE_COEF / 2
            if collisionCircleEllipse( (self.bubble.center_x, self.bubble.center_y) ,
                                       HW,
                                       center,
                                       radiusX, radiusY
                                       ):
                return True
        return False

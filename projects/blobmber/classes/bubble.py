import math
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
        params["flipH"] = False
        for angle in range(0, 360, 90):
            for dist in range(1, self.power+1, 1):
                # set distance
                dx = dist * w * math.cos(angle*math.pi/180)
                dy = dist * h * math.sin(angle * math.pi / 180)
                # update params to display explosion
                index = random.randint(3,5)
                params["startIndex"] = index
                params["endIndex"] = index
                params["flipV"] = [True, False][random.randint(0,1)]
                params["position"] = (x+dx,y+dy)
                explode = createAnimatedSprite(params)
                explode.angle = angle+180
                self.explosions.append(explode)
                # Check collisions with all bubbles : if yes, detonate !!
                for b in self.allBubbles:
                    HW = self.bubble.width * Constants.BUBBLE_COLL_SIZE_COEF / 2
                    if b.isOvalColliding((x+dx, y+dy), HW, HW):
                        b.detonate()
                        # this is a condition to stop distance progression
                        dist = self.power + 1

    def __init__(self, x, y, w, h, clr, power, countdown, allBubbles):
        self.allBubbles = allBubbles
        self.exploded = False
        self.clr = clr
        self.countdown = countdown
        self.power = max(1,power)
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
        if self.countdown <= 0:
            if not self.exploded:
                self.__createExplosions()
            elif self.countdown >= -Constants.BUBBLE_FADE_TIME:
                t = -self.countdown
                for exp in self.explosions:
                    exp.alpha = self.bubble.alpha * (Constants.BUBBLE_FADE_TIME - t) / Constants.BUBBLE_FADE_TIME

    def draw(self):
        # TODO handle progressive creation of the explosions
        if self.countdown > 0:
            self.bubble.draw()
        else:
            self.explosions.draw()
        if Constants.DEBUG_PHYSICS:
            arcade.draw_text( str(len(self.allBubbles)), self.bubble.center_x, self.bubble.center_y,(255,255,255))
            arcade.draw_circle_outline( self.bubble.center_x, self.bubble.center_y,
                                        self.bubble.width*Constants.BUBBLE_COLL_SIZE_COEF/2,
                                        (255,255,255))

    def detonate(self):
        if self.countdown > Constants.BUBBLE_PROPAGATION_DELAY:
            self.countdown = Constants.BUBBLE_PROPAGATION_DELAY

    def can_reap(self):
        return self.countdown <= -Constants.BUBBLE_FADE_TIME

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

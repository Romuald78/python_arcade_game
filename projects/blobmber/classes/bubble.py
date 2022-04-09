import math
import random

import arcade

from projects.blobmber.classes.constants import Constants
from utils.collisions import collision2Ellipses, collisionCircleEllipse, collisionCircleAABB, collisionEllipseAABB
from utils.gfx_sfx import createAnimatedSprite


class Bubble():

    def __createExplosions(self):
        self.exploded = True
        # create center
        x = self.initPos[0]
        y = self.initPos[1]
        w = self.bubble.width
        h = self.bubble.height
        index = random.randint(0,1)
        clr = (self.clr[0], self.clr[1], self.clr[2], int(0.5*(self.clr[3]+255)))
        params = {
            "filePath": "projects/blobmber/images/explosions.png",
            "position": (x, y),
            "size": (w*Constants.BUBBLE_COLL_SIZE_COEF, h*Constants.BUBBLE_COLL_SIZE_COEF),
            "spriteBox": (3, 2, 256, 256),
            "frameDuration": 1,
            "filterColor": clr,
            "startIndex": index,
            "endIndex": index,
            "flipH": [True, False][random.randint(0,1)],
            "flipV": [True, False][random.randint(0,1)],
        }
        center = createAnimatedSprite(params)
        center.angle = random.randint(0,360) + 1
        self.explosions.append(center)
        # Check collisions with all bubbles : if yes, detonate !!
        HW = self.bubble.width * Constants.BUBBLE_COLL_SIZE_COEF / 2
        for bub in self.allBubbles:
            if bub.isOvalColliding((x, y), HW, HW):
                bub.detonate()
        # create explosions according to correct angle
        params["flipH"] = False
        for angle in range(0, 360, 90):
            for dist in range(1, self.power+1, 1):
                # set distance
                dw1 = w * math.cos(angle * math.pi / 180)
                dh1 = h * math.sin(angle * math.pi / 180)
                dx  = dist * dw1
                dy  = dist * dh1
                ofx = -dw1/2
                ofy = -dh1/2
                realX = x + dx + ofx
                realY = y + dy + ofy
                # update params to display explosion
                index = random.randint(3,5)
                params["startIndex"] = index
                params["endIndex"] = index
                params["flipV"] = [True, False][random.randint(0,1)]
                params["position"] = (realX,realY)
                explode = createAnimatedSprite(params)
                explode.angle = angle+180
                # prepare collision data
                HW = self.bubble.width * Constants.BUBBLE_COLL_SIZE_COEF / 2
                HH = HW
                if angle == 90 or angle == 270:
                    HW /= 2
                else:
                    HH /= 2
                topLeft     = (realX-HW, realY+HH)
                bottomRight = (realX+HW, realY-HH)
                #DEBUG
                if Constants.DEBUG_PHYSICS:
                    explode.width  = 2*HW
                    explode.height = 2*HH

                # Check collisions with all bubbles : if yes, detonate !!
                # Stop progression
                stop = False
                for bub in self.allBubbles:
                    if bub is not self:
                       if bub.isAABBColliding(topLeft , bottomRight):
                            bub.detonate()
                            print(f"stop in angle:{angle} with dist:{dist}")
                            stop= True
                    else:
                        print("SKIP Bomb !!")
                # Check collisions with all blocks
                if not stop:
                    if self.allBlocks.isAABBColliding(topLeft , bottomRight):
                        stop = True
                # Check collisions with all crates
                if not stop:
                    if self.allCrates.isAABBColliding(topLeft , bottomRight, True):
                        # add the explosion in this case particularly
                        self.explosions.append(explode)
                        stop = True
                # Stop current direction
                if stop:
                    break
                # if OK,  add the sprite
                self.explosions.append(explode)

    def __computeBlinkColor(self, clr):
        r,g,b,a = clr
        Y = 0.299*r + 0.587*g + 0.114*b
        r = 255
        if Y >= 128:
            g = 0
            b = 0
        else:
            g = 160
            b = 160
        return (int(r), int(g), int(b), a)

    def __init__(self, x, y, w, h, clr, power, countdown, allBubbles, allBlocks, allCrates):
        self.allBubbles = allBubbles
        self.allBlocks = allBlocks
        self.allCrates = allCrates
        self.exploded = False
        self.clr = clr
        self.blinkClr = self.__computeBlinkColor(clr)
        self.countdown = countdown
        self.power = max(1,power)
        self.initPos = (x,y)
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
        self.bubble.center_x = self.initPos[0]
        self.bubble.center_y = self.initPos[1]
        # generate explosions
        if self.countdown <= 0:
            if not self.exploded:
                self.__createExplosions()
            elif self.countdown >= -Constants.BUBBLE_FADE_TIME:
                t = -self.countdown
                for exp in self.explosions:
                    exp.alpha = self.bubble.alpha * (Constants.BUBBLE_FADE_TIME - t) / Constants.BUBBLE_FADE_TIME
        elif self.countdown <= Constants.BUBBLE_SHAKE_TIME:
            # The bubble is shaking
            self.bubble.center_x = self.initPos[0] + random.randint(-Constants.BUBBLE_SHAKE_HALF, Constants.BUBBLE_SHAKE_HALF)
            self.bubble.center_y = self.initPos[1] + random.randint(-Constants.BUBBLE_SHAKE_HALF, Constants.BUBBLE_SHAKE_HALF)
            self.bubble.angle += random.randint(0,10)/10
            # Last second the bubble is blinking between color and full RED
            state = int(self.countdown*10)%2
            if state == 0:
                self.bubble.color = self.clr
            elif state == 1:
                self.bubble.color = self.blinkClr

    def draw(self):
        # TODO handle progressive creation of the explosions
        if self.countdown > 0:
            self.bubble.draw()
        else:
            self.explosions.draw()
        if Constants.DEBUG_PHYSICS:
            arcade.draw_text( str(round(self.countdown,1)), self.initPos[0], self.initPos[1],(255,255,255))
            arcade.draw_circle_outline( self.initPos[0], self.initPos[1],
                                        self.bubble.width*Constants.BUBBLE_COLL_SIZE_COEF/2,
                                        (255,255,0,255))
            for exp in self.explosions:
                HW = exp.width
                HH = exp.height
                arcade.draw_rectangle_outline(exp.center_x, exp.center_y,HW, HH, (255,255,0,255))

    def detonate(self):
        if self.countdown > Constants.BUBBLE_PROPAGATION_DELAY:
            self.countdown = Constants.BUBBLE_PROPAGATION_DELAY

    def can_reap(self):
        return self.countdown <= -Constants.BUBBLE_FADE_TIME

    def isShaking(self):
        return self.countdown <= Constants.BUBBLE_SHAKE_TIME

    def isAABBColliding(self, tl, br):
        if not self.exploded:
            if collisionEllipseAABB( tl, br, self.initPos, self.bubble.width/2, self.bubble.height/2 ):
                return True
        return False

    def isOvalColliding(self, center, radiusX, radiusY):
        if not self.exploded:
            HW = self.bubble.width*Constants.BUBBLE_COLL_SIZE_COEF / 2
            if collisionCircleEllipse( (self.initPos[0], self.initPos[1]) ,
                                       HW,
                                       center,
                                       radiusX, radiusY
                                       ):
                return True
        return False

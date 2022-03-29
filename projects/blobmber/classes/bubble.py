import arcade

from projects.blobmber.classes.constants import Constants
from utils.collisions import collision2Ellipses, collisionCircleEllipse
from utils.gfx_sfx import createAnimatedSprite


class Bubble():

    def __init__(self, x, y, w, h, clr, countdown):
        self.clr = clr
        self.countdown = countdown
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

    def update(self,deltaTime):
        self.countdown -= deltaTime
        self.bubble.update_animation(deltaTime)

    def draw(self):
        self.bubble.draw()
        if Constants.DEBUG_PHYSICS:
            arcade.draw_circle_outline( self.bubble.center_x, self.bubble.center_y,
                                        self.bubble.width*Constants.BUBBLE_COLL_SIZE_COEF/2,
                                        (255,255,255))

    def isOvalColliding(self, center, radiusX, radiusY):
        HW = self.bubble.width*Constants.BUBBLE_COLL_SIZE_COEF / 2
        if collisionCircleEllipse( (self.bubble.center_x, self.bubble.center_y) ,
                                   HW,
                                   center,
                                   radiusX, radiusY
                                   ):
            return True
        return False

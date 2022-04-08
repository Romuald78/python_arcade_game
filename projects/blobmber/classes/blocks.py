import random

import arcade

from projects.blobmber.classes.constants import Constants
from utils.collisions import collisionCircleAABB, collisionEllipseAABB, collisionCircleEllipse, collision2AABB
from utils.gfx_sfx import createAnimatedSprite, createFixedSprite


class Blocks():

    def __createBlock(self, x, y, w, h, clr):
        flip = [False, True][random.randint(0,1)]
        params = {
            "filePath": "projects/blobmber/images/rock_square.png",
            "position": (x, y),
            "size": (w, h),
            "filterColor": clr,
            "flipH": flip,
        }
        rock = createFixedSprite(params)
        rock.angle = random.randint(0,3)*90
        return rock

    def __init__(self, nbX, nbY, w, h, ofX, ofY):
        self.rocks = arcade.SpriteList()
        for x in range(nbX):
            for y in range(nbY):
                if x==0 or x==nbX-1 or y==0 or y==nbY-1 or (x%2==0 and y%2==0):
                    rock = self.__createBlock((x+0.5)*w + ofX, (y+0.5)*h + ofY, w, h, (255,255,255,255))
                    self.rocks.append( rock )

    def draw(self):
        for rock in self.rocks:
            rock.draw()
            if Constants.DEBUG_PHYSICS:
                arcade.draw_rectangle_outline(rock.center_x, rock.center_y, rock.width/Constants.BLOCKS_REDUCE_FACTOR, rock.height/Constants.BLOCKS_REDUCE_FACTOR, (255,255,255,255))

    def getList(self):
        return list(self.rocks)

    def isOvalColliding(self, center, radiusX, radiusY):
        HW = self.rocks[0].width  / Constants.BLOCKS_REDUCE_FACTOR / 2
        HH = self.rocks[0].height / Constants.BLOCKS_REDUCE_FACTOR / 2
        for rock in self.rocks:
            left   = rock.center_x - HW
            right  = rock.center_x + HW
            top    = rock.center_y + HH
            bottom = rock.center_y - HH
            if collisionEllipseAABB((left,top), (right,bottom), center, radiusX, radiusY):
                return True
        return False

    def isAABBColliding(self, tl, br):
        HW = self.rocks[0].width / Constants.BLOCKS_REDUCE_FACTOR / 2
        HH = self.rocks[0].height / Constants.BLOCKS_REDUCE_FACTOR / 2
        for rock in self.rocks:
            left   = rock.center_x - HW
            right  = rock.center_x + HW
            top    = rock.center_y + HH
            bottom = rock.center_y - HH
            if collision2AABB((left,top), (right,bottom), tl, br):
                return True
        return False

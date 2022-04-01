import random

import arcade

from projects.blobmber.classes.constants import Constants
from utils.collisions import collisionCircleAABB, collisionEllipseAABB, collisionCircleEllipse
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
            "flipV": flip,
        }
        rock = createFixedSprite(params)
        return rock

    def __init__(self, nbX, nbY, w, h, fullW, fullH):
        # compute X, Y offsets
        ofX = (fullW - nbX*w)/2
        ofY = (fullH - nbY*h)/2
        self.rocks = arcade.SpriteList()
        for x in range(0,nbX,2):
            for y in range(0,nbY,2):
                rock = self.__createBlock((x+0.5)*w + ofX, (y+0.5)*h + ofY, w, h, (255,255,255,255))
                self.rocks.append( rock )

    def draw(self):
        for rock in self.rocks:
            rock.draw()
            if Constants.DEBUG_PHYSICS:
                arcade.draw_rectangle_outline(rock.center_x, rock.center_y, rock.width/Constants.BLOCKS_REDUCE_FACTOR, rock.height/Constants.BLOCKS_REDUCE_FACTOR, (255,255,0,255))



    def isOvalColliding(self, center, radiusX, radiusY):
        HW = self.rocks[0].width / Constants.BLOCKS_REDUCE_FACTOR / 2
        HH = self.rocks[0].height / Constants.BLOCKS_REDUCE_FACTOR / 2
        for rock in self.rocks:
            left   = rock.center_x - HW
            right  = rock.center_x + HW
            top    = rock.center_y + HH
            bottom = rock.center_y - HH
            if collisionEllipseAABB((left,top), (right,bottom), center, radiusX, radiusY):
                return True
        return False

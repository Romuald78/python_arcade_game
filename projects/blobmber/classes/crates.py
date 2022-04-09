import random

import arcade

from projects.blobmber.classes.constants import Constants
from utils.collisions import collisionCircleAABB, collisionEllipseAABB, collisionCircleEllipse, collision2AABB
from utils.gfx_sfx import createAnimatedSprite, createFixedSprite


class Crates():

    def __createCrate(self, x, y, w, h, clr):
        flip = [False, True][random.randint(0,1)]
        params = {
            "filePath": "projects/blobmber/images/crate.png",
            "position": (x, y),
            "size": (w, h),
            "filterColor": clr,
            "flipH": flip,
        }
        crate = createFixedSprite(params)
        crate.angle = random.randint(0,3)*90
        # Add specific property : destroyState
        crate.destroyTime  = Constants.CRATE_DESTROY_TIME
        crate.destroyState = False
        return crate

    def __init__(self, nbX, nbY, w, h, ofX, ofY, playerInitPos):
        self.crates = arcade.SpriteList()
        for x in range(nbX):
            for y in range(nbY):
                if x!=0 and x!=nbX-1 and y!=0 and y!=nbY-1 and (x%2==1 or y%2==1):
                    addOK = True
                    for dx in range(-1,2,1):
                        for dy in range(-1, 2, 1):
                            if (x+dx, y+dy) in playerInitPos:
                                dx = 2
                                dy = 2
                                addOK = False
                    # DEBUG
                    if Constants.DEBUG_PHYSICS and random.random()<=0.85:
                        addOK = False
                    if addOK:
                        crate = self.__createCrate((x+0.5)*w + ofX, (y+0.5)*h + ofY, w, h, (255,255,255,255))
                        self.crates.append( crate )

    def update(self, deltaTime):
        toBeRemoved = []
        for crate in self.crates:
            if crate.destroyState:
                crate.destroyTime -= deltaTime
                if crate.destroyTime <= 0:
                    toBeRemoved.append(crate)
        # destroy all the crates to be
        for tbr in toBeRemoved:
            self.crates.remove(tbr)

    def draw(self):
        for crate in self.crates:
            crate.draw()
            if Constants.DEBUG_PHYSICS:
                arcade.draw_text(str(round(crate.destroyTime, 1)), crate.center_x, crate.center_y, (255, 255, 255))
                arcade.draw_rectangle_outline(crate.center_x, crate.center_y, crate.width/Constants.BLOCKS_REDUCE_FACTOR, crate.height/Constants.BLOCKS_REDUCE_FACTOR, (255,255,255,255))

    def getList(self):
        return list(self.crates)

    def isOvalColliding(self, center, radiusX, radiusY, destroy=False):
        if len(self.crates) == 0:
            return False
        HW = self.crates[0].width / Constants.BLOCKS_REDUCE_FACTOR / 2
        HH = self.crates[0].height / Constants.BLOCKS_REDUCE_FACTOR / 2
        for crate in self.crates:
            left   = crate.center_x - HW
            right  = crate.center_x + HW
            top    = crate.center_y + HH
            bottom = crate.center_y - HH
            if collisionEllipseAABB((left,top), (right,bottom), center, radiusX, radiusY):
                if destroy:
                    self.crates.remove(crate)
                return True
        return False

    def isAABBColliding(self, tl, br, destroy=False):
        if len(self.crates) == 0:
            return False
        HW = self.crates[0].width / Constants.BLOCKS_REDUCE_FACTOR / 2
        HH = self.crates[0].height / Constants.BLOCKS_REDUCE_FACTOR / 2
        for crate in self.crates:
            left   = crate.center_x - HW
            right  = crate.center_x + HW
            top    = crate.center_y + HH
            bottom = crate.center_y - HH
            if collision2AABB((left,top), (right,bottom), tl, br):
                if destroy:
                    crate.destroyState = True
                return True
        return False

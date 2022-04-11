import arcade

from projects.blobmber.classes.bubble import Bubble
from projects.blobmber.classes.constants import Constants
from utils.collisions import collision2Ellipses
from utils.gfx_sfx import createAnimatedSprite
from utils.trigo import rotate


class Blob():

    LEFT  = 0
    RIGHT = 1
    UP    = 2
    DOWN  = 3

    def __init__(self, x, y, w, h, clr):
        # Player Properties
        self.speed      = Constants.BLOB_MOVE_SPEED
        self.power      = 1
        self.countDown  = Constants.BUBBLE_COUNTDOWN
        self.maxBombs   = 1
        self.availBombs = 1
        self.disease    = None
        # Internal properties
        self.walking = [False,False,False,False]
        self.lastDir = Blob.DOWN
        self.walks   = [None,None,None,None]
        self.idles   = [None,None,None,None]
        self.radiusX = min(w,h)/Constants.BLOB_REDUCE_FACTOR
        self.radiusY = self.radiusX / Constants.BLOB_HW_RATIO
        self.color     = clr
        self.initColor = clr

        params = {
            "filePath": "projects/blobmber/images/blob.png",
            "position": (x, y),
            "size": (w, h),
            "spriteBox": (8, 3, 384, 384),
            "frameDuration": Constants.BLOB_FRAME_SPEED,
            "startIndex": 0,
            "endIndex": 7,
            "flipH": True
        }
        self.walks[Blob.DOWN] = createAnimatedSprite(params)
        params["startIndex"] = 8
        params["endIndex"] = 15
        self.walks[Blob.UP] = createAnimatedSprite(params)
        params["startIndex"] = 16
        params["endIndex"] = 23
        self.walks[Blob.LEFT] = createAnimatedSprite(params)
        params["flipH"] = False
        self.walks[Blob.RIGHT] = createAnimatedSprite(params)
        # IDLES
        params["startIndex"] = 0
        params["endIndex"] = 0
        params["flipH"] = True
        self.idles[Blob.DOWN] = createAnimatedSprite(params)
        params["startIndex"] = 8
        params["endIndex"] = 8
        self.idles[Blob.UP] = createAnimatedSprite(params)
        params["startIndex"] = 16
        params["endIndex"] = 16
        self.idles[Blob.LEFT] = createAnimatedSprite(params)
        params["flipH"] = False
        self.idles[Blob.RIGHT] = createAnimatedSprite(params)
        # CURRENT
        self.currentAnim = self.idles[Blob.DOWN]
        # position
        self.x = x
        self.y = y

    def addBomb(self):
        self.maxBombs   += 1
        self.availBombs += 1

    def addPower(self):
        self.power += 1

    def __getDirection(self):
        dx = 0
        dy = 0
        if self.walking[Blob.UP] != self.walking[Blob.DOWN]:
            dy = 1
            if self.walking[Blob.DOWN]:
                dy = -1
        if self.walking[Blob.LEFT] != self.walking[Blob.RIGHT]:
            dx = -1
            if self.walking[Blob.RIGHT]:
                dx = 1
        # Filter movement according to environment
        # # TODO use game rule object
        return (dx, dy)

    def __selectAnim(self, deltaTime):
        result = None
        if self.walking[Blob.LEFT] != self.walking[Blob.RIGHT]:
            result = self.walks[Blob.LEFT]
            if self.walking[Blob.RIGHT]:
                result = self.walks[Blob.RIGHT]
        elif self.walking[Blob.UP]!=self.walking[Blob.DOWN]:
            result = self.walks[Blob.UP]
            if self.walking[Blob.DOWN]:
                result = self.walks[Blob.DOWN]
        else:
            # Idle animation
            result = self.idles[self.lastDir]
        self.currentAnim = result
        self.currentAnim.update_animation(deltaTime)
        self.currentAnim.color = self.color

    @property
    def center_x(self):
        return self.x
    @property
    def center_y(self):
        return self.y
    @property
    def getradiusX(self):
        return self.radiusX
    @property
    def getradiusY(self):
        return self.radiusY

    def move(self, dir, isPressed):
        self.walking[dir] = isPressed
        self.lastDir = dir

    def __isNextStepOK(self, newX, newY, obstacles):
        for o in obstacles:
            # if we are already in collision, do not check
            if not o.isOvalColliding((self.x, self.y), self.radiusX, self.radiusY):
                if o.isOvalColliding((newX, newY), self.radiusX, self.radiusY):
                    return False
        # OK to move
        return True

    def __filterMove(self, diff, obstacles):
        # update movement
        dx, dy = diff
        newX = self.x + dx
        newY = self.y + dy
        newX2, newY2 = rotate((newX, newY), (self.x, self.y), -85)
        newX3, newY3 = rotate((newX,newY),(self.x,self.y),85)
        out = (self.x, self.y)
        if self.__isNextStepOK(newX, newY, obstacles):
            out = (newX, newY)
        elif self.__isNextStepOK(self.x, newY, obstacles) and dy != 0:
            out = (self.x, newY)
        elif self.__isNextStepOK(newX, self.y, obstacles) and dx != 0:
            out = (newX, self.y)
        elif self.__isNextStepOK(newX2, newY2, obstacles):
            out = (newX2, newY2)
        elif self.__isNextStepOK(newX3, newY3, obstacles):
            out = (newX3, newY3)
        # return diff
        return (out[0]-self.x, out[1]-self.y)

    def update(self, deltaTime, blocks, crates, bubbles, opponents):
        # select current anim
        self.__selectAnim(deltaTime)
        # get direction
        dx, dy = self.__getDirection()
        dx = dx * self.speed * deltaTime
        dy = dy * self.speed * deltaTime
        # Get all obstacles (crates, blocks, bubbles, opponents, ...)
        environment = []
        environment.append(blocks)
        environment.append(crates)
        environment += opponents
        environment += bubbles
        # Remove self object (from player list)
        if self in environment:
            environment.remove(self)
        # update movement
        diff  = (dx, dy)
        diff2 = self.__filterMove(diff, environment)
        if diff2 is not None:
            self.x += diff2[0]
            self.y += diff2[1]

        # update current anim position
        self.currentAnim.center_x = self.x
        self.currentAnim.center_y = self.y + self.radiusY/Constants.BLOB_Y_OFFSET

    def draw(self):
        self.currentAnim.draw()
        if Constants.DEBUG_PHYSICS:
            arcade.draw_ellipse_outline(self.x, self.y,2*self.radiusX, 2*self.radiusY,(0,0,0,160))

    def getCenter(self):
        return (self.x, self.y)

    def setColor(self, clr):
        self.color = clr
    def resetColor(self):
        self.color = self.initColor

    def isOvalColliding(self, c, r1, r2):
        return collision2Ellipses(c, r1, r2, (self.x, self.y), self.radiusX, self.radiusY)

    # return drop ref for upper layer
    def dropBubble(self, allBubbles, allBlocks, allCrates):
        if self.availBombs > 0:
            size = self.radiusX*2*Constants.BUBBLE_SIZE_COEF;
            # impossible to drop a bomb if another is colliding
            for bub in allBubbles:
                if bub.isOvalColliding( (self.x, self.y), self.radiusX, self.radiusY ):
                    return None
            # Ready to drop a bomb
            self.availBombs -= 1
            return Bubble( self.x, self.y, size, size, self.initColor, self.power, self.countDown, allBubbles, allBlocks, allCrates, self)

    def notifyExplosion(self):
        self.availBombs += 1

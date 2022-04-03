import random

from projects.blobmber.classes.constants import Constants
from utils.gfx_sfx import createAnimatedSprite, createFixedSprite


class SelectPlayer():


    def __init__(self, ctrlID, initPos):
        self.ctrlID = ctrlID
        params = {
            "filePath": "projects/blobmber/images/blob.png",
            "position": initPos,
            "spriteBox": (8, 3, 384, 384),
            "frameDuration": Constants.BLOB_FRAME_SPEED,
            "startIndex": 0,
            "endIndex": 7,
            "flipH": [True, False][random.randint(0,1)]
        }
        self.blob = createAnimatedSprite(params)
        params = {
             "filePath": "projects/blobmber/images/rockframe.png",
             "position": initPos,
        }
        self.frame = createFixedSprite(params)
        self.target = list(initPos)

    @property
    def center_x(self):
        return self.blob.center_x
    @property
    def center_y(self):
        return self.blob.center_y
    @property
    def color(self):
        return self.blob.color
    @center_x.setter
    def center_x(self, newX):
        self.blob.center_x = newX
    @center_y.setter
    def center_y(self, newY):
        self.blob.center_y = newY
    @color.setter
    def color(self, newC):
        self.blob.color = newC

    def update(self, deltaTime, anim=False):
        # Move to target
        self.blob.center_x = self.blob.center_x * 0.95 + self.target[0] * 0.05
        self.blob.center_y = self.blob.center_y * 0.95 + self.target[1] * 0.05
        # update anim
        if anim:
            self.blob.update_animation(deltaTime)
        # move all elements around blob
        self.frame.center_x = self.blob.center_x
        self.frame.center_y = self.blob.center_y

    def moveTo(self, x, y):
        self.target = [x, y]

    def draw(self):
        self.frame.draw()
        self.blob.draw()

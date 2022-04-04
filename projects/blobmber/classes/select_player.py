import random

import arcade.color

from projects.blobmber.classes.constants import Constants
from utils.gfx_sfx import createAnimatedSprite, createFixedSprite


class SelectPlayer():


    def __init__(self, ctrlID, initPos, dims):
        self.refW, self.refH = dims
        self.ctrlID = ctrlID
        params = {
            "filePath": "projects/blobmber/images/blob.png",
            "position": initPos,
            "size" : (self.refW*0.9, self.refH*0.9),
            "spriteBox": (8, 3, 384, 384),
            "frameDuration": Constants.BLOB_FRAME_SPEED,
            "startIndex": 0,
            "endIndex": 7,
            "flipH": [True, False][random.randint(0,1)]
        }
        self.blob = createAnimatedSprite(params)
        params = {
             "filePath": "projects/blobmber/images/rockframe.png",
            "size": (self.refW, self.refH),
            "position": initPos,
        }
        self.frame = createFixedSprite(params)
        fp = "gamepad"
        if ctrlID == Constants.KEYBOARD_CTRLID1 or ctrlID == Constants.KEYBOARD_CTRLID2:
            # TODO get keayboard icon
            fp = "gamepad"
        params = {
            "filePath": f"projects/blobmber/images/{fp}.png",
            "size": (self.refW/2, self.refH/2),
            "position": initPos,
        }
        self.pad = createFixedSprite(params)
        params = {
            "filePath": f"projects/blobmber/images/{fp}_outfill.png",
            "size": (self.refW/2, self.refH/2),
            "position": initPos,
        }
        self.pad_outfill = createFixedSprite(params)
        self.target = initPos

    @property
    def center_x(self):
        return self.blob.center_x
    @property
    def center_y(self):
        return self.blob.center_y
    @property
    def color(self):
        return self.blob.color
    @color.setter
    def color(self, newC):
        self.blob.color = newC
        self.pad.color  = newC
        self.pad_outfill.color  = arcade.color.WHITE

    def update(self, deltaTime, anim=False):
        # Move to target
        self.blob.center_x = self.blob.center_x * 0.95 + self.target[0] * 0.05
        self.blob.center_y = self.blob.center_y * 0.95 + self.target[1] * 0.05
        # update anim
        if anim:
            self.blob.update_animation(deltaTime)
        # move all elements around blob
        self.frame.center_x = self.blob.center_x + self.refW/7.5
        self.frame.center_y = self.blob.center_y - self.refH/50
        self.pad.center_x = self.blob.center_x + self.refW/2.5
        self.pad.center_y = self.blob.center_y - self.refH/6
        self.pad_outfill.center_x = self.pad.center_x
        self.pad_outfill.center_y = self.pad.center_y

    def moveTo(self, x, y):
        self.target = (x, y)

    def draw(self):
        self.frame.draw()
        self.pad.draw()
        self.pad_outfill.draw()
        self.blob.draw()

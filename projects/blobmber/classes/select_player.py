import random

import arcade.color

from projects.blobmber.classes.constants import Constants
from utils.gfx_sfx import createAnimatedSprite, createFixedSprite, utilsUpdateAnimation


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
        idx = 0
        if ctrlID == Constants.KEYBOARD_CTRLID1 or ctrlID == Constants.KEYBOARD_CTRLID2:
            # TODO get keyboard icon
            idx = 1
        params = {
            "filePath": "projects/blobmber/images/controllers_glow.png",
            "size": (self.refW/3, self.refH/3),
            "position": initPos,
            "spriteBox": (2,1,360,280),
            "startIndex":idx,
            "endIndex":idx,
        }
        self.pad = createAnimatedSprite(params)
        params["filePath"] = "projects/blobmber/images/controllers_line.png"
        self.pad_outfill = createAnimatedSprite(params)
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
        r = newC[0]
        g = newC[1]
        b = newC[2]
        Y = r*0.299 + g*0.587 + b*0.114
        Y = int(min(2*Y, 255))
        self.blob.color = newC
        self.pad.color = newC
        self.pad_outfill.color = (Y,Y,Y,128)

    def update(self, deltaTime, anim=False):
        # Move to target
        self.blob.center_x = self.blob.center_x * 0.95 + self.target[0] * 0.05
        self.blob.center_y = self.blob.center_y * 0.95 + self.target[1] * 0.05
        # update anim
        if anim:
            utilsUpdateAnimation(self.blob, deltaTime)
        else:
            self.blob.set_texture(0)

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
        ctrlID = self.ctrlID
        if ctrlID == Constants.KEYBOARD_CTRLID1:
            ctrlID = 1
        elif ctrlID == Constants.KEYBOARD_CTRLID2:
            ctrlID = 2
        ctrlID = str(ctrlID)
        arcade.draw_text(ctrlID, self.pad.center_x-self.refW*len(ctrlID)/25, self.pad.center_y+self.refH/10, self.pad.color, font_size=30, align="center")

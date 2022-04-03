import math

import arcade

from projects.blobmber.classes.blocks import Blocks
from projects.blobmber.classes.blob import Blob
from projects.blobmber.classes.constants import Constants
from utils.collisions import collisionCircleEllipse
from utils.gfx_sfx import createFixedSprite, createAnimatedSprite
from utils.trigo import rotate


class CyGameInGame():


    def __init__(self, W, H, cellSize, nbX, nbY, manager):
        super().__init__()
        self.W = W
        self.H = H
        self.S = cellSize
        self.NBX = nbX
        self.NBY = nbY
        self.manager = manager

    def setup(self):
        # key is ctrlID / Value is blob
        self.blobs = {}
        # list of blobs, sorted by Y
        self.blobsY = []
        w = self.S
        h = w
        w2 = w * Constants.BLOB_SIZE_COEF
        h2 = h * Constants.BLOB_SIZE_COEF
        # PLAYER 1
        blob = Blob(self.W//2, self.H//2, w2, h2, Constants.BLOB_COLORS[0])
        self.blobs[Constants.KEYBOARD_CTRLID1] = blob
        self.blobsY.append(blob)
        # PLAYER 2
        blob = Blob(self.W//2, self.H//2, w2, h2, Constants.BLOB_COLORS[1])
        self.blobs[Constants.KEYBOARD_CTRLID2] = blob
        self.blobsY.append(blob)
        # Rocks
        self.blocks = Blocks(self.NBX, self.NBY, w, h, self.W, self.H)
        # bubbles
        self.bubbles = []
        # Ground
        self.ground = arcade.SpriteList()
        for x in range(2):
            for y in range(2):
                params = {
                    "filePath": "projects/blobmber/images/ground.png",
                    "position": (x*self.W//2+self.W//4, y*self.H//2+self.H//4),
                    "size": (self.W/2, self.H/2),
                    "isMaxRatio" : True
                }
                tile = createFixedSprite(params)
                self.ground.append(tile)

    def update(self,deltaTime):
        # sort blobs by Y
        self.blobsY = sorted(self.blobsY, key=lambda blb: -blb.center_y )
        for blob in self.blobsY:
            blob.update(deltaTime, self.blocks, self.bubbles, self.blobsY)
        # Draw bubbles
        for bub in self.bubbles:
            bub.update(deltaTime)

#        if collisionCircleEllipse((1000,400), 150,
#                                  (self.blobs[Constants.KEYBOARD_CTRLID1].center_x,self.blobs[Constants.KEYBOARD_CTRLID1].center_y+Constants.BLOB_Y_OFFSET),
#                                  self.blobs[Constants.KEYBOARD_CTRLID1].radiusX, self.blobs[Constants.KEYBOARD_CTRLID1].radiusY):
#            self.blobs[Constants.KEYBOARD_CTRLID1].setColor( (255,255,255,255) )
#        else:
#            self.blobs[Constants.KEYBOARD_CTRLID1].setColor( (0,255,0,255) )


    def draw(self):
        # Draw ground
        self.ground.draw()
        # Draw blocks
        self.blocks.draw()
        # Draw bubbles
        for bub in self.bubbles:
            bub.draw()
        # for all players draw player and blocks below
        for i in range(len(self.blobs)):
            self.blobsY[i].draw()


    def onKeyEvent(self, key, isPressed):
        # Player 1
        if arcade.key.LEFT == key:
            self.blobs[Constants.KEYBOARD_CTRLID1].move(Blob.LEFT, isPressed)
        if arcade.key.RIGHT == key:
            self.blobs[Constants.KEYBOARD_CTRLID1].move(Blob.RIGHT, isPressed)
        if arcade.key.UP == key:
            self.blobs[Constants.KEYBOARD_CTRLID1].move(Blob.UP, isPressed)
        if arcade.key.DOWN == key:
            self.blobs[Constants.KEYBOARD_CTRLID1].move(Blob.DOWN, isPressed)
        if arcade.key.SPACE == key and isPressed:
            self.bubbles.append( self.blobs[Constants.KEYBOARD_CTRLID1].dropBubble() )
        # Player 2
        if arcade.key.Q == key:
            self.blobs[Constants.KEYBOARD_CTRLID2].move(Blob.LEFT, isPressed)
        if arcade.key.D == key:
            self.blobs[Constants.KEYBOARD_CTRLID2].move(Blob.RIGHT, isPressed)
        if arcade.key.Z == key:
            self.blobs[Constants.KEYBOARD_CTRLID2].move(Blob.UP, isPressed)
        if arcade.key.S == key:
            self.blobs[Constants.KEYBOARD_CTRLID2].move(Blob.DOWN, isPressed)
        if arcade.key.LCTRL == key and isPressed:
            self.bubbles.append( self.blobs[Constants.KEYBOARD_CTRLID2].dropBubble() )

    def onButtonEvent(self, gamepadNum, buttonName, isPressed):
        pass

    def onAxisEvent(self, gamepadNum, axisName, analogValue):
        pass


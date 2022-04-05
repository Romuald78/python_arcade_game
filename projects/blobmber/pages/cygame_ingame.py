import math

import arcade

from projects.blobmber.classes.blocks import Blocks
from projects.blobmber.classes.blob import Blob
from projects.blobmber.classes.constants import Constants
from projects.blobmber.classes.crates import Crates
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

    def setup(self, params=None):
        # key is ctrlID / Value is blob
        self.blobs = {}
        # list of blobs, sorted by Y
        self.blobsY = []
        w = self.S
        h = w
        w2 = w * Constants.BLOB_SIZE_COEF
        h2 = h * Constants.BLOB_SIZE_COEF
        # compute X, Y offsets
        ofX = (self.W - self.NBX * w) / 2
        ofY = (self.H - self.NBY * h) / 2

        # TODO shuffle positions

        # init list of start positions (for crate generation)
        initPos = []
        # CREATE ALL PLAYERS
        if params is not None:
            i = 0
            for param in params:
                x = Constants.BLOB_POS[i][0]
                y = Constants.BLOB_POS[i][1]
                initPos.append((x,y))
                clr    = param["color"]
                ctrlID = param["ctrlID"]
                blob = Blob((x + 0.5) * w + ofX, (y + 0.5) * w + ofY, w2, h2, clr)
                self.blobs[ctrlID] = blob
                self.blobsY.append(blob)
                i += 1

        # Rocks
        self.blocks = Blocks(self.NBX, self.NBY, w, h, ofX, ofY)
        # Crates
        self.crates = Crates(self.NBX, self.NBY, w, h, ofX, ofY, initPos)
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
            blob.update(deltaTime, self.blocks, self.crates, self.bubbles, self.blobsY)
        # update bubbles
        for bub in self.bubbles:
            bub.update(deltaTime)

    def draw(self):
        # Draw ground
        self.ground.draw()
        # Draw blocks
        self.blocks.draw()
        # Draw crates
        self.crates.draw()
        # Draw bubbles
        for bub in self.bubbles:
            bub.draw()
        # for all players draw player and blocks below
        for i in range(len(self.blobs)):
            self.blobsY[i].draw()

    def onKeyEvent(self, key, isPressed):
        # Player 1
        if arcade.key.LEFT == key:
            if Constants.KEYBOARD_CTRLID1 in self.blobs:
                self.blobs[Constants.KEYBOARD_CTRLID1].move(Blob.LEFT, isPressed)
        if arcade.key.RIGHT == key:
            if Constants.KEYBOARD_CTRLID1 in self.blobs:
                self.blobs[Constants.KEYBOARD_CTRLID1].move(Blob.RIGHT, isPressed)
        if arcade.key.UP == key:
            if Constants.KEYBOARD_CTRLID1 in self.blobs:
                self.blobs[Constants.KEYBOARD_CTRLID1].move(Blob.UP, isPressed)
        if arcade.key.DOWN == key:
            if Constants.KEYBOARD_CTRLID1 in self.blobs:
                self.blobs[Constants.KEYBOARD_CTRLID1].move(Blob.DOWN, isPressed)
        if arcade.key.SPACE == key and isPressed:
            if Constants.KEYBOARD_CTRLID1 in self.blobs:
                self.bubbles.append( self.blobs[Constants.KEYBOARD_CTRLID1].dropBubble() )
        # Player 2
        if arcade.key.Q == key:
            if Constants.KEYBOARD_CTRLID2 in self.blobs:
                self.blobs[Constants.KEYBOARD_CTRLID2].move(Blob.LEFT, isPressed)
        if arcade.key.D == key:
            if Constants.KEYBOARD_CTRLID2 in self.blobs:
                self.blobs[Constants.KEYBOARD_CTRLID2].move(Blob.RIGHT, isPressed)
        if arcade.key.Z == key:
            if Constants.KEYBOARD_CTRLID2 in self.blobs:
                self.blobs[Constants.KEYBOARD_CTRLID2].move(Blob.UP, isPressed)
        if arcade.key.S == key:
            if Constants.KEYBOARD_CTRLID2 in self.blobs:
                self.blobs[Constants.KEYBOARD_CTRLID2].move(Blob.DOWN, isPressed)
        if arcade.key.LCTRL == key and isPressed:
            if Constants.KEYBOARD_CTRLID2 in self.blobs:
                self.bubbles.append( self.blobs[Constants.KEYBOARD_CTRLID2].dropBubble() )

    def onButtonEvent(self, gamepadNum, buttonName, isPressed):
        pass

    def onAxisEvent(self, gamepadNum, axisName, analogValue):
        pass


import math
import random

import arcade

from projects.blobmber.classes.Items import Items
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
        self.isPaused = False

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

        self.items = Items(self.blobsY)
        for i in range(20):
            type = random.randint(0,5)
            x = random.randint(0,6)*2 + 1
            y = random.randint(0,6)*2 + 1
            self.items.addItem(x * w, y * h, w * Constants.RUNE_SIZE_RATIO, h * Constants.RUNE_SIZE_RATIO, type)

    def update(self,deltaTime):
        if not self.isPaused:
            # update all items
            self.items.update(deltaTime)
            # sort blobs by Y
            self.blobsY = sorted(self.blobsY, key=lambda blb: -blb.center_y )
            for blob in self.blobsY:
                blob.update(deltaTime, self.blocks, self.crates, self.bubbles, self.blobsY)
            # update bubbles
            toBeRemoved = []
            for bub in self.bubbles:
                bub.update(deltaTime)
                if bub.can_reap():
                    toBeRemoved.append(bub)
            for tbr in toBeRemoved:
                self.bubbles.remove(tbr)
            # update crates
            self.crates.update(deltaTime)

    def draw(self):
        # Draw ground
        self.ground.draw()
        # Draw runes
        self.items.draw()
        # Draw bubbles
        for bub in self.bubbles:
            bub.draw()
        # Draw blocks
        self.blocks.draw()
        # Draw crates
        self.crates.draw()
        # for all players draw player and blocks below
        for i in range(len(self.blobs)):
            self.blobsY[i].draw()


    def onKeyEvent(self, key, isPressed):
        if self.isPaused:
            if key == arcade.key.P and not isPressed:
                self.isPaused = False
        else:
            if key == arcade.key.P and not isPressed:
                self.isPaused = True

            # Player 1
            if arcade.key.NUM_4 == key:
                if Constants.KEYBOARD_CTRLID1 in self.blobs:
                    self.blobs[Constants.KEYBOARD_CTRLID1].move(Blob.LEFT, isPressed)
            if arcade.key.NUM_6 == key:
                if Constants.KEYBOARD_CTRLID1 in self.blobs:
                    self.blobs[Constants.KEYBOARD_CTRLID1].move(Blob.RIGHT, isPressed)
            if arcade.key.NUM_8 == key:
                if Constants.KEYBOARD_CTRLID1 in self.blobs:
                    self.blobs[Constants.KEYBOARD_CTRLID1].move(Blob.UP, isPressed)
            if arcade.key.NUM_5 == key:
                if Constants.KEYBOARD_CTRLID1 in self.blobs:
                    self.blobs[Constants.KEYBOARD_CTRLID1].move(Blob.DOWN, isPressed)
            if arcade.key.ENTER == key and isPressed:
                if Constants.KEYBOARD_CTRLID1 in self.blobs:
                    bub = self.blobs[Constants.KEYBOARD_CTRLID1].dropBubble(self.bubbles, self.blocks, self.crates)
                    if bub is not None:
                        self.bubbles.append( bub )
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
                    bub = self.blobs[Constants.KEYBOARD_CTRLID2].dropBubble(self.bubbles, self.blocks, self.crates)
                    if bub is not None:
                        self.bubbles.append( bub )

    def onButtonEvent(self, gamepadNum, buttonName, isPressed):
        pass

    def onAxisEvent(self, gamepadNum, axisName, analogValue):
        pass


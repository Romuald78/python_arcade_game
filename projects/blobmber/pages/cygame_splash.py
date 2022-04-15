import math
import random

import arcade

from projects.blobmber.classes.Word import Word
from projects.blobmber.classes.constants import Constants
from projects.blobmber.classes.select_player import SelectPlayer
from utils.gfx_sfx import createFixedSprite, createAnimatedSprite

class CyGameSplash():

    STATE_IDLE      = 0
    STATE_SELECTING = 1
    STATE_ALL_VALID = 2
    STATE_STARTING  = 3
    STATE_START     = 4

    def __init__(self, W, H, manager):
        super().__init__()
        self.W = W
        self.H = H
        self.manager = manager
        self.state = self.STATE_IDLE
        # Dict with ctrlID and color
        self.players = []

    def __goToGamePage(self, players):
        self.manager.selectPage(2,players)

    def __isRegistered(self, ctrlID):
        for p in self.players:
            if p["ctrlID"] == ctrlID:
                return True
        return False

    def __areAllValids(self):
        for p in self.players:
            if not p["valid"]:
                return False
        return True

    def __validPlayer(self, ctrlID):
        for p in self.players:
            if p["ctrlID"] == ctrlID:
                if not p["valid"]:
                    p["valid"] = True
                else:
                    # check if we can go into game
                    if self.__areAllValids():
                        self.__goToGamePage(self.players)

    def __changeColor(self, ctrlID, step):
        if self.state == self.STATE_SELECTING:
            if self.__isRegistered(ctrlID):
                for p in self.players:
                    if p["ctrlID"] == ctrlID:
                        if not p["valid"]:
                            p["colorSeed"] += step
                            random.seed(p["colorSeed"])
                            # set random color
                            r = random.randint(0, 255)
                            g = random.randint(0, 255)
                            b = random.randint(0, 255)
                            a = Constants.BLOB_ALPHA
                            clr = (r, g, b, a)
                            p["color"] = clr
                            p["sprite"].color = clr;
                        break

    def __movePlayers(self):
        # Set all player targets
        selectW = 1.05 * self.W / Constants.SELECT_RATIO
        selectH = self.H / Constants.SELECT_RATIO
        N = len(self.players)
        nbX = min(N, 4)
        y = self.H / 2
        x = self.W / 2.1 - (selectW * 0.5 * (nbX - 1))
        idx = 0
        for p in self.players:
            if idx % 4 == 0:
                x = self.W / 2.1 - (selectW * 0.5 * (nbX - 1))
            p["sprite"].moveTo(x, y)
            x += selectW
            if idx == 3:
                y -= selectH
            idx += 1

    def __unregisterPlayer(self, ctrlID):
        if self.state < self.STATE_STARTING:
            if self.__isRegistered(ctrlID):
                for p in self.players:
                    if p["ctrlID"] == ctrlID:
                        if p["valid"]:
                            p["valid"] = False
                            if self.state == self.STATE_ALL_VALID:
                                self.state = self.STATE_SELECTING
                        else:
                            self.players.remove( p )
                            if self.state == self.STATE_SELECTING:
                                if len(self.players) == 0:
                                    self.state = self.STATE_IDLE
                            self.__movePlayers()
                        break

    def __registerPlayer(self, ctrlID):
        if self.state < self.STATE_STARTING:
            if not self.__isRegistered(ctrlID):
                if len(self.players)<Constants.MAX_NB_PLAYERS:
                    clr = arcade.color.WHITE
                    selP = SelectPlayer(ctrlID, (self.W/2, -self.H), (self.W/Constants.SELECT_RATIO, self.H/Constants.SELECT_RATIO))
                    selP.color = clr
                    self.players.append( {"ctrlID":ctrlID, "colorSeed": random.randint(0,1000000), "color":clr, "sprite":selP, "valid":False} )
                    # change state
                    if self.state == self.STATE_IDLE:
                        self.state = self.STATE_SELECTING
                    # Set random color
                    self.__changeColor(ctrlID, 0)
                    self.__movePlayers()
            else:
                # player is registered : we put it into validated state
                self.__validPlayer(ctrlID)

    def __moveBack(self):
        T = 2*math.pi*self.time
        xc = self.W/4
        rx = self.W/17
        self.bigTopLeft.center_x = math.cos(T/23)*rx + xc
        xc = self.W/8
        rx = self.W/15
        yc = 5*self.H/6
        ry = self.H/15
        T += 73
        self.bigTopMid.center_x = math.cos(T/29)*rx + xc
        self.bigTopMid.center_y = math.cos(T/43)*ry + yc
        xc = self.W/2
        rx = self.W/4
        yc = self.H/10
        ry = self.H/17
        T += 53
        self.bottom.center_x = math.cos(T/31)*rx + xc
        self.bottom.center_y = math.cos(T/19)*ry + yc
        xc = 4*self.W/5
        rx = self.W/17
        yc = 10*self.H/11
        ry = self.H/17
        T += 17
        self.topRight.center_x = math.cos(T/17)*rx + xc
        self.topRight.center_y = math.cos(T/13)*ry + yc
        xc = 6*self.W/7
        rx = self.W/11
        yc = self.H/6
        ry = self.H/11
        T += 23
        self.bottomRight.center_x = math.cos(T / 25) * rx + xc
        self.bottomRight.center_y = math.cos(T / 41) * ry + yc

    def setup(self):
        self.time = 0
        self.title = Word(self.W/2,self.H/2.0,"Blobber Man", self.W/12,self.W/12, (128,255,128,200), True, True)
        self.title.center_x = self.W//13
        self.title.center_y = self.H//1.25

        self.pressStart = Word(self.W/10, self.H/10, "Press Start", self.W/20, self.W/14, (255,255,0,200), blinking=True)
        self.pressStart.center_x = self.W//4
        self.pressStart.center_y = self.H//2.25

        params = {
            "filePath": "projects/blobmber/images/big_lava_top_left.png",
            "position": (self.W/4, self.H/2),
            "size": (self.W/2, self.H),
            "isMaxRatio" : True,
            "filterColor": (255,0,0,160)
        }
        self.bigTopLeft = createFixedSprite(params)
        params = {
            "filePath": "projects/blobmber/images/big_lava_top_mid.png",
            "position": (self.W/5, 3*self.H/4),
            "size": (self.W/2, self.H/2),
            "isMaxRatio" : True,
            "filterColor": (0,0,255,160)
        }
        self.bigTopMid = createFixedSprite(params)
        params = {
            "filePath": "projects/blobmber/images/lava_bottom.png",
            "position": (self.W / 2, self.H / 10),
            "size": (self.W / 3, self.H / 3),
            "isMaxRatio": True,
            "filterColor": (0, 255, 255, 160)
        }
        self.bottom = createFixedSprite(params)
        params = {
            "filePath": "projects/blobmber/images/lava_top_right.png",
            "position": (3*self.W/4, 10*self.H / 11),
            "size": (self.W / 3, self.H / 3),
            "isMaxRatio": True,
            "filterColor": (128, 255, 0, 160)
        }
        self.topRight = createFixedSprite(params)
        params = {
            "filePath": "projects/blobmber/images/lava_bottom_left.png",
            "position": (self.W/3, self.H / 3),
            "size": (self.W / 2, self.H / 2),
            "isMaxRatio": True,
            "filterColor": (255, 0, 255, 160),
            "flipH" : True
        }
        self.bottomRight = createFixedSprite(params)
        params = {
            "filePath": "projects/blobmber/images/bg.png",
            "position": (self.W/2, self.H / 2),
            "size": (self.W, self.H),
            "isMaxRatio": True,
            "filterColor": (0, 255, 0, 160),
        }
        self.bg = createFixedSprite(params)


    def update(self,deltaTime):
        self.time += deltaTime
        self.title.update(deltaTime)
        self.pressStart.update(deltaTime)
        self.__moveBack()
        # update players
        for p in self.players:
            p["sprite"].update(deltaTime, p["valid"])

    def draw(self):
        self.bg.draw()
        self.topRight.draw()
        self.bigTopLeft.draw()
        self.bigTopMid.draw()
        self.bottom.draw()
        self.bottomRight.draw()
        self.title.draw()
        if self.time <= 3:
            alpha = int(255*(2.5-self.time)/3)
            arcade.draw_rectangle_filled(self.W//2, self.H//2, self.W, self.H, (0,0,0,alpha))
        if self.time >= 3 and self.state == self.STATE_IDLE:
            self.pressStart.draw()
        # display players
        if self.state >= self.STATE_SELECTING:
            for p in self.players:
                p["sprite"].draw()

    def onKeyEvent(self, key, isPressed):
        # Player 1 : keyboard
        if key == arcade.key.NUM_ENTER and not isPressed:
            self.__registerPlayer(Constants.KEYBOARD_CTRLID1)
        if key == arcade.key.BACKSPACE and not isPressed:
            self.__unregisterPlayer(Constants.KEYBOARD_CTRLID1)
        if key == arcade.key.NUM_4 and not isPressed:
            self.__changeColor(Constants.KEYBOARD_CTRLID1, -1)
        if key == arcade.key.NUM_6 and not isPressed:
            self.__changeColor(Constants.KEYBOARD_CTRLID1,  1)

        # Player 2 : keyboard
        if key == arcade.key.LCTRL and not isPressed:
            self.__registerPlayer(Constants.KEYBOARD_CTRLID2)
        if key == arcade.key.LSHIFT and not isPressed:
            self.__unregisterPlayer(Constants.KEYBOARD_CTRLID2)
        if key == arcade.key.Q and not isPressed:
            self.__changeColor(Constants.KEYBOARD_CTRLID2, -1)
        if key == arcade.key.D and not isPressed:
            self.__changeColor(Constants.KEYBOARD_CTRLID2,  1)

        # DEBUG
        if key == arcade.key.J and isPressed:
            self.__registerPlayer(1)
            self.__registerPlayer(2)
        if key == arcade.key.K and isPressed:
            self.__registerPlayer(3)
            self.__registerPlayer(4)
        if key == arcade.key.L and isPressed:
            self.__registerPlayer(5)
            self.__registerPlayer(6)


    def onButtonEvent(self, gamepadNum, buttonName, isPressed):
        print(gamepadNum, buttonName, isPressed)
        if not isPressed:
            pass


    def onAxisEvent(self, gamepadNum, axisName, analog):
        print(gamepadNum, axisName, analog)
import math

from projects.shmup.classes.Ship import Ship
from utils.gfx_sfx import createFixedSprite
from utils.trigo import rotate


class CyGameInGame():

    SHIP_SPEED = 500

    STATE_ENTERING = 0
    STATE_PLAYING  = 1
    STATE_EXITING  = 2

    def __moveShips(self):
        pass

    def __init__(self, W, H, manager):
        super().__init__()
        self.W = W
        self.H = H
        self.manager = manager

    def setup(self, params=None):
        if params is not None:
            self.players = []
            for p in params:
                ship = Ship(p["shipID"])
                player = {"ctrlID"  : p["ctrlID"],
                          "shipRef" : ship,
                          "score"   : 0,
                          "life"    : 100
                          }
                ship.center_x = -self.W/4
                ship.center_y = self.H//2
                self.players.append(player)

    def update(self,deltaTime):
        for p in self.players:
            ship = p["shipRef"]
            ship.update(deltaTime)
            ship.center_x = min(max(ship.center_x, 0),self.W)
            ship.center_y = min(max(ship.center_y, 0),self.H)

    def draw(self):
        for p in self.players:
            p["shipRef"].draw()

    def onKeyEvent(self, key, isPressed):
        pass

    def onButtonEvent(self, gamepadNum, buttonName, isPressed):
        pass

    def onAxisEvent(self, gamepadNum, axisName, analogValue):
        for p in self.players:
            if p["ctrlID"] == gamepadNum:
                if axisName == "X":
                    p["shipRef"].moveX(analogValue * CyGameInGame.SHIP_SPEED)
                elif axisName == "Y":
                    p["shipRef"].moveY(analogValue * CyGameInGame.SHIP_SPEED)
                break

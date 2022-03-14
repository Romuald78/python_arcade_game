import math

from utils.utils import createFixedSprite, rotate


class CyGameInGame():

    STATE_ENTERING = 0
    STATE_PLAYING  = 1
    STATE_EXITING  = 2

    def __init__(self, W, H, manager):
        super().__init__()
        self.W = W
        self.H = H
        self.manager = manager

    def setup(self):
        pass

    def update(self,deltaTime):
        pass

    def draw(self):
        pass

    def onKeyEvent(self, key, isPressed):
        pass

    def onButtonEvent(self, gamepadNum, buttonName, isPressed):
        pass

    def onAxisEvent(self, gamepadNum, axisName, analogValue):
        pass
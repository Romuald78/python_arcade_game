import math

from sources.cygame.Ship import Ship
from sources.utils import createFixedSprite


class CyGameSplash():

    def __init__(self, W, H):
        super().__init__()
        self.W = W
        self.H = H

    def setup(self):
        x0, y0 = self.W/2, self.H/2
        r = self.W/4
        self.player1   = Ship(1, (r*math.cos(0)+x0, r*math.sin(0)+y0))
        self.player2   = Ship(2, (r*math.cos(2*math.pi/3)+x0, r*math.sin(2*math.pi/3)+y0))
        self.player3   = Ship(3, (r*math.cos(4*math.pi/3)+x0, r*math.sin(4*math.pi/3)+y0))
        self.player12  = Ship(1, (r*math.cos(1*math.pi/3)+x0, r*math.sin(1*math.pi/3)+y0))
        self.player13  = Ship(1, (r*math.cos(5*math.pi/3)+x0, r*math.sin(5*math.pi/3)+y0))
        self.player23  = Ship(2, (r*math.cos(3*math.pi/3)+x0, r*math.sin(3*math.pi/3)+y0))
        self.player123 = Ship(1, (x0,y0))

        self.player12.mergeWith(2)
        self.player13.mergeWith(3)
        self.player23.mergeWith(3)
        self.player123.mergeWith(2)
        self.player123.mergeWith(3)


    def update(self,deltaTime):
        self.player1.update(deltaTime)
        self.player2.update(deltaTime)
        self.player3.update(deltaTime)
        self.player12.update(deltaTime)
        self.player13.update(deltaTime)
        self.player23.update(deltaTime)
        self.player123.update(deltaTime)

    def draw(self):
        self.player1.draw()
        self.player2.draw()
        self.player3.draw()
        self.player12.draw()
        self.player13.draw()
        self.player23.draw()
        self.player123.draw()


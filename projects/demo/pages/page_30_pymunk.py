import arcade.key

from projects.demo.classes.PhysicWorld import PhysicWorld
from utils.gfx_sfx import createFixedSprite


class Page30Pymunk():

    def __init__(self, W, H):
        super().__init__()
        self.W = W
        self.H = H

    def setup(self):
        self.phy = PhysicWorld(self.W, self.H)

    def update(self,deltaTime):
        self.phy.update(deltaTime)

    def draw(self):
        self.phy.draw()

    def onKeyEvent(self, key, isPressed):
        if key == arcade.key.SPACE and isPressed:
            self.phy.addCircle( (self.W/2, self.H/2), 50, type="ASTEROID" )
        if key == arcade.key.ENTER and isPressed:
            self.phy.addCircle( (self.W/2, self.H/2), 5, type="LASER" )



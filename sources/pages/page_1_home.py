from sources.classes.Chicken import Chicken
from sources.classes.Gems import Star
from sources.utils import *


class Page1Home():

    def __init__(self, W, H):
        super().__init__()
        self.W = W
        self.H = H

    def setup(self):
        # PYTHONS
        params = {
            "filePath"   : "images/misc/arcade.png",
            "position"   : (115,115),
            "filterColor": (255,255,255,96),
            "flipH" : True,
        }
        self.arcadeL  = createFixedSprite(params)
        params = {
            "filePath"   : "images/misc/arcade.png",
            "position"   : (self.W-115,self.H-115),
            "filterColor": (255,255,255,96),
        }
        self.arcadeR  = createFixedSprite(params)
        # BACKGROUND
        params = {
            "filePath"   : "images/misc/background_cytech.jpg",
            "position"   : (self.W//2,self.H//2),
            "size"       : (self.W,self.H),
            "filterColor": (128,200,255,128),
        }
        self.back = createFixedSprite(params)
        # CY TECH LOGO
        params = {
            "filePath"   : "images/misc/cytech.png",
            "position"   : (self.W//2,self.H//2),
            "size"       : (310*2,163*2),
            "filterColor": (255,255,255,160),
        }
        self.cytech = createFixedSprite(params)
        # PARTICLE EMITTER
        colors = [(randint(0,5),randint(0,2)) for x in range(4)]
        self.starEmitters = [Star(self.W, self.H, colors[i]) for i in range(len(colors))]
        # Chicken
        self.chicken = Chicken(self.W, self.H)

    def update(self,deltaTime):
        # update particles
        for star in self.starEmitters:
            star.update(deltaTime)
        self.chicken.update(deltaTime)

    def draw(self):
        self.cytech.draw()
        self.back.draw()
        for star in self.starEmitters:
            star.draw()
        self.arcadeL.draw()
        self.arcadeR.draw()
        self.chicken.draw()

from projects.demo.classes.Chicken import Chicken
from projects.demo.classes.Gems import Star
from utils.gfx_sfx import *


class Page1Home():

    def __init__(self, W, H):
        super().__init__()
        self.W = W
        self.H = H

    def setup(self):
        # PYTHONS
        params = {
            "filePath"   : "projects/demo/images/misc/arcade.png",
            "position"   : (115,115),
            "size" : (self.W//4, self.H//4),
            "filterColor": (255,255,255,128),
            "flipH" : True,
        }
        self.arcadeL  = createFixedSprite(params)
        params = {
            "filePath"   : "projects/demo/images/misc/arcade.png",
            "position"   : (self.W-115,self.H-115),
            "size": (self.W // 4, self.H // 4),
            "filterColor": (255,255,255,128),
        }
        self.arcadeR  = createFixedSprite(params)
        # BACKGROUND
        params = {
            "filePath"   : "projects/demo/images/misc/background_cytech.jpg",
            "position"   : (self.W//2,self.H//2),
            "size"       : (self.W,self.H),
            "isMaxRatio"   : True,
            "filterColor": (160,220,255,160),
        }
        self.back = createFixedSprite(params)
        # CY TECH LOGO
        params = {
            "filePath"   : "projects/demo/images/misc/cytech.png",
            "position"   : (self.W//2,self.H//2),
            "size"       : (self.W//3,self.W//4),
            "filterColor": (255,255,255,192),
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

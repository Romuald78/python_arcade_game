from utils.gfx_sfx import createFixedSprite
import arcade


class Page2bColor():

    def __init__(self, W, H):
        super().__init__()
        self.W = W
        self.H = H

    def setup(self):
        params = {
            "filePath"   : "projects/demo/images/backgrounds/city.png",
            "position"   : (self.W//2,self.H//2),
            # ----------------------------------------
            "size"       : (self.W,self.H),
            "isMaxRatio" : True,
            "filterColor": (255,255,255,255),
            "flipH"      : False,
            "flipV"      : False,
        }
        self.back = createFixedSprite(params)
        params = {
            "filePath"   : "projects/demo/images/characters/chicken.png",
            "position"   : (self.W//2,self.H//2),
            # ----------------------------------------
            "size"       : (self.W,self.H),
            "isMaxRatio" : True,
            "filterColor": (255,255,255,255),
            "flipH"      : False,
            "flipV"      : False,
        }
        self.skull = createFixedSprite(params)
        self.R = False
        self.G = False
        self.B = False
        self.A = False
        self.UP = False
        self.DOWN = False

    def update(self,deltaTime):
        if self.UP != self.DOWN:
            step = 3
            if self.DOWN:
                step = -step
            # prepare color
            r, g, b = self.skull.color
            a = self.skull.alpha
            # update rgba
            if self.R:
                r += step
            if self.G:
                g += step
            if self.B:
                b += step
            if self.A:
                a += step
            # update color if needed
            r = max(min(r, 255), 0)
            g = max(min(g, 255), 0)
            b = max(min(b, 255), 0)
            a = max(min(a, 255), 0)
            self.skull.color = (int(r), int(g), int(b))
            self.skull.alpha = int(a)


    def draw(self):
        self.back.draw()
        self.skull.draw()


    def onKeyEvent(self, key, isPressed):
        # Check components
        if key== arcade.key.R:
            self.R = isPressed
        if key == arcade.key.G:
            self.G = isPressed
        if key == arcade.key.B:
            self.B = isPressed
        if key== arcade.key.A:
            self.A = isPressed
        # check up and down
        if key == arcade.key.UP:
            self.UP = isPressed
        if key == arcade.key.DOWN:
            self.DOWN = isPressed

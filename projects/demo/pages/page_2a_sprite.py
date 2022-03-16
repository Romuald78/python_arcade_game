from utils.gfx_sfx import createFixedSprite


class Page2Sprite():

    def __init__(self, W, H):
        super().__init__()
        self.W = W
        self.H = H

    def setup(self):
        # BACKGROUND
        params = {
            "filePath"   : "projects/demo/images/backgrounds/cake.png",
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
            "filePath"   : "projects/demo/images/characters/penguin_fix.png",
            "position"   : (self.W//1.5,self.H//3),
            # ----------------------------------------
            "size"       : (self.W//4,self.H//4),
            "isMaxRatio" : True,
            "filterColor": (255,255,255,255),
            "flipH"      : True,
            "flipV"      : False,
        }
        self.penguin = createFixedSprite(params)


    def update(self,deltaTime):
        pass

    def draw(self):
        self.back.draw()
        self.penguin.draw()

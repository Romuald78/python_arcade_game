from sources.utils import createFixedSprite


class Page2Sprite():

    def __init__(self, W, H):
        super().__init__()
        self.W = W
        self.H = H

    def setup(self):
        # BACKGROUND
        params = {
            "filePath"   : "images/backgrounds/cake.png",
            "position"   : (self.W//2,self.H//2),
            # ----------------------------------------
            "size"       : (self.W,self.H),
            "isMaxRatio" : False,
            "filterColor": (255,255,255,255),
            "flipH"      : False,
            "flipV"      : False,
        }
        self.back = createFixedSprite(params)


    def update(self,deltaTime):
        pass

    def draw(self):
        self.back.draw()

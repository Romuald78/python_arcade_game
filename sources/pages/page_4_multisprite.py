from sources.utils import createAnimatedSprite


class Page4Multi():

    def __init__(self, W, H):
        super().__init__()
        self.W = W
        self.H = H

    def setup(self):
        # ANIMATED SPRITE
        params = {
            "filePath"     : "images/fonts/font1.png",
            "spriteBox"    : (8, 5, 30, 40),
            "size"         : (60,80),
            "position"     : (self.W//2, self.H//2),
            "startIndex"   : 26,
            "endIndex"     : 35,
            "frameDuration": 1 / 3,
            "filterColor"  : (255, 255, 255, 255),
            "flipH"        : False,
        }
        self.digits = []
        self.digits.append(createAnimatedSprite(params))
        params["position"] = (self.W//2+60, self.H//2)
        self.digits.append(createAnimatedSprite(params))
        params["position"] = (self.W//2+120, self.H//2)
        self.digits.append(createAnimatedSprite(params))
        self.count = 0

    def update(self,deltaTime):
        self.count += deltaTime*3
        value = int(self.count)
        self.digits[2].set_texture((value-1)%10)
        self.digits[1].set_texture(((value//10)-1)%10)
        self.digits[0].set_texture(((value//100)-1)%10)

    def draw(self):
        for d in self.digits:
            d.draw()




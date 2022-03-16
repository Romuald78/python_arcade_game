from utils.gfx_sfx import createAnimatedSprite
import arcade

class Page4Multi():

    def __init__(self, W, H):
        super().__init__()
        self.W = W
        self.H = H

    def setup(self):
        # ANIMATED SPRITE
        params = {
            "filePath"     : "projects/demo/images/fonts/font1.png",
            "spriteBox"    : (8, 5, 30, 40),
            "size"         : (self.W//4,self.H//4),
            "position"     : (self.W//2, self.H//2.5),
            "startIndex"   : 26,
            "endIndex"     : 35,
            "frameDuration": 1 / 3,
            "filterColor"  : (255, 255, 255, 255),
            "flipH"        : False,
        }
        self.digits = []
        self.digits.append(createAnimatedSprite(params))
        params["position"] = (self.W//2-self.W/7, self.H//2.5)
        self.digits.append(createAnimatedSprite(params))
        params["position"] = (self.W//2+self.W/7, self.H//2.5)
        self.digits.append(createAnimatedSprite(params))
        self.count = 0

        params["position"] = (self.W//2, 3*self.H//4)
        self.monoDigit = createAnimatedSprite(params)
        self.count2 = 0

    def update(self,deltaTime):
        self.monoDigit.set_texture(self.count2)

        self.count += deltaTime*3
        value = int(self.count)
        self.digits[2].set_texture((value-1)%10)
        self.digits[0].set_texture(((value//10)-1)%10)
        self.digits[1].set_texture(((value//100)-1)%10)

    def draw(self):
        self.monoDigit.draw()
        for d in self.digits:
            d.draw()


    def onKeyEvent(self, key, isPressed):
        # check up and down
        if key == arcade.key.UP and isPressed:
            self.count2 = (self.count2 + 1)%10
        if key == arcade.key.DOWN and isPressed:
            self.count2 = (self.count2 - 1) % 10




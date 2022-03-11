from utils.utils import createAnimatedSprite
from random import randint


class Page5Rotation():

    def __init__(self, W, H):
        super().__init__()
        self.W = W
        self.H = H

    def getParams(self):
        # ANIMATED SPRITE
        idx = randint(0, 3) + randint(0,2)
        x = randint(0, self.W)
        y = randint(0, self.H)
        params = {
            "filePath": "projects/demo/images/items/candies.png",
            "spriteBox": (3, 2, 128, 128),
            "position": (x, y),
            "startIndex": idx,
            "endIndex": idx,
            "frameDuration": 1 / 10,
            "filterColor": (255, 255, 255, 192),
            "flipH": False,
        }
        return params

    def setup(self):
        self.anims = []
        for i in range(100):
            self.anims.append(createAnimatedSprite(self.getParams()))

    def update(self,deltaTime):
        for i in range(len(self.anims)):
            self.anims[i].angle += i/10 + 1

    def draw(self):
        for a in self.anims:
            a.draw()

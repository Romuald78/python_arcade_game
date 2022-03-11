from utils.utils import createAnimatedSprite


class Page3Anim():

    def __init__(self, W, H):
        super().__init__()
        self.W = W
        self.H = H

    def setup(self):
        # ANIMATED SPRITE
        params = {
            "filePath": "projects/demo/images/characters/troll.png",
            "spriteBox": (5, 1, 400, 250),
            "position": (self.W//2, self.H//2),
            "startIndex": 1,
            "endIndex": 4,
            "size":(self.W//2, self.H//2),
            "frameDuration": 1 / 10,
            "filterColor": (255, 255, 255, 255),
            "flipH": False,
        }
        self.anim = createAnimatedSprite(params)

    def update(self,deltaTime):
        self.anim.update_animation(deltaTime)

    def draw(self):
        self.anim.draw()

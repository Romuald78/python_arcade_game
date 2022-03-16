from utils.gfx_sfx import createAnimatedSprite


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
            "position": (self.W//4, self.H//3.5),
            "startIndex": 1,
            "endIndex": 4,
            "size":(self.W//2, self.H//2),
            "frameDuration": 1 / 10,
            "filterColor": (255, 255, 255, 255),
            "flipH": False,
        }
        self.troll = createAnimatedSprite(params)
        params = {
            "filePath": "projects/demo/images/characters/girl.png",
            "spriteBox": (7, 1, 170, 250),
            "position": (4*self.W//5, self.H//3),
            "startIndex": 1,
            "endIndex": 6,
            "size":(self.W//2.5, self.H//2.5),
            "isMaxRatio" : False,
            "frameDuration": 1 / 8,
            "filterColor": (255, 255, 255, 255),
            "flipH": True,
        }
        self.girl = createAnimatedSprite(params)
        params = {
            "filePath": "projects/demo/images/characters/chicken.png",
            "spriteBox": (4, 4, 192, 192),
            "position": (3*self.W//5, 3*self.H//4),
            "startIndex": 0,
            "endIndex": 7,
            "size":(self.W//2, self.H//2),
            "frameDuration": 1 / 25,
            "filterColor": (255, 255, 255, 255),
            "flipH": True,
        }
        self.chicken = createAnimatedSprite(params)

    def update(self,deltaTime):
        self.troll.update_animation(deltaTime)
        self.girl.update_animation(deltaTime)
        self.chicken.update_animation(deltaTime)

    def draw(self):
        self.troll.draw()
        self.girl.draw()
        self.chicken.draw()

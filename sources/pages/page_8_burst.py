import random

from sources.utils import createParticleBurst


class Page8Burst():

    def __init__(self, W, H):
        super().__init__()
        self.W = W
        self.H = H

    def __createBurst(self, x, y):
        params = {
            "position": (x, y),
            "filePath": "images/items/star.png",
            "spriteBox": (1, 1, 128, 128),
            "spriteSelect": (0, 0),

            "partSize": 128,
            "partScale": 2.0,
            "partSpeed": 5.0,
            "filterColor": (255, 255, 255, 255),
            "startAlpha": 100,
            "endAlpha": 25,

            "partInterval": 0.05,
            "totalDuration": 0.4,
        }
        burst = createParticleBurst(params)
        self.bursts.append(burst)

    def setup(self):
        # PARTICLE BURST
        self.bursts = []
        self.timer = 0

    def update(self,deltaTime):
        self.timer += deltaTime
        if self.timer > 0.4:
            self.timer -= 0.4
            x = random.randint(0, self.W)
            y = random.randint(0, self.H)
            self.__createBurst(x,y)

        for b in self.bursts:
            b.update()
            if b.can_reap():
                self.bursts.remove(b)

    def draw(self):
        for b in self.bursts:
            b.draw()

    def onMouseButtonEvent(self, x, y, buttonNum, isPressed):
        if isPressed:
            self.__createBurst(x, y)

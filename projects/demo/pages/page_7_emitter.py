from utils.utils import createParticleEmitter


class Page7Emitter():

    def __init__(self, W, H):
        super().__init__()
        self.W = W
        self.H = H

    def setup(self):
        # PARTICLE EMITTER
        params = {
            "position" : (self.W/2, self.H/2),
            "filePath": "projects/demo/images/items/star.png",
            "spriteBox": (1, 1, 128, 128),
            "spriteSelect": (0, 0),

            "partSize": 128,
            "partScale": 2.0,
            "partSpeed": 4.0,
            "filterColor": (255, 255, 255, 255),
            "startAlpha": 100,
            "endAlpha": 0,

            "partNB": 50,
            "maxLifeTime": 1.0,
        }
        self.emitter = createParticleEmitter(params)

    def update(self,deltaTime):
        self.emitter.update()

    def draw(self):
        self.emitter.draw()

    def onMouseMotionEvent(self, x, y, dx, dy):
        self.emitter.center_x = x
        self.emitter.center_y = y


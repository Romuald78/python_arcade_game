import random

import arcade.key

from utils.utils import createFixedSprite, collision2Circles, collisionPointAABB, collision2AABB, collisionCircleAABB


class Page9Collisions():

    def __init__(self, W, H):
        super().__init__()
        self.W = W
        self.H = H

    def setup(self):
        # PYTHONS
        self.radius1 = self.W/9
        self.radius2 = 100
        params = {
            "filePath": "projects/demo/images/misc/colorsquare.png",
            "position": (self.W - self.radius1, self.H // 2),
            "size": (self.radius1*2, self.radius1*2),
            "filterColor": (255, 255, 255, 64)
        }
        self.bg = createFixedSprite(params)

        params = {
            "filePath": "projects/demo/images/misc/green_circle.png",
            "position": (self.radius1, self.H // 2),
            "size"       : (self.radius1*2, self.radius1*2),
            "filterColor": (255, 255, 255, 255)
        }
        self.green = createFixedSprite(params)

        params = {
            "filePath": "projects/demo/images/misc/colorsquare.png",
            "position": (self.W // 2, self.H // 4),
            "size": (self.radius1*2, self.radius1*2),
            "filterColor": (255, 255, 255, 64)
        }
        self.bg2 = createFixedSprite(params)

        params = {
            "filePath": "projects/demo/images/misc/blue_circle.png",
            "position": (self.W // 2, self.H // 2),
            "size"       : (self.radius2*2, self.radius2*2),
            "filterColor": (255, 255, 255, 160)
        }
        self.blue = createFixedSprite(params)

        params = {
            "filePath": "projects/demo/images/misc/colorsquare.png",
            "position": (self.W // 2, self.H // 2),
            "size"       : (self.radius2*2, self.radius2*2),
            "filterColor": (255, 255, 255, 160)
        }
        self.blue2 = createFixedSprite(params)

        self.shape = False
        self.colliding1 = False
        self.colliding2 = False
        self.colliding3 = False


    def update(self,deltaTime):
        # Circle collisions
        self.colliding1 = collision2Circles((self.blue.center_x, self.blue.center_y), self.radius2,
                                            (self.green.center_x, self.green.center_y), self.radius1)
        # Square collisions
        tl1 = (self.blue2.center_x - self.radius2, self.blue2.center_y + self.radius2)
        br1 = (self.blue2.center_x + self.radius2, self.blue2.center_y - self.radius2)
        tl2 = (self.bg.center_x   - self.radius1, self.bg.center_y   + self.radius1)
        br2 = (self.bg.center_x   + self.radius1, self.bg.center_y   - self.radius1)
        self.colliding2 = collision2AABB(tl1, br1, tl2, br2)

        tl3 = (self.bg2.center_x   - self.radius1, self.bg2.center_y   + self.radius1)
        br3 = (self.bg2.center_x   + self.radius1, self.bg2.center_y   - self.radius1)
        center3 = (self.blue.center_x, self.blue.center_y)
        self.colliding3 = collisionCircleAABB( tl3, br3, center3, self.radius2 )

        if self.colliding1:
            self.green.color = (255,255,255,255)
        else:
            self.green.color = (255, 255, 255, 128)
        if self.colliding2:
            self.bg.color = (255,255,255,255)
        else:
            self.bg.color = (255, 255, 255, 128)
        if self.colliding3:
            self.bg2.color = (255,255,255,255)
        else:
            self.bg2.color = (255, 255, 255, 128)

    def draw(self):
        self.green.draw()
        self.bg.draw()
        self.bg2.draw()
        # Collision with blue SQUARE
        if self.shape:
            self.blue2.draw()
        # Collision with blue CIRCLE
        else:
            self.blue.draw()

    def onKeyEvent(self, key ,isPressed):
        if key == arcade.key.SPACE and isPressed:
            self.shape = not self.shape

    def onMouseMotionEvent(self, x, y, dx, dy):
        self.blue.center_x  = x
        self.blue.center_y  = y
        self.blue2.center_x = x
        self.blue2.center_y = y


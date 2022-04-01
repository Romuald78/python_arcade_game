import arcade.key
from utils.collisions import collision2Circles, collisionPointAABB, collision2AABB, collisionCircleAABB, \
    collisionCircleEllipse, collisionEllipseAABB, collision2Ellipses
from utils.gfx_sfx import createFixedSprite

class Page9Collisions():

    STATE_CIRCLE_CIRCLE   = 0
    STATE_CIRCLE_SQUARE   = 1
    STATE_SQUARE_SQUARE   = 2
    STATE_ELLIPSE_CIRCLE  = 3
    STATE_ELLIPSE_SQUARE  = 4
    STATE_ELLIPSE_ELLIPSE = 5
    NB_STATES             = 6

    def __init__(self, W, H):
        super().__init__()
        self.W = W
        self.H = H

    def setup(self):
        # PYTHONS
        self.rU = self.W / 10
        self.rC = 2*self.rU

        # =====================================================
        # user shapes
        # =====================================================
        params = {
            "filePath": "projects/demo/images/misc/green_circle.png",
            "position": (self.W//2, self.H // 2),
            "size"       : (self.rU*2, self.rU*2),
            "filterColor": (255, 255, 255, 160)
        }
        self.userCircle = createFixedSprite(params)
        params = {
            "filePath": "projects/demo/images/misc/colorsquare.png",
            "position": (self.W // 2, self.H // 2),
            "size": (self.rU*2, self.rU*2),
            "filterColor": (255, 255, 255, 160)
        }
        self.userSquare = createFixedSprite(params)
        params = {
            "filePath": "projects/demo/images/misc/ellipse.png",
            "position": (self.W // 2, self.H // 2),
            "size": (self.rU*2, self.rU),
            "filterColor": (255, 255, 255, 160)
        }
        self.userEllipse = createFixedSprite(params)


        # =====================================================
        # collisions shapes
        # =====================================================
        params = {
            "filePath": "projects/demo/images/misc/blue_circle.png",
            "position": (self.W // 2, self.H // 2),
            "size"       : (self.rC*2, self.rC*2),
            "filterColor": (255, 255, 255, 255)
        }
        self.circle = createFixedSprite(params)
        params = {
            "filePath": "projects/demo/images/misc/colorsquare.png",
            "position": (self.W // 2, self.H // 2),
            "size"       : (self.rC*2, self.rC*2),
            "filterColor": (255, 255, 255, 255)
        }
        self.square = createFixedSprite(params)
        params = {
            "filePath": "projects/demo/images/misc/ellipse.png",
            "position": (self.W // 2, self.H // 2),
            "size": (self.rC*2, self.rC),
            "filterColor": (255, 255, 255, 160)
        }
        self.ellipse = createFixedSprite(params)

        self.state = 0
        self.colliding = False
        self.x = 0
        self.y = 0


    def update(self,deltaTime):
        # update positions
        self.userCircle.center_x  = self.x
        self.userCircle.center_y  = self.y
        self.userSquare.center_x  = self.x
        self.userSquare.center_y  = self.y
        self.userEllipse.center_x  = self.x
        self.userEllipse.center_y  = self.y


        if self.state == self.STATE_CIRCLE_CIRCLE:
            self.colliding = collision2Circles((self.x, self.y), self.rU, (self.W//2, self.H//2), self.rC)
        elif self.state == self.STATE_CIRCLE_SQUARE:
            tl3 = (self.W//2 - self.rC, self.H//2 + self.rC)
            br3 = (self.W//2 + self.rC, self.H//2 - self.rC)
            center3 = (self.x, self.y)
            self.colliding = collisionCircleAABB(tl3, br3, center3, self.rU)
        elif self.state == self.STATE_SQUARE_SQUARE:
            tl1 = (self.x - self.rU, self.y + self.rU)
            br1 = (self.x + self.rU, self.y - self.rU)
            tl2 = (self.W//2 - self.rC, self.H//2 + self.rC)
            br2 = (self.W//2 + self.rC, self.H//2 - self.rC)
            self.colliding = collision2AABB(tl1, br1, tl2, br2)
        elif self.state == self.STATE_ELLIPSE_CIRCLE:
            self.colliding = collisionCircleEllipse((self.W//2, self.H//2), self.rC, (self.x, self.y), self.rU, self.rU/2)
        elif self.state == self.STATE_ELLIPSE_SQUARE:
            tl3 = (self.W // 2 - self.rC, self.H // 2 + self.rC)
            br3 = (self.W // 2 + self.rC, self.H // 2 - self.rC)
            self.colliding = collisionEllipseAABB(tl3, br3, (self.x, self.y), self.rU, self.rU/2)
        elif self.state == self.STATE_ELLIPSE_ELLIPSE:
            self.colliding = collision2Ellipses((self.W//2, self.H//2), self.rC, self.rC/2, (self.x, self.y), self.rU, self.rU/2)


        if self.colliding:
            self.circle.color = (255, 255, 255, 255)
            self.square.color = (255, 255, 255, 255)
            self.ellipse.color = (255, 255, 255, 255)
        else:
            self.circle.color = (255, 255, 255, 64)
            self.square.color = (255, 255, 255, 64)
            self.ellipse.color = (255, 255, 255, 64)

    def draw(self):
        if self.state == self.STATE_CIRCLE_CIRCLE:
            self.circle.draw()
            self.userCircle.draw()

        elif self.state == self.STATE_CIRCLE_SQUARE:
            self.square.draw()
            self.userCircle.draw()

        elif self.state == self.STATE_SQUARE_SQUARE:
            self.square.draw()
            self.userSquare.draw()
        elif self.state == self.STATE_ELLIPSE_CIRCLE:
            self.circle.draw()
            self.userEllipse.draw()
        elif self.state == self.STATE_ELLIPSE_SQUARE:
            self.square.draw()
            self.userEllipse.draw()
        elif self.state == self.STATE_ELLIPSE_ELLIPSE:
            self.ellipse.draw()
            self.userEllipse.draw()

    def onKeyEvent(self, key ,isPressed):
        if key == arcade.key.SPACE and isPressed:
            self.state = (self.state+1) % self.NB_STATES


    def onMouseMotionEvent(self, x, y, dx, dy):
        self.x = x
        self.y = y


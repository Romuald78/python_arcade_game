import arcade.key

from utils.gfx_sfx import createAnimatedSprite, createFixedSprite


class Page6Move():

    def __init__(self, W, H):
        super().__init__()
        self.W = W
        self.H = H

    def setup(self):
        # ANIMATED SPRITES
        params = {
            "filePath": "projects/demo/images/characters/ninja.png",
            "spriteBox": (7, 1, 120, 120),
            "size"     : (self.W//3,self.H//3),
            "position": (self.W//2, self.H//2),
            "startIndex": 1,
            "endIndex": 6,
            "frameDuration": 1 / 25,
            "filterColor": (255, 255, 255, 255),
            "flipH": False,
        }
        self.runR = createAnimatedSprite(params)
        params["flipH"] = True
        self.runL = createAnimatedSprite(params)

        params = {
            "filePath": "projects/demo/images/parallax/night/night6.png",
            "size": (self.W, self.H),
            "position": (self.W // 2, self.H // 2),
            "isMaxRatio": True,
            "filterColor": (255, 255, 255, 128),
            "flipH": False,
        }
        self.bg6 = createFixedSprite(params)
        params = {
            "filePath": "projects/demo/images/parallax/night/night5.png",
            "size": (self.W, self.H),
            "position": (self.W // 1.8, self.H // 2),
            "isMaxRatio": True,
            "filterColor": (255, 200, 160, 160),
            "flipH": False,
        }
        self.bg5 = createFixedSprite(params)
        params = {
            "filePath": "projects/demo/images/parallax/night/night2.png",
            "size": (self.W, self.H),
            "position": (self.W // 2, self.H // 2),
            "isMaxRatio": True,
            "filterColor": (255, 255, 255, 255),
            "flipH": False,
        }
        self.bg2 = createFixedSprite(params)
        params = {
            "filePath": "projects/demo/images/parallax/night/night1.png",
            "size": (self.W, self.H),
            "position": (self.W // 2, self.H // 2),
            "isMaxRatio": True,
            "filterColor": (128, 128, 128, 255),
            "flipH": False,
        }
        self.bg1 = createFixedSprite(params)

        # FIXED SPRITES
        params = {
            "filePath": "projects/demo/images/characters/ninja_fix.png",
            "size"     : (self.W//3,self.H//3),
            "position": (self.W // 2, self.H // 3.5),
            "filterColor": (255, 255, 255, 255),
            "flipH": False,
        }
        self.idleR = createFixedSprite(params)
        params["flipH"] = True
        self.idleL = createFixedSprite(params)
        # move vars
        self.moveL = False
        self.moveR = False
        self.lastMoveL = False

    def update(self,deltaTime):
        # update animations for all
        self.runL.update_animation(deltaTime)
        self.runR.update_animation(deltaTime)
        # move sprites according to user key selection
        if self.moveL:
            self.idleL.center_x -= 10
        if self.moveR:
            self.idleL.center_x += 10
        if self.idleL.center_x < 75:
            self.idleL.center_x = 75
        if self.idleL.center_x > self.W-75:
            self.idleL.center_x = self.W - 75
        # all sprites are at the same position
        self.idleR.center_x = self.idleL.center_x
        self.runL.center_x  = self.idleL.center_x
        self.runR.center_x  = self.idleL.center_x
        self.idleR.center_y = self.idleL.center_y
        self.runL.center_y  = self.idleL.center_y
        self.runR.center_y  = self.idleL.center_y

    def draw(self):
        self.bg6.draw()
        self.bg5.draw()
        self.bg2.draw()

        if self.moveL == self.moveR:
            if self.lastMoveL:
                self.idleL.draw()
            else:
                self.idleR.draw()
        elif self.moveL:
            self.runL.draw()
        else:
            self.runR.draw()

        self.bg1.draw()

    def onKeyEvent(self, key, isPressed):
        if key== arcade.key.Q:
            self.moveL = isPressed
            self.lastMoveL = True
        if key == arcade.key.D:
            self.moveR = isPressed
            self.lastMoveL = False

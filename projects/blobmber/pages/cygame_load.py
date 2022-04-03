import math

import arcade

from projects.blobmber.classes.Word import Word
from utils.gfx_sfx import createFixedSprite, createAnimatedSprite

class CyGameLoad():


    def __init__(self, W, H, manager):
        super().__init__()
        self.W = W
        self.H = H
        self.manager = manager

        self.STEP = 6

    def __goToSplashPage(self):
        self.manager.selectPage(1)

    def setup(self):
        params = {
            "filePath": "projects/blobmber/images/RPH_studio.png",
            "position": (self.W/2, self.H/2),
            "size": (self.W*0.75, self.H*0.75),
            "filterColor": (255,255,255,200),
        }
        logoRPH = createFixedSprite(params)
        params = {
            "filePath": "projects/blobmber/images/arcade.png",
            "position": (self.W/2, self.H/2),
            "size": (self.W*0.75, self.H*0.75),
            "filterColor": (255,255,255,200),
        }
        logoArcade = createFixedSprite(params)
        params = {
            "filePath": "projects/blobmber/images/cytech.png",
            "position": (self.W/2, self.H/2),
            "size": (self.W*0.75, self.H*0.75),
            "filterColor": (255,255,255,200),
        }
        logoCYTech = createFixedSprite(params)

        self.logos = [
            {
                "logo": logoCYTech,
                "text": "a CY-Tech programming event",
                "duration": 5,
            },
            {
                "logo"     : logoArcade,
                "text"     : "powered by Arcade",
                "duration" : 5,
            },
            {
                "logo"     : logoRPH,
                "text"     : "presents...",
                "duration" : 5,
            },

        ]
        self.logoIndex = 0
        self.time = 0

    def update(self,deltaTime):
        if self.logoIndex < len(self.logos):
            self.time += deltaTime
            duration = self.logos[self.logoIndex]["duration"]
            if self.time >= duration:
                self.time -= duration
                self.logoIndex += 1
        else:
            # Go to next page
            self.__goToSplashPage()

    def draw(self):
        if self.logoIndex < len(self.logos):
            # Display current logo
            self.logos[self.logoIndex]["logo"].draw()
            # display text
            txt = self.logos[self.logoIndex]["text"]
            arcade.draw_text(txt, self.W*0.95, self.H/30, (255,255,255,200), anchor_x="right", font_size=24)
            # Compute alpha according to time and duration
            alpha = 0
            full = self.logos[self.logoIndex]["duration"]
            half = full/2
            if self.time <= half:
                    T = half - self.time
                    alpha = int(255*T/half)
            elif self.time <= full:
                T = full - self.time
                alpha = 255-int(255*T/half)
            # Draw black rectangle according to alpha
            arcade.draw_rectangle_filled(self.W/2, self.H/2, self.W, self.H, (0,0,0,alpha))

    def onKeyEvent(self, key, isPressed):
        if not isPressed:
            self.__goToSplashPage()

    def onButtonEvent(self, gamepadNum, buttonName, isPressed):
        if not isPressed:
            self.__goToSplashPage()


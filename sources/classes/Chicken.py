from sources.utils import  *
import math


class Chicken():

    def __init__(self, W, H):
        self.W = W
        self.H = H
        self.speed = randint(400,600)
        self.speed2 = 100
        self.dx    = 1
        self.k    = 0.965
        params = {
            "filePath": "images/characters/chicken.png",
            "spriteBox": (4, 4, 192, 192),
            "position" : (-200,75),
            "startIndex":0,
            "endIndex":7,
            "frameDuration":1/15,
            "color": (255,255,255,255),
        }
        self.chickenR = createAnimatedSprite(params)
        params["flipH"] = True
        self.chickenL = createAnimatedSprite(params)
        params = {
            "filePath": "images/characters/chicken.png",
            "spriteBox": (4, 4, 192, 192),
            "position" : (250,self.H + 500),
            "startIndex":8,
            "endIndex":11,
            "frameDuration":1/20,
            "color": (255,255,255,255),
        }
        self.chickenFR = createAnimatedSprite(params)
        params["flipH"] = True
        self.chickenFL = createAnimatedSprite(params)


    def toggleChickens(self):
        self.speed = randint(600,1000)
        self.chickenR.center_x = randint(-5000, -200)
        self.chickenL.center_x = self.W + randint(200, 5000)
        self.dx *= -1

    def update(self, deltaTime):
        # update anims
        self.chickenL.update_animation(deltaTime)
        self.chickenR.update_animation(deltaTime)
        # run back and forth
        if self.dx == 1:
            self.chickenR.center_x += self.speed * deltaTime
            if self.chickenR.center_x > self.W + 200:
                self.toggleChickens()
        else:
            self.chickenL.center_x -= self.speed * deltaTime
            if self.chickenL.center_x < -200:
                self.toggleChickens()
        # flying chicken
        self.chickenFL.update_animation(deltaTime)
        self.chickenFR.update_animation(deltaTime)
        self.chickenFL.center_y = (self.chickenFL.center_y)*self.k + (self.H/2)*(1-self.k)
        if self.k < 1:
            if self.chickenFL.center_y < self.H/2+10:
                self.k = 2 - self.k
        else:
            if self.chickenFL.center_y > self.H + 100:
                self.chickenFL.center_y = self.H * randint(4000, 40000)
                self.k = 2 - self.k
                self.chickenFL.center_x = randint(int(self.W*0.75),int(self.W*1.25))%self.W
        self.chickenFR.center_x = self.chickenFL.center_x
        self.chickenFR.center_y = self.chickenFL.center_y

    def draw(self):
        if self.dx == 1:
            self.chickenR.draw()
        else:
            self.chickenL.draw()
        if self.chickenFL.center_x < self.W/2:
            self.chickenFR.draw()
        else:
            self.chickenFL.draw()

    @property
    def center_x(self):
        return self.chicken.center_x

    @property
    def center_y(self):
        return self.chicken.center_y


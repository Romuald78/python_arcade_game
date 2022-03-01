from sources.utils import  *
import math


class Star():

    def __init__(self, W, H, spriteSelect):
        self.angStep = 90
        self.radius = randint(350,450)
        self.speed  = 0
        self.ang2   = self.angStep
        self.ang    = 0
        self.rotWay = 1
        self.W      = W
        self.H      = H
        self.moveToCenter = True
        params = {
            "position": (-1000,-1000),
            "filePath": "images/items/gems.png",
            "spriteBox": (6, 3, 100, 100),
            "spriteSelect": spriteSelect,

            "partSize": 128,
            "partScale": 0.9,
            "partSpeed": 1.0,
            "filterColor": (255,255,255,255),
            "startAlpha": 75,
            "endAlpha": 0,

            "partNB": 50,
            "maxLifeTime": 1.0,
        }
        self.starEmitter = createParticleEmitter(params)

    def update(self, deltaTime):
        # update star generation
        self.starEmitter.update()

        # if out of screen, select random input
        if self.center_x < -500 or self.center_x > self.W+500 or self.center_y < -500 or self.center_y > self.H+500:
            self.selectStart()

        # if too far...
        if self.moveToCenter and (abs(self.center_x - self.W/2) > self.radius or abs(self.center_y - self.H/2) > self.radius/2):
            # ... move to the center
            dx = math.cos((self.ang+180)*math.pi/180)
            dy = math.sin((self.ang+180)*math.pi/180)
            self.starEmitter.center_x += dx * self.speed * deltaTime
            self.starEmitter.center_y += dy * self.speed * deltaTime
        elif abs(self.ang-self.ang2) <= self.speed*deltaTime/5 :
            # ... move away from center
            self.moveToCenter = False
            self.ang = self.ang2
            dx = math.cos((self.ang+180)*math.pi/180)
            dy = math.sin((self.ang+180)*math.pi/180)
            self.starEmitter.center_x -= dx * self.speed * deltaTime
            self.starEmitter.center_y -= dy * self.speed * deltaTime
        else:
           # ... else rotate
            self.ang = (self.ang + (self.speed*deltaTime/5)*self.rotWay) # % 360
            # position the star emitter
            self.starEmitter.center_x  = self.W // 2
            self.starEmitter.center_y  = self.H // 2
            self.starEmitter.center_x += self.radius * math.cos(self.ang * math.pi / 180.0)
            self.starEmitter.center_y += self.radius * 0.5 * math.sin(self.ang * math.pi / 180.0)

    def draw(self):
        self.starEmitter.draw()

    def selectStart(self):
        # speed
        self.speed  = randint(500,600)
        # rotation
        self.rotWay = randint(0,1)*2 -1
        # input/output angles
        tmp = randint(0, 3) * self.angStep
        if self.ang%360 == tmp:
            tmp += self.angStep
        self.ang = tmp
        self.ang2  = self.ang + self.rotWay*(randint(1,7) * self.angStep)
        # set position according to input angle
        dx = math.cos(self.ang*math.pi/180)
        dy = math.sin(self.ang*math.pi/180)
        self.starEmitter.center_x  = self.W // 2
        self.starEmitter.center_y  = self.H // 2
        self.starEmitter.center_x += dx * self.W // 2
        self.starEmitter.center_y += dy * self.H // 2
        self.moveToCenter = True

    @property
    def center_x(self):
        return self.starEmitter.center_x

    @property
    def center_y(self):
        return self.starEmitter.center_y


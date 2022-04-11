from random import randint

import arcade
import pymunk

class PhysicWorld():

    def __init__(self, w, h):
        self.PADDING = 100
        self.W = w
        self.H = h
        self.space = pymunk.Space()

    def addCircle(self, initPos=(0,0), radius=1, mass=0.01, type="" ):
        b = pymunk.Body()
        b.position = initPos
        c = pymunk.Circle(b, radius)
        c.mass = mass
        c.friction = 0
        self.space.add(b, c)
        vx = randint(0,1)*2 - 1
        vy = randint(0,1)*2 - 1
        vx *= randint(50,100)
        vy *= randint(50,100)
        b.apply_force_at_local_point((vx,vy),(0,0))
        return c

    def update(self, deltaTime):
        self.space.step(deltaTime)
        for body in self.space.bodies:
            x, y = body.position
            if x < -self.PADDING:
                x = self.W+self.PADDING-1
            if y < -self.PADDING:
                y = self.H+self.PADDING-1
            if x >= self.W+self.PADDING:
                x = -self.PADDING
            if y >= self.H+self.PADDING:
                y = -self.PADDING
            body.position = (x,y)

    def draw(self):
        for shape in self.space.shapes:
            radius = shape.radius
            x,y  = shape.body.position
            arcade.draw_circle_outline(x, y, radius, (255,255,255,255))


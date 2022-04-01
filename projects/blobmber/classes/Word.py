import math
import random

import arcade

from utils.gfx_sfx import createAnimatedSprite


class Word():

    def __init__(self, charW, charH, word, spcW, spcH, color=(255,255,255,255)):
        self.x = 0
        self.y = 0
        self.sc = 1
        self.w = charW
        self.h = charH
        self.spcW = spcW
        self.spcH = spcH
        self.color = color
        self.setWord(word)

    @property
    def center_x(self):
        return self.x
    @property
    def center_y(self):
        return self.y
    @property
    def scale(self):
        return self.sc

    @center_x.setter
    def center_x(self, x0):
        for letter in self.letters:
            letter.targetx = x0
            x0 += self.spcW
    @center_y.setter
    def center_y(self, y0):
        for letter in self.letters:
            letter.targety = y0
    @scale.setter
    def scale(self, sc0):
        for letter in self.letters:
            letter.targetScale = sc0

    def setWord(self, word):
        self.letters = arcade.SpriteList()
        word = word.upper()
        N = len(word)
        a = 0
        for c in word:
            index = -1
            a += 2*math.pi/N
            x = 5000 * math.cos(a) + 800
            y = 5000 * math.sin(a) + 800
            params = {
                "filePath": "projects/blobmber/images/slimefont.png",
                "position": (x, y),
                "size": (self.w, self.h),
                "spriteBox": (6, 6, 122, 122),
                "frameDuration": 1,
                "flipH": False,
                "filterColor": self.color
            }
            if 'A' <= c <= 'Z':
                index = ord(c) - 65
            elif '0' <= c <= '9':
                index = ord(c) - 48 + 26
            elif c == ' ':
                index = 0
                params["spriteBox"] = (1, 1, 1, 1)
            else:
                continue
                print(c)

            params["startIndex"] = index
            params["endIndex"] = index

            letter = createAnimatedSprite(params)
            letter.angle += random.randint(-10,10)
            letter.targetAng = letter.angle
            letter.targetx = letter.center_x
            letter.targety = letter.center_y
            letter.targetScale = 1
            self.letters.append( letter )
            x += self.spcW

    def draw(self):
        self.letters.draw()

    def update(self, deltaTime):
        first = True
        for letter in self.letters:
            # target angle
            letter.angle = letter.angle * 0.99 + letter.targetAng * 0.01
            if abs(letter.targetAng - letter.angle) < 0.1:
                letter.targetAng = random.random()*30 - 15
            # target scale
            letter.scale = letter.scale * 0.97 + letter.targetScale * 0.03
            if abs(letter.targetScale - letter.scale) < 0.1:
                letter.targetScale = random.random()*0.5 + 0.9
            # target position
            letter.center_x = letter.center_x * 0.94 + letter.targetx * 0.06
            letter.center_y = letter.center_y * 0.94 + letter.targety * 0.06
            if first:
                first = False
                self.x  = letter.center_x
                self.y  = letter.center_y
                self.sc = letter.scale


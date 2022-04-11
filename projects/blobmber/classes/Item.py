from arcade import SpriteList

from projects.blobmber.classes.constants import Constants
from utils.gfx_sfx import createAnimatedSprite, createParticleEmitter


class Item():

    TYPE_FIRE     = 0
    TYPE_SPEED    = 1
    TYPE_BOMB     = 2
    TYPE_GAUNTLET = 3
    TYPE_KICK     = 4
    TYPE_DISEASE  = 5
    NB_TYPES      = 6

    def __init__(self, x, y, w, h, type):
        params = {
            "filePath": "projects/blobmber/images/runes.png",
            "position": (x, y + h*Constants.RUNE_OFFSET_KY),
            "size": (w, h),
            "spriteBox": (3, 2, 512, 512),
            "frameDuration": 1,
            "startIndex": type,
            "endIndex": type,
        }
        self.rune = createAnimatedSprite(params)
        params = {
            "position": (x, y+h*Constants.RUNE_OFFSET_KY),
            "filePath": "projects/blobmber/images/runes_front_light.png",
            "spriteBox": (3, 2, 512, 512),
            "spriteSelect": (type%3, type//3),
            "partSize": 512,
            "partScale": w/512,
            "partSpeed": 0.3,
            "filterColor": (255, 255, 255, 255),
            "startAlpha": 95,
            "endAlpha": 95,
            "partNB": 20,
            "maxLifeTime": 2.0,
        }
        self.frontLight = createParticleEmitter(params)
        params["filePath"]   = "projects/blobmber/images/runes_back_light.png"
        params["endAlpha"]   = 0
        params["partScale"] *= 1.40
        params["partNB"]     = 10
        self.backLight = createParticleEmitter(params)


    def update(self, deltaTime):
        self.frontLight.update()
        self.backLight.update()

    def draw(self):
        self.backLight.draw()
        self.rune.draw()
        self.frontLight.draw()

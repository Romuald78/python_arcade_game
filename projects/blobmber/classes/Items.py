from arcade import SpriteList

from projects.blobmber.classes.constants import Constants
from utils.gfx_sfx import createAnimatedSprite, createParticleEmitter, utilsUpdateAnimation
from utils.trigo import distance2


class Items():

    TYPE_FIRE     = 0
    TYPE_KICK     = 1
    TYPE_SPEED    = 2
    TYPE_GAUNTLET = 3
    TYPE_BOMB     = 4
    TYPE_DISEASE  = 5
    NB_TYPES      = 6

    def addItem(self, x, y, w, h, type):
        params = {
            "filePath": "projects/blobmber/images/runes.png",
            "position": (x, y + h*Constants.RUNE_OFFSET_KY),
            "size": (w, h),
            "spriteBox": (3, 2, 512, 512),
            "frameDuration": 1,
            "startIndex": type,
            "endIndex": type,
        }
        rune = createAnimatedSprite(params)
        params = {
            "position": (x, y+h*Constants.RUNE_OFFSET_KY),
            "filePath": "projects/blobmber/images/runes_front_light.png",
            "spriteBox": (3, 2, 512, 512),
            "spriteSelect": (type%3, type//3),
            "partSize": 512,
            "partScale": 1.05*w/512,
            "partSpeed": 0.3,
            "filterColor": (255, 255, 255, 255),
            "startAlpha": 100,
            "endAlpha": 0,
            "partNB": 15,
            "maxLifeTime": 1,
        }
        frontLight = createParticleEmitter(params)
        params["filePath"]   = "projects/blobmber/images/runes_back_light.png"
        params["startAlpha"]   = 75
        params["partScale"] *= 1.30
        params["partNB"]     = 15
        params["partSpeed"]  *= 1.5
        backLight = createParticleEmitter(params)
        # add particles in rune
        rune.frontLight = frontLight
        rune.backLight  = backLight
        rune.type       = type
        # Add rune to the sprite list
        self.runes.append(rune)

    def __init__(self, blobs):
        self.blobs = blobs
        self.runes = SpriteList()

    def update(self, deltaTime):
        # toBeRemoved list
        toBeRemoved = []
        # Check collisions with players
        for rune in self.runes:
            # list for all potential pickers
            pickers = []
            for blob in self.blobs:
                # collision test
                if blob.isOvalColliding( (rune.center_x, rune.center_y), rune.width/6, rune.height/6 ):
                    # add potential picker to the list
                    pickers.append(blob)
                    # remove this rune
                    toBeRemoved.append(rune)
            # Now compute the distances
            if len(pickers) > 0:
                minDist = 1000000000
                nearest = None
                for pck in pickers:
                    d = distance2(rune.center_x, rune.center_y, pck.center_x, pck.center_y)
                    if d < minDist:
                        nearest = pck
                        minDist = d
                # Now store rune inside player
                nearest.pickUpRune(rune)

        # Remove all picked up runes
        for tbr in toBeRemoved:
            self.runes.remove(tbr)

        # Update particle emitters
        for rune in self.runes:
            rune.frontLight.update()
            rune.backLight.update()

    def draw(self):
        # backlight
        for rune in self.runes:
            rune.backLight.draw()
        # stone runes
        self.runes.draw()
        # front light
        for rune in self.runes:
            rune.frontLight.draw()


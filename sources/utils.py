import math

import arcade
from random import *

from arcade import AnimationKeyframe

def rotate(pos, pivot, angle):
    COS = math.cos(angle*math.pi/180)
    SIN = math.sin(angle*math.pi/180)
    x0, y0 = pos
    xp, yp = pivot
    x0 -= xp
    y0 -= yp
    x1 = (x0 * COS) - (y0 * SIN)
    y1 = (x0 * SIN) + (y0 * COS)
    x1 += xp
    y1 += yp
    return x1, y1

def createSound(fileName):
    snd = arcade.load_sound(fileName)
    return snd

def drawText(params):
    # retrieve parameters
    x       = params["x"]
    y       = params["y"]
    message = params["message"]
    size    = 12                if "size"   not in params else params["size"  ]
    color   = (255,255,255,255) if "color"  not in params else params["color" ]
    alignH  = "center"          if "alignH" not in params else params["alignH"]    # left, center, right
    alignV  = "center"          if "alignV" not in params else params["alignV"]    # top, center, bottom
    angle   = 0                 if "angle"  not in params else params["angle" ]
    bold    = False             if "bold"   not in params else params["bold"  ]
    italic  = False             if "italic" not in params else params["italic"]
    # draw text according to configuration
    arcade.draw_text(text=message,start_x=x,start_y=y,color=color,font_size=size,anchor_x=alignH,anchor_y=alignV,rotation=angle,bold=bold,italic=italic)

def createFixedSprite(params):
    # retrieve parameters
    filePath    = params["filePath"  ]
    size        = None if "size" not in params else params["size"]
    filterColor = (255,255,255,255) if "filterColor" not in params else params["filterColor"]
    isMaxRatio  = False if "isMaxRatio" not in params else params["isMaxRatio"]
    position    = (0,0) if "position" not in params else params["position"]
    flipH       = False if "flipH" not in params else params["flipH"]
    flipV       = False if "flipV" not in params else params["flipV"]

    # load texture for sprite
    spr = arcade.AnimatedTimeSprite()
    spr.color = filterColor
    spr.append_texture(arcade.load_texture(filePath, flipped_horizontally=flipH, flipped_vertically=flipV))
    # set dimensions
    spr.update_animation()
    if size != None:
        if isMaxRatio:
            ratio = max(size[0] / spr.width, size[1] / spr.height)
        else:
            ratio = min(size[0]/spr.width, size[1]/spr.height)
        spr.scale = ratio
    # set position (init)
    spr.center_x = position[0]
    spr.center_y = position[1]
    return spr


def createAnimatedSprite(params):
    # retrieve parameters
    filePath      = params["filePath"  ]
    size          = None if "size" not in params else params["size"]
    filterColor   = (255, 255, 255, 255) if "filterColor" not in params else params["filterColor"]
    isMaxRatio    = False  if "isMaxRatio"    not in params else params["isMaxRatio"]
    position      = (0, 0) if "position"      not in params else params["position"]
    spriteBox     = params["spriteBox" ]
    startIndex    = params["startIndex"]
    endIndex      = params["endIndex"  ]
    frameduration = 1/60   if "frameDuration" not in params else params["frameDuration"]
    flipH         = False  if "flipH"         not in params else params["flipH"]
    flipV         = False  if "flipv"         not in params else params["flipV"]

    # get sprite box (nb sprites X, nb Y, size X size Y)
    nbX, nbY, szW, szH = spriteBox
    # Instanciate sprite object
    spr = arcade.AnimatedTimeSprite()
    spr.color = filterColor
    # Read Horizontal first, then vertical
    for y in range(nbY):
        for x in range(nbX):
            index = x + y*nbX
            # add index only if in range
            if index >= startIndex and index <= endIndex:
                tex = arcade.load_texture(filePath, x * szW, y * szH, szW, szH, flipped_horizontally=flipH, flipped_vertically=flipV)
                spr.textures.append(tex)
    # set dimensions
    spr.update_animation()
    spr.center_x = position[0]
    spr.center_y = position[1]
    if size != None:
        if isMaxRatio:
            ratio = max(size[0]/spr.width, size[1]/spr.height)
        else:
            ratio = min(size[0]/spr.width, size[1]/spr.height)
        spr.scale = ratio

    # set frame duration
    spr.texture_change_frames = int(frameduration*60 + 0.5)

    # return sprite object
    return spr


def createParticleBurst(params):
    # retrieve Sprite parameters
    filePath = None if "filePath" not in params else params["filePath"]
    spriteBox = None if "spriteBox" not in params else params["spriteBox"]
    spriteSelect = None if "spriteSelect" not in params else params["spriteSelect"]
    flipH = False if "flipH" not in params else params["flipH"]
    flipV = False if "flipv" not in params else params["flipV"]

    # Retrieve common emitter parameters
    position      = params["position"     ]
    partSize      = params["partSize"     ]
    partScale     = params["partScale"    ]
    partSpeed     = params["partSpeed"    ]
    color         = params["filterColor"  ]
    startAlpha    = params["startAlpha"   ]
    endAlpha      = params["endAlpha"     ]

    # Retrieve specific burst parameters
    partInterval  = params["partInterval" ]
    totalDuration = params["totalDuration"]

    # Prepare Texture
    if filePath == None:
        tex = arcade.make_circle_texture(partSize, color)
    else:
        nbX, nbY, szW, szH = spriteBox
        x, y = spriteSelect
        tex = arcade.load_texture(filePath, x * szW, y * szH, szW, szH,
                                  flipped_horizontally=flipH,
                                  flipped_vertically=flipV)

    # create Burst
    e = arcade.Emitter(
        center_xy=position,
        emit_controller=arcade.EmitterIntervalWithTime(partInterval, totalDuration),
        particle_factory=lambda emitter: arcade.FadeParticle(
            filename_or_texture=tex,
            change_xy=arcade.rand_in_circle((0.0, 0.0), partSpeed),
            scale=partScale,
            lifetime=uniform(totalDuration/4, totalDuration),
            start_alpha=startAlpha,
            end_alpha=endAlpha,
        ),
    )
    # return result
    return e



def createParticleEmitter(params):
    # retrieve Sprite parameters
    filePath = None if "filePath" not in params else params["filePath"]
    spriteBox = None if "spriteBox" not in params else params["spriteBox"]
    spriteSelect = None if "spriteSelect" not in params else params["spriteSelect"]
    flipH = False if "flipH" not in params else params["flipH"]
    flipV = False if "flipv" not in params else params["flipV"]

    # Retrieve common emitter parameters
    position      = params["position"     ]
    partSize      = params["partSize"     ]
    partScale     = params["partScale"    ]
    partSpeed     = params["partSpeed"    ]
    color         = params["filterColor"  ]
    startAlpha    = params["startAlpha"   ]
    endAlpha      = params["endAlpha"     ]

    # Retrieve specific emitter parameters
    partNB        = params["partNB"      ]
    maxLifeTime   = params["maxLifeTime" ]

    # Prepare Texture
    if filePath == None:
        tex = arcade.make_circle_texture(partSize, color)
    else:
        nbX, nbY, szW, szH = spriteBox
        x, y = spriteSelect
        tex = arcade.load_texture(filePath, x * szW, y * szH, szW, szH,
                                  flipped_horizontally=flipH,
                                  flipped_vertically=flipV)

    # Create emitter
    e = arcade.Emitter(
        center_xy        = position,
        emit_controller  = arcade.EmitMaintainCount(partNB),
        particle_factory = lambda emitter: arcade.FadeParticle(
            filename_or_texture = tex,
            change_xy           = arcade.rand_in_circle( (0.0,0.0), partSpeed),
            lifetime            = uniform(maxLifeTime/10,maxLifeTime),
            scale = partScale,
            start_alpha=startAlpha,
            end_alpha=endAlpha,
        ),
    )
    return e



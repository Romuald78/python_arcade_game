### ====================================================================================================
### IMPORTS
### ====================================================================================================
import arcade

from utils.gfx_sfx import createFixedSprite, createAnimatedSprite
import math

class Process:

    ### ====================================================================================================
    ### PARAMETERS
    ### ====================================================================================================
    SCREEN_WIDTH  = 1280 #int(1920*0.90) #int(1280*0.75)
    SCREEN_HEIGHT = 1024 #int(1080*0.90) #int(1024*0.75)


    ### ====================================================================================================
    ### CONSTRUCTOR
    ### ====================================================================================================
    def __init__(self):
        pass


    ### ====================================================================================================
    ### INIT
    ### ====================================================================================================
    def setup(self):
        params = {
            "filePath" : "projects/demo/images/characters/girl_fix.png",
            "position" : (self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT/2),
            "flipH" : False
        }
        self.girlIdleR = createFixedSprite(params)
        params["flipH"] = True
        self.girlIdleL = createFixedSprite(params)
        params = {
            "filePath" : "projects/demo/images/characters/girl.png",
            "position" : (self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT/2),
            "spriteBox": (7,1,170,250),
            "startIndex":1,
            "endIndex":6,
            "frameDuration":1/15,
            "flipH": False
        }
        self.girlRunR = createAnimatedSprite(params)
        params["flipH"] = True
        self.girlRunL = createAnimatedSprite(params)


        # GESTION du TEMPS
        self.timer = 0
        # movement directions
        self.moveL = False
        self.moveR = False
        self.lastDirectionLeft = False


    ### ====================================================================================================
    ### UPDATE
    ### ====================================================================================================
    def update(self,deltaTime):
        self.girlRunL.update_animation(deltaTime)
        self.girlRunR.update_animation(deltaTime)
        self.timer += deltaTime
        if self.moveL:
            self.girlIdleR.center_x -= 15
        if self.moveR:
            self.girlIdleR.center_x += 15
        self.girlIdleL.center_x = self.girlIdleR.center_x
        self.girlRunL.center_x  = self.girlIdleR.center_x
        self.girlRunR.center_x  = self.girlIdleR.center_x

    ### ====================================================================================================
    ### RENDERING
    ### ====================================================================================================
    def draw(self):
        if self.moveL == self.moveR:
            if self.lastDirectionLeft:
                self.girlIdleL.draw()
            else:
                self.girlIdleR.draw()
        elif self.moveL:
            self.girlRunL.draw()
        else:
            self.girlRunR.draw()

    ### ====================================================================================================
    ### KEYBOARD EVENTS
    ### key is taken from : arcade.key.xxx
    ### ====================================================================================================
    def onKeyEvent(self,key,isPressed):
        #print(f"KEYBOARD : key={key} / isPressed={isPressed}");
        if key == arcade.key.LEFT:
            self.moveL = isPressed
            self.lastDirectionLeft = True
        if key == arcade.key.RIGHT:
            self.moveR = isPressed
            self.lastDirectionLeft = False


    ### ====================================================================================================
    ### GAMEPAD BUTTON EVENTS
    ### buttonName can be "A", "B", "X", "Y", "LB", "RB", "VIEW", "MENU", "LSTICK", "RSTICK"
    ### ====================================================================================================
    def onButtonEvent(self, gamepadNum,buttonName,isPressed):
        print(f"GAMEPAD BUTTON : gamepad={gamepadNum} / button={buttonName} / isPressed={isPressed}");


    ### ====================================================================================================
    ### GAMEPAD AXIS EVENTS
    ### axisName can be "X", "Y", "RX", "RY", "Z"
    ### ====================================================================================================
    def onAxisEvent(self, gamepadNum,axisName,analogValue):
        print(f"GAMEPAD AXIS : gamepad={gamepadNum} / axis={axisName} / value={analogValue}");


    ### ====================================================================================================
    ### MOUSE MOTION EVENTS
    ### ====================================================================================================
    def onMouseMotionEvent(self,x,y,dx,dy):
        print(f"MOUSE MOTION : x={x} / y={y} / dx={dx} / dy={dy}")


    ### ====================================================================================================
    ### MOUSE BUTTON EVENTS
    ### ====================================================================================================
    def onMouseButtonEvent(self,x,y,buttonNum,isPressed):
        print(f"MOUSE BUTTON : x={x} / y={y} / button={buttonNum} / isPressed={isPressed}")



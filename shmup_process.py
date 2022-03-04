### ====================================================================================================
### IMPORTS
### ====================================================================================================
import arcade

from projects.shmup.cygame_splash import CyGameSplash


class Process:

    ### ====================================================================================================
    ### PARAMETERS
    ### ====================================================================================================
    SCREEN_WIDTH  = int(1920*0.75)
    SCREEN_HEIGHT = int(1080*0.75)


    def selectPage(self, pageIndex):
        self.pageIndex = pageIndex
        self.currentPage = self.pages[self.pageIndex]


    ### ====================================================================================================
    ### CONSTRUCTOR
    ### ====================================================================================================
    def __init__(self):
        pass


    ### ====================================================================================================
    ### INIT
    ### ====================================================================================================
    def setup(self):
        self.pages = []
        self.pages.append(CyGameSplash(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self))
        # Set first page
        self.pageIndex = 0
        self.currentPage = self.pages[self.pageIndex]
        # Setup all the pages only once
        for p in self.pages:
            p.setup()


    ### ====================================================================================================
    ### UPDATE
    ### ====================================================================================================
    def update(self,deltaTime):
        self.currentPage.update(deltaTime)


    ### ====================================================================================================
    ### RENDERING
    ### ====================================================================================================
    def draw(self):
        self.currentPage.draw()


    ### ====================================================================================================
    ### KEYBOARD EVENTS
    ### key is taken from : arcade.key.xxx
    ### ====================================================================================================
    def onKeyEvent(self,key,isPressed):
        # transfer event to page if needed
        check = callable(getattr(self.currentPage, 'onKeyEvent', None))
        if check:
            self.currentPage.onKeyEvent(key, isPressed)


    ### ====================================================================================================
    ### GAMEPAD BUTTON EVENTS
    ### buttonName can be "A", "B", "X", "Y", "LB", "RB", "VIEW", "MENU", "LSTICK", "RSTICK"
    ### ====================================================================================================
    def onButtonEvent(self, gamepadNum,buttonName,isPressed):
        #print(f"GamePad={gamepadNum} - ButtonNum={buttonName} - isPressed={isPressed}")
        # transfer event to page if needed
        check = callable(getattr(self.currentPage, 'onButtonEvent', None))
        if check:
            self.currentPage.onButtonEvent(gamepadNum, buttonName, isPressed)


    ### ====================================================================================================
    ### GAMEPAD AXIS EVENTS
    ### axisName can be "X", "Y", "RX", "RY", "Z"
    ### ====================================================================================================
    def onAxisEvent(self, gamepadNum,axisName,analogValue):
        #print(f"GamePad={gamepadNum} - AxisName={axisName} - Value={analogValue}")
        # transfer event to page if needed
        check = callable(getattr(self.currentPage, 'onAxisEvent', None))
        if check:
            self.currentPage.onAxisEvent(gamepadNum, axisName, analogValue)

    ### ====================================================================================================
    ### MOUSE MOTION EVENTS
    ### ====================================================================================================
    def onMouseMotionEvent(self,x,y,dx,dy):
        print(f"MOUSE MOTION : x={x}/y={y} dx={dx}/dy={dy}")


    ### ====================================================================================================
    ### MOUSE BUTTON EVENTS
    ### ====================================================================================================
    def onMouseButtonEvent(self,x,y,buttonNum,isPressed):
        print(f"MOUSE BUTTON : x={x}/y={y} buttonNum={buttonNum} isPressed={isPressed}")


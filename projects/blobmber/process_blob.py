### ====================================================================================================
### IMPORTS
### ====================================================================================================
import arcade.key

from projects.blobmber.classes.constants import Constants
from projects.blobmber.pages.cygame_load import CyGameLoad
from projects.blobmber.pages.cygame_splash import CyGameSplash
from projects.blobmber.pages.cygame_ingame import CyGameInGame


class Process:

    ### ====================================================================================================
    ### PARAMETERS
    ### ====================================================================================================

    SCREEN_HEIGHT = 1000                             #int(1024*0.75) # int(1080*0.75)
    SCREEN_WIDTH  = int(SCREEN_HEIGHT * 1280 / 1024) #int(1280*0.75) # int(1920*0.75)
    CELL_SIZE = min(SCREEN_WIDTH/Constants.NB_CELLS_X, SCREEN_HEIGHT/Constants.NB_CELLS_Y)
    NB_CELL_X = int(SCREEN_WIDTH/CELL_SIZE)+1
    NB_CELL_Y = int(SCREEN_HEIGHT/CELL_SIZE)+1

    def selectPage(self, pageIndex, params=None):
        self.pageIndex = pageIndex
        self.currentPage = self.pages[self.pageIndex]
        if params is not None:
            self.currentPage.setup(params)



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
        self.pages.append(CyGameLoad(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self))
        self.pages.append(CyGameSplash(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self))
        self.pages.append(CyGameInGame(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.CELL_SIZE, self.NB_CELL_X, self.NB_CELL_Y, self))
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


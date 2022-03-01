### ====================================================================================================
### IMPORTS
### ====================================================================================================
import arcade

from sources.cygame.cygame_splash import CyGameSplash
from sources.pages.page_1_home      import Page1Home
from sources.pages.page_2_sprite    import Page2Sprite
from sources.pages.page_3_anim      import Page3Anim
from sources.pages.page_4_multisprite import Page4Multi
from sources.pages.page_5_rotation  import Page5Rotation
from sources.pages.page_6_move      import Page6Move
from sources.pages.page_7_emitter   import Page7Emitter
from sources.pages.page_20_parallax import Page20Parallax
from sources.pages.page_8_burst import Page8Burst


class Process:

    ### ====================================================================================================
    ### PARAMETERS
    ### ====================================================================================================
    SCREEN_WIDTH  = int(1920*0.75)
    SCREEN_HEIGHT = int(1080*0.75)


    ### ====================================================================================================
    ### CONSTRUCTOR
    ### ====================================================================================================
    def __init__(self):
        pass


    ### ====================================================================================================
    ### INIT
    ### ====================================================================================================
    def setup(self):
        # Add all pages
        self.pages = []
        # DEBUG CYGAME
        self.pages.append(CyGameSplash(self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.pages.append(Page1Home     (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.pages.append(Page2Sprite   (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.pages.append(Page3Anim     (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.pages.append(Page4Multi    (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.pages.append(Page5Rotation (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.pages.append(Page6Move     (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.pages.append(Page7Emitter  (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.pages.append(Page8Burst    (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.pages.append(Page20Parallax(self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

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
        #print(f"key={key} - isPressed={isPressed}")
        if len(self.pages) > 1:
            # Switch to previous or next page
            if key == arcade.key.LEFT and isPressed:
                self.pageIndex = (self.pageIndex-1+len(self.pages))%len(self.pages)
                self.currentPage = self.pages[self.pageIndex]
            elif key == arcade.key.RIGHT and isPressed:
                self.pageIndex = (self.pageIndex+1)%len(self.pages)
                self.currentPage = self.pages[self.pageIndex]
        # transfer event to page if needed
        check = callable(getattr(self.currentPage, 'onKeyEvent', None))
        if check:
            self.currentPage.onKeyEvent(key, isPressed)


    ### ====================================================================================================
    ### GAMEPAD BUTTON EVENTS
    ### buttonName can be "A", "B", "X", "Y", "LB", "RB", "VIEW", "MENU", "LSTICK", "RSTICK"
    ### ====================================================================================================
    def onButtonEvent(self, gamepadNum,buttonName,isPressed):
        print(f"GamePad={gamepadNum} - ButtonNum={buttonName} - isPressed={isPressed}")
        

    ### ====================================================================================================
    ### GAMEPAD AXIS EVENTS
    ### axisName can be "X", "Y", "RX", "RY", "Z"
    ### ====================================================================================================
    def onAxisEvent(self, gamepadNum,axisName,analogValue):
        print(f"GamePad={gamepadNum} - AxisName={axisName} - Value={analogValue}")
        

    ### ====================================================================================================
    ### MOUSE MOTION EVENTS
    ### ====================================================================================================
    def onMouseMotionEvent(self,x,y,dx,dy):
        #print(f"MOUSE MOTION : x={x}/y={y} dx={dx}/dy={dy}")
        # transfer event to page if needed
        check = callable(getattr(self.currentPage, 'onMouseMotionEvent', None))
        if check:
            self.currentPage.onMouseMotionEvent(x, y, dx, dy)


    ### ====================================================================================================
    ### MOUSE BUTTON EVENTS
    ### ====================================================================================================
    def onMouseButtonEvent(self,x,y,buttonNum,isPressed):
        #print(f"MOUSE BUTTON : x={x}/y={y} buttonNum={buttonNum} isPressed={isPressed}")
        # transfer event to page if needed
        check = callable(getattr(self.currentPage, 'onMouseButtonEvent', None))
        if check:
            self.currentPage.onMouseButtonEvent(x, y, buttonNum, isPressed)

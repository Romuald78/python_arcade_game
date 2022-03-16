import math

from utils.gfx_sfx import createFixedSprite
from utils.trigo import rotate


class CyGameSplash():

    STATE_2IDLE   = 0
    STATE_IDLE    = 1
    STATE_2SELECT = 2
    STATE_SELECT  = 3
    STATE_ALIGN   = 4
    STATE_FLY     = 5
    STATE_GAME    = 6

    def __isShipSelected(self, shipID):
        for player in self.players:
            if player["ctrlID"] != -1 and player["shipID"] == shipID:
                return True
        return False

    def __moveBackground(self):
        period = 101
        xc = self.W/2
        yc = self.H/2
        rx = self.W*0.15
        ry = self.H*0.15
        x0 = rx*math.cos(2*self.time*math.pi/period)+xc
        y0 = ry*math.sin(2*self.time*math.pi/period)+yc
        x1, y1 = rotate((x0,y0), (xc,yc), 60)
        self.back.center_x = x1
        self.back.center_y = y1

    def __movePlanet(self):
        period = 53
        xc = self.W*0.9
        yc = self.H*0.9
        rx = self.W*0.03
        ry = self.H*0.03
        x0 = -rx*math.cos(2*self.time*math.pi/period)+xc
        y0 =  ry*math.sin(2*self.time*math.pi/period)+yc
        x1, y1 = rotate((x0,y0), (xc,yc), -30)
        self.planet.center_x = x1
        self.planet.center_y = y1

    def __moveMoon(self):
        period = 43
        xc = self.planet.center_x * 1.5
        yc = self.planet.center_y * 0.85
        rx = self.W*1.4
        ry = self.H*0.55
        x0 = -rx*math.cos(2*self.time*math.pi/period)+xc
        y0 =  ry*math.sin(2*self.time*math.pi/period)+yc
        x1, y1 = rotate((x0,y0), (xc,yc), 17)
        self.moon.center_x = x1
        self.moon.center_y = y1
        v = int(510*((self.time+period/4)%period)/period)
        if v <= 255:
            v = 255-v
        else:
            v -= 255
        self.moon.color = (v,v,v,255)

    def __moveTitle(self):
        period = 31
        xc = self.W / 2
        yc = self.H / 2
        rx = self.W * 0.02
        ry = self.W * 0.03
        x0 = rx * math.cos(2 * self.time * math.pi / period) + xc
        y0 = ry * math.sin(2 * self.time * math.pi / period) + yc
        x1, y1 = rotate((x0, y0), (xc, yc), 17)
        if self.state == self.STATE_IDLE:
            self.title.center_x = x1
            self.title.center_y = y1
        elif self.state == self.STATE_2IDLE:
            # Move the title down
            self.title.center_x = (self.title.center_x * 0.90 + 0.10 * x1)
            self.title.center_y = (self.title.center_y*0.90 + 0.10*y1)
            if abs(self.title.center_y - y1) < 5:
                self.state = self.STATE_IDLE
                for ship in self.ships:
                    ship.center_x = self.W/4
                    ship.center_y = -self.H/4
        elif self.state == self.STATE_2SELECT:
            # Move the title up
            self.title.center_x = (self.title.center_x * 0.90 + 0.10 * self.W / 2)
            y1 = self.H * 0.90
            self.title.center_y = (self.title.center_y * 0.90 + 0.10 * y1)
            if abs(self.title.center_y - y1) < 5:
                self.state = self.STATE_SELECT


    def __movePressStart(self):
        period = 23
        xc = self.title.center_x
        yc = self.title.center_y * 0.675
        rx = self.W*0.02
        ry = self.W*0.01
        x0 = xc
        y0 = ry*math.sin(2*self.time*math.pi/period)+yc
        self.pressStart.center_x = x0
        self.pressStart.center_y = y0

    def __moveGUI(self):
        # check if all ships are aligned
        if self.state == self.STATE_ALIGN:
            ok = True
            for ship in self.ships:
                if ship.angle != 0:
                    ok = False
                    break
            if ok:
                self.state = self.STATE_FLY
        # check if all ships are sent to game
        if self.state == self.STATE_FLY:
            ok = True
            for i in range(len(self.ships)):
                if self.ships[i].center_x < self.W*1.5 and self.players[i]["ctrlID"] != -1:
                    ok = False
                    break
            if ok:
                self.state = self.STATE_GAME

        # if ready to go to game
        if self.state == self.STATE_GAME:
            print("LAUNCH IN-GAME")
            # prepare player config
            playerConfig = []
            for p in self.players:
                if p["ctrlID"] != -1:
                    playerConfig.append(p)
            self.manager.selectPage(1, playerConfig)

        # Move ships and Set frame pos to ship pos
        for i in range(len(self.frames)):
            # Move ship
            x0 = self.W * 0.22
            y0 = self.title.center_y - (self.H * 0.22)
            dx = self.W * 0.13
            dy = -self.H * 0.26
            xc = x0 + i * dx
            yc = y0 + i * dy
            period = 23
            rx = self.W * 0.01
            ry = self.H * 0.01
            x0 = rx * math.cos(2 * self.time * math.pi / period) + xc
            y0 = ry * math.sin(2 * self.time * math.pi / period) + yc
            x1, y1 = rotate((x0, y0), (xc, yc), 59 * (i + 1))
            if self.state == self.STATE_2SELECT or (self.state == self.STATE_SELECT and (abs(self.ships[i].center_x - x1)>= 1 or abs(self.ships[i].center_y - y1)>= 1)):
                # Move the ships up
                self.ships[i].center_x = self.ships[i].center_x * (0.86+0.02*(i+1)) + (0.14-0.02*(i+1)) * x1
                self.ships[i].center_y = self.ships[i].center_y * (0.86+0.02*(i+1)) + (0.14-0.02*(i+1)) * y1
                self.ships[i].angle = 0
            elif self.state == self.STATE_2IDLE or (self.state >= self.STATE_ALIGN and self.players[i]["ctrlID"] == -1):
                # Move the ships down
                x1 = self.W/4
                y1 = -self.H/4
                self.ships[i].center_x = self.ships[i].center_x * (0.86+0.02*(i+1)) + (0.14-0.02*(i+1)) * x1
                self.ships[i].center_y = self.ships[i].center_y * (0.86+0.02*(i+1)) + (0.14-0.02*(i+1)) * y1
                self.ships[i].angle = 0
            elif self.state == self.STATE_SELECT:
                self.ships[i].center_x = x1
                self.ships[i].center_y = y1
            elif self.state == self.STATE_FLY and self.players[i]["ctrlID"] != -1:
                # Move the ships RIGHT
                self.ships[i].center_x = self.ships[i].center_x * 0.99 + 0.01 * self.W*2

            # Set filter color
            if self.__isShipSelected(i+1):
                self.frames[i].color = self.players[i]["color"]
                self.ships[i].color  = (255,255,255,192)
            else:
                self.frames[i].color = (128,128,128,128)
                self.ships[i].color  = (128,128,144,128)

            # Rotate ship according to lastX
            if self.state <= self.STATE_SELECT:
                if self.players[i]["ctrlID"] != -1:
                    self.ships[i].angle -= 5 * self.players[i]["lastX"]
            elif self.STATE_ALIGN:
                ang = abs(self.ships[i].angle % 360)
                if ang <= 6 or ang >= 354:
                    self.ships[i].angle = 0
                elif ang >=180 :
                    self.ships[i].angle += 5
                else:
                    self.ships[i].angle -= 5

            # move frame
            if self.state <= self.STATE_ALIGN:
                self.frames[i].center_x = self.ships[i].center_x
                self.frames[i].center_y = self.ships[i].center_y




    def __init__(self, W, H, manager):
        super().__init__()
        self.W = W
        self.H = H
        self.manager = manager

    def setup(self):
        # Title
        params = {
            "filePath": "projects/shmup/images/writings/cy-ber-tech.png",
            "position": (self.W // 2, self.H * 1.3),
            "size": (self.W*0.75, self.H*0.75),
            "filterColor": (255, 255, 200, 160),
        }
        self.title = createFixedSprite(params)
        # Background
        params = {
            "filePath": "projects/shmup/images/planets/space.png",
            "position": (self.W // 2, self.H // 2),
            "size": (self.W*1.30, self.H*1.30),
            "filterColor": (200, 200, 255, 200),
        }
        self.back = createFixedSprite(params)
        # Planet
        params = {
            "filePath": "projects/shmup/images/planets/planet.png",
            "position": (self.W, self.H),
            "size"    : (self.W/1.5, self.W/1.5),
            "filterColor": (200, 200, 255, 255),
        }
        self.planet = createFixedSprite(params)
        # Moon
        params = {
            "filePath": "projects/shmup/images/planets/satellite.png",
            "position": (3*self.W//4, 2*self.H//3),
            "filterColor": (200, 200, 255, 255),
        }
        self.moon = createFixedSprite(params)
        params = {
            "filePath": "projects/shmup/images/writings/press_start.png",
            "position": (self.W // 2, self.H // 2),
            "size": (self.W*0.5, self.H*0.5),
            "filterColor": (200, 200, 200, 200),
        }
        self.pressStart = createFixedSprite(params)
        # SHIPS
        self.ships   = []
        self.frames  = []
        self.players = []
        colors = [(0,255,0,192),
                  (255,255,0,192),
                  (0, 0, 255, 192)]
        for i in range(1,4):
            params = {
                "filePath": f"projects/shmup/images/ships/ship0{i}.png",
                "position": (self.H/4, -self.H/4),
                "size": (self.W * 0.15, self.H * 0.15),
                "filterColor": (255, 255, 255, 255),
            }
            self.ships.append( createFixedSprite(params) )
            params = {
                "filePath": "projects/shmup/images/gui/frame.png",
                "position": (self.H/4,-self.H/4),
                "size": (self.H/2.7, self.W/2.7),
                "filterColor":colors[i-1]
            }
            self.frames.append( createFixedSprite(params) )
            self.players.append( {"shipID" : i,
                                  "ctrlID" : -1,
                                  "color"  : colors[i-1],
                                  "lastX"  : 0,
                                  "lastY"  : 0 } )

        # game time and state
        self.time = 0
        self.state = self.STATE_2IDLE


    def update(self,deltaTime):
        self.time += deltaTime
        # Move GUI elements
        self.__moveBackground()
        self.__moveMoon()
        self.__movePlanet()
        self.__moveTitle()
        self.__movePressStart()
        self.__moveGUI()

    def draw(self):
        self.back.draw()
        self.moon.draw()
        self.planet.draw()
        self.title.draw()
        if self.time%2 > 1.0 and self.state == self.STATE_IDLE:
            self.pressStart.draw()
        if self.state != self.STATE_FLY:
            for frame in self.frames:
                frame.draw()
        for ship in self.ships:
            ship.draw()

    def onKeyEvent(self, key, isPressed):
        pass

    def registerCtrl(self, ctrlID):
        for i in range(len(self.players)):
            if self.players[i]["ctrlID"] == ctrlID:
                # already registered
                return False
        # not registered : find an available slot
        for i in range(len(self.players)):
            if self.players[i]["ctrlID"] == -1:
                self.players[i]["ctrlID"] = ctrlID
                self.players[i]["lastX"] = 0
                self.players[i]["lastY"] = 0
                self.ships[i].angle = 0
                return True

    def unregisterCtrlID(self, ctrlID):
        for i in range(len(self.players)):
            if self.players[i]["ctrlID"] == ctrlID:
                self.players[i]["ctrlID"] = -1
                return True
        return False

    def isRegistered(self,ctrlID):
        for i in range(len(self.players)):
            if self.players[i]["ctrlID"] == ctrlID:
                return True
        return False

    def nbPlayerRegistered(self):
        count = 0
        for player in self.players:
            if player["ctrlID"] != -1:
                count += 1
        return count

    def onButtonEvent(self, gamepadNum, buttonName, isPressed):
        if not isPressed:
            # --------------------------------------
            # if we are opening the game
            # --------------------------------------
            if self.state == self.STATE_IDLE:
                if self.registerCtrl(gamepadNum):
                    self.state = self.STATE_2SELECT
            # --------------------------------------
            # if we are in the select part
            # --------------------------------------
            elif self.state == self.STATE_SELECT:
                if buttonName=="MENU":
                    if self.isRegistered(gamepadNum):
                        self.state = self.STATE_ALIGN
                    if self.registerCtrl(gamepadNum):
                        return
                elif buttonName=="B":
                    if self.unregisterCtrlID(gamepadNum):
                        if self.nbPlayerRegistered() == 0:
                            self.state = self.STATE_2IDLE
                    else :
                        self.registerCtrl(gamepadNum)
                else:
                    self.registerCtrl(gamepadNum)


    def onAxisEvent(self, gamepadNum, axisName, analogValue):
        if self.state <= self.STATE_SELECT:
            for i in range(len(self.players)):
                # found the registered player
                if self.players[i]["ctrlID"] == gamepadNum:
                    if axisName == "X":
                        self.players[i]["lastX"] = analogValue
                        if abs(self.players[i]["lastX"]) <= 0.1:
                            self.players[i]["lastX"] = 0
                    if axisName == "Y":
                        prevY = self.players[i]["lastY"]
                        self.players[i]["lastY"] = analogValue
                        if abs(self.players[i]["lastY"]) <= 0.1:
                            self.players[i]["lastY"] = 0
                        # step DOWN
                        if analogValue <= -0.5 < prevY:
                            j = i+1
                            while j <= 2:
                                if self.players[j]["ctrlID"] == -1:
                                    # swap
                                    self.players[j]["ctrlID"] = self.players[i]["ctrlID"]
                                    self.players[j]["lastY"]  = self.players[i]["lastY"]
                                    self.players[i]["ctrlID"] = -1
                                    return
                                j += 1
                            break
                        # step UP
                        if prevY < 0.5 <= analogValue:
                            j = i-1
                            while j >=0 :
                                if self.players[j]["ctrlID"] == -1:
                                    # swap
                                    self.players[j]["ctrlID"] = self.players[i]["ctrlID"]
                                    self.players[j]["lastY"]  = self.players[i]["lastY"]
                                    self.players[i]["ctrlID"] = -1
                                    return
                                j -= 1
                            break

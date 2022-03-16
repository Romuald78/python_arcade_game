from utils.gfx_sfx import createFixedSprite


class Ship():

    def __init__(self, index, position=(0,0)):
        # index of the ship owner
        self.index      = str(index)
        # init positions
        self.x = position[0]
        self.y = position[1]
        self.mX = 0
        self.mY = 0
        # Load all needed sprites
        params = {
            "filePath": f"projects/shmup/images/ships/ship0{self.index}.png",
            "position": (self.x, self.y),
            # ----------------------------------------
            "size": (96, 96),
            "isMaxRatio": False,
            "filterColor": (255, 255, 255, 255),
            "flipH": False,
            "flipV": False,
        }
        self.ships = {}
        self.ships[str(index)] = createFixedSprite(params)
        for i in range(1,3):
            for j in range(i+1,4):
                params["size"] = (160, 160)
                params["filePath"] = f"projects/shmup/images/ships/ship{i}{j}.png"
                self.ships[f"{i}{j}"] = createFixedSprite(params)
        params["size"] = (192, 192)
        params["filePath"] = f"projects/shmup/images/ships/ship123.png"
        self.ships["123"] = createFixedSprite(params)

    @property
    def center_x(self):
        return self.x
    @property
    def center_y(self):
        return self.y

    @center_x.setter
    def center_x(self, x):
        self.x = x
    @center_y.setter
    def center_y(self, y):
        self.y = y

    def moveX(self, mx):
        self.mX = mx
    def moveY(self, my):
        self.mY = my




    def update(self, deltaTime):
        # Move ship
        self.x += self.mX * deltaTime
        self.y += self.mY * deltaTime

    def draw(self):
        self.ships[self.index].center_x = self.x
        self.ships[self.index].center_y = self.y
        self.ships[self.index].draw()

    def mergeWith(self, index):
        index = str(index)
        if index in self.index:
            raise Exception (f"Cannot merge ships : ship {index} already merged in {self.index} !")
        self.index += index
        self.index = "".join(sorted(self.index))
        print(self.index)
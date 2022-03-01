from sources.utils import createFixedSprite


class Ship():

    OWN     = 0
    SHIP12  = 1
    SHIP13  = 2
    SHIP23  = 3
    SHIP123 = 4

    def __init__(self, index, position=(0,0)):
        # index of the ship owner
        self.index      = str(index)
        # init positions
        self.x = position[0]
        self.y = position[1]
        # Load all needed sprites
        params = {
            "filePath": f"images/ships/ship0{self.index}.png",
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
                params["filePath"] = f"images/ships/ship{i}{j}.png"
                self.ships[f"{i}{j}"] = createFixedSprite(params)
        params["size"] = (192, 192)
        params["filePath"] = f"images/ships/ship123.png"
        self.ships["123"] = createFixedSprite(params)

    def update(self, deltaTime):
        # Put the current ship at the correct position
        #self.ships[self.index].center_x = self.x
        #self.ships[self.index].center_y = self.y
        pass

    def draw(self):
        self.ships[self.index].draw()

    def mergeWith(self, index):
        index = str(index)
        if index in self.index:
            raise Exception (f"Cannot merge ships : ship {index} already merged in {self.index} !")
        self.index += index
        self.index = "".join(sorted(self.index))
        print(self.index)
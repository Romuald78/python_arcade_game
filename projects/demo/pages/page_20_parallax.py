

from utils.gfx_sfx import createFixedSprite


class Page20Parallax():

    def __init__(self, W, H):
        super().__init__()
        self.W = W
        self.H = H

    def setup(self):
        self.layers = []
        for layer in range(4,-1,-1):
            params = {
                "filePath": f"projects/demo/images/parallax/city2/city2_{layer}.png",
                "size"    : (self.W, self.H),
                "position": (0,300),
                "filterColor": (255, 255, 255, 255),
                "flipH": False,
            }
            if layer == 1:
#                params["filterColor"] = (160,160,160,255)
                params["position"] = (0,300)
            if layer == 2:
                params["position"] = (0,325)
            if layer == 4:
                params["position"] = (0,400)
            s1 = createFixedSprite(params)
            params["position"] = (self.W,params["position"][1])
            s2 = createFixedSprite(params)
            self.layers.append( (s1,s2) )
        self.refX = 0

    def update(self,deltaTime):
        self.refX += (25*deltaTime)%self.W
        # move layers according to refX
        for i in range(len(self.layers)):
            spr = self.layers[i][0]
            spr2 = self.layers[i][1]
            spr.center_x = -self.refX*(i+1)
            while(spr.center_x <= -self.W/2):
                spr.center_x += 2*self.W
            # set next sprites
            if spr.center_x < self.W/2:
                spr2.center_x = spr.center_x + self.W
            else:
                spr2.center_x = spr.center_x - self.W

    def draw(self):
        for layer in self.layers:
            for spr in layer:
                spr.draw()


class Camera():

    def __init__(self, window):

        self.x0 = x0
        self.y0 = y0
        self.W  = W
        self.H  = H

    @property
    def x(self):
        return self.x0
    @property
    def y(self):
        return self.y0
    @property
    def size(self):
        return (self.W, self.H)

    def setPosition(self, pos):
        self.x0 = pos[0]
        self.y0 = pos[1]

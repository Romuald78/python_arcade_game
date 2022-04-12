

class IDisease():

    def __init__(self, params):
        # Params to be restored by the creator
        self.params = params

    # used to provide infinite bombs or reduce to 1
    def getMaxBombs(self):
        raise Exception("Method not implemented yet !!")

    # used for "no bomb" disease or for "auto-drop" disease
    def isDroppingBomb(self):
        raise Exception("Method not implemented yet !!")

    # Used to minimize or maximize fire
    def getMaxPower(self):
        raise Exception("Method not implemented yet !!")

    # used for "very slow" disease or "ultra speed" disease
    def getMaxSpeed(self):
        raise Exception("Method not implemented yet !!")


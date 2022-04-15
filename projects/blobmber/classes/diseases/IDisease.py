import random

from projects.blobmber.classes.constants import Constants


class IDisease():

    NO_BOMB      = 1
    FULL_BOMB    = 2
    AUTO_DROP    = 3
    ONE_POWER    = 4
    FULL_POWER   = 5
    TURTLE_SPEED = 6
    RABBIT_SPEED = 7

    @staticmethod
    def getRandomDisease():
        idx = random.randint(6,7)
        out = None
        if idx == IDisease.NO_BOMB:
            out = DiseaseZeroBomb()
        elif idx == IDisease.FULL_BOMB:
            out = DiseaseFullBombs()
        elif idx == IDisease.AUTO_DROP:
            out = DiseaseAutoDrop()
        elif idx == IDisease.ONE_POWER:
            out = DiseaseOnePower()
        elif idx == IDisease.FULL_POWER:
            out = DiseaseFullPower()
        elif idx == IDisease.TURTLE_SPEED:
            out = DiseaseTurtleSpeed()
        elif idx == IDisease.RABBIT_SPEED:
            out = DiseaseRabbitSpeed()
        # Return disease object ref
        return out

    def __init__(self, time=5):
        self.time = time

    def update(self, deltaTime):
        self.time -= deltaTime

    def isFinished(self):
        return self.time < 0

    # used to provide infinite bombs or reduce to 1
    def getMaxBombs(self):
        raise Exception("Method not implemented yet !!")

    # used for "no bomb" disease (maxbomb 0 ?) or for "auto-drop" disease
    def isDroppingBomb(self):
        raise Exception("Method not implemented yet !!")

    # Used to minimize or maximize fire
    def getMaxPower(self):
        raise Exception("Method not implemented yet !!")

    # used for "very slow" disease or "ultra speed" disease
    def getMaxSpeed(self):
        raise Exception("Method not implemented yet !!")


class DiseaseZeroBomb(IDisease):
    def getMaxBombs(self):
        return 0

class DiseaseFullBombs(IDisease):
    def getMaxBombs(self):
        return 100

class DiseaseAutoDrop(IDisease):
    def isDroppingBomb(self):
        return True

class DiseaseOnePower(IDisease):
    def getMaxPower(self):
        return 1

class DiseaseFullPower(IDisease):
    def getMaxPower(self):
        return 100

class DiseaseTurtleSpeed(IDisease):
    def getMaxSpeed(self):
        return Constants.BLOB_TURTLE_SPEED

class DiseaseRabbitSpeed(IDisease):
    def getMaxSpeed(self):
        return Constants.BLOB_RABBIT_SPEED

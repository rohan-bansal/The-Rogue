import AppEngine
from AppEngine import *

class StationaryObstacle():
    def __init__(self, sprite):
        self.sprite = sprite
        self.x = sprite.x
        self.y = sprite.y

        self.id_ = "stationary"
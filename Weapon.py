import AppEngine
from AppEngine import *

class Weapon():
    def __init__(self, name, image, desc, x, y):
        self.name = name
        self.image = image
        self.desc = desc

        self.weapon = True

        self.pickedUp = False

        self.spriteImage = sprite(self.image, x, y, self.name)
        self.spriteImage.description = self.desc

        self.invSlot = ""

    def assignInvSlot(self,slot):
        self.invSlot = slot

    def use(self):
        pass

    
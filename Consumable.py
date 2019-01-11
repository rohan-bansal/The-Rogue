import AppEngine
from AppEngine import *

import JsonParser
import Spritesheet

class Consumable():
    def __init__(self, name, x, y):

        parser = JsonParser.Parser()
        parser.parse("GameConfig/ItemDatabase.json")

        ss = Spritesheet.spritesheet("Sprites/Spritesheets/pixelArt.png")

        self.name = name
        self.image = ss.image_at(tuple(parser.settings[name]["coords"]), (0, 0, 0, 0))
        self.desc = parser.settings[name]["desc"]

        self.consumable = True

        self.pickedUp = False

        self.spriteImage = sprite(self.image, x, y, self.name)
        self.spriteImage.description = self.desc

        self.invSlot = ""

    def assignInvSlot(self, slot):
        self.invSlot = slot

    def use(self):
        pass

    
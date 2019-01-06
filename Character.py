import AppEngine
from AppEngine import *

class Character(pygame.sprite.Sprite):
    def __init__(self):
        self.storage = {
            1 : "",
            2 : "",
            3 : "",
            4 : "",
            5 : "",
            6 : "",
            7 : ""
        }

        self.itemDimensions = {
            1 : "",
            2 : "",
            3 : "",
            4 : "",
            5 : "",
            6 : "",
            7 : ""
        }

        self.availableSlot = 1
        self.totalFilled = 0

    def addToInventory(self, item):
        if self.totalFilled == 7:
            pass
        else:
            self.storage.update({self.availableSlot : item})
            self.availableSlot += 1
    
    def removeFromInventory(self, index):
        self.storage.update({index : ""})
        if self.availableSlot < index:
            pass
        else:
            self.availableSlot = index

    def addDimensions(self, width, height, index):
        self.itemDimensions.update({index : str(width) + " " + str(height)})

    def findTotalFilled(self):
        for key in self.storage.keys():
            if self.storage[key] != "":
                self.totalFilled += 1
        return self.totalFilled
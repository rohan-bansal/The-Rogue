import AppEngine
from AppEngine import *

import Item
import LevelParser
import Spritesheet

import random

class StageOne():
    def __init__(self):
        self.groundTiles = []
        self.obstacleTiles = []
        self.obstacles = ["dead_vines", "rocks"]

        self.ss1 = Spritesheet.spritesheet("Sprites/Spritesheets/pixelArt.png")

        self.lvl1 = LevelParser.Parser("Level One")
        self.lvl1.parse()

        self.items = []

    def generateGround(self):
        self.lvl1.generate_ground(self.groundTiles)

    def generateObstacles(self):
        self.lvl1.generate_obstacles(self.obstacleTiles)
        
    def generateLevelComplete(self):
        pass

    def spawnTreasure(self):
        self.items.append(Item.Item("Cherry Juice", self.ss1.image_at((238, 102, 32, 32), (0, 0, 0, 0)), True, False, "Food", 600, 700))
        self.items.append(Item.Item("Blackberry", self.ss1.image_at((0, 0, 32, 32), (0, 0, 0, 0)), True, False, "Food", 500, 700))
        self.items.append(Item.Item("Cherry", self.ss1.image_at((35, 0, 32, 32), (0, 0, 0, 0)), True, False, "Food", 400, 700))
        self.items.append(Item.Item("Green Apple", self.ss1.image_at((70, 0, 32, 32), (0, 0, 0, 0)), True, False, "Food", 300, 700))

        return self.items

    def startMusic(self):
        au.playMusic("Music/Level1.ogg", -1)
    
    def destroyStage(self):
        for item in self.groundTiles:
            item.destroy()
        for element in self.obstacleTiles:
            element.destroy()
        


import AppEngine
from AppEngine import *

import Consumable as co
import LevelParser
import Spritesheet

import random


class StageTwo():
    def __init__(self):
        self.groundTiles = []
        self.obstacleTiles = []
        self.hazards = []

        self.lvl2 = LevelParser.Parser("Level Two")
        self.lvl2.parse()

        self.items = []

    def generateGround(self):
        self.lvl2.generate_ground(self.groundTiles)

    def generateObstacles(self):
        self.lvl2.generate_obstacles(self.obstacleTiles)

    def destroy(self):
        self.obstacleTiles.clear()
        self.hazards.clear()
        self.groundTiles.clear()
        self.items.clear()
        self.stopMusic()

    def spawnTreasure(self):
        self.items.append(co.Consumable("Yellow Potion", 600, 700))
        self.items.append(co.Consumable("Small Sword", 500, 700))
        self.items.append(co.Consumable("Red Apple", 400, 700))
        self.items.append(co.Consumable("Orange Potion", 300, 700))

        return self.items

    def startMusic(self):
        au.playMusic("Music/Level1.ogg", -1)
    
    def stopMusic(self):
        au.stopMusic()

    def checkCollision(self, hero):
        heroRect = hero.main.get_rect(topleft=(hero.x, hero.y))
        heroRect.inflate_ip(10, 10)
        for f in self.obstacleTiles:
            fRect = f.sprite.main.get_rect(topleft=(f.sprite.x, f.sprite.y))
            if f.id_ == "stationary":
                if fRect.colliderect(heroRect):
                    if fRect.collidepoint(heroRect.midleft):
                        return "west"
                    if fRect.collidepoint(heroRect.midright):
                        return "east"
                    if fRect.collidepoint(heroRect.midtop):
                        return "north"
                    if fRect.collidepoint(heroRect.midbottom):
                        return "south"
        return ""
                
                
            
        


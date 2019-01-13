import AppEngine
from AppEngine import *

import Consumable as co
import LevelParser
import Spritesheet

import random


class StageThree():
    def __init__(self):
        self.groundTiles = []
        self.obstacleTiles = []
        self.hazards = []

        self.lvl3 = LevelParser.Parser("Level Three")
        self.lvl3.parse()

        self.itemInfo = []

        self.items = []

    def generateGround(self):
        self.lvl3.generate_ground(self.groundTiles)

    def generateObstacles(self):
        self.lvl3.generate_obstacles(self.obstacleTiles)

    def destroy(self):
        for i in self.obstacleTiles:
            i.sprite.destroy()
        #for c in self.hazards:
        #    c.sprite.destroy()
        for f in self.groundTiles:
            f.destroy()
        self.obstacleTiles.clear()
        self.hazards.clear()
        self.groundTiles.clear()
        self.items.clear()
        self.stopMusic()

    def spawnTreasure(self):
        if len(self.items) > 0:
            temp = []
            for item in self.items:
                if item.spriteImage.y != 905:
                    item.spriteImage.destroy()
                    item.spriteImage = None
                    del item
                else:
                    temp.append(item)
            self.items = temp
                    
        else:
            for x in range(len(self.itemInfo)):
                self.items.append(co.Consumable(self.itemInfo[x][0], self.itemInfo[x][1], self.itemInfo[x][2]))

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
                
                
            
        


import AppEngine
from AppEngine import *

import Consumable
import LevelParser
import Spritesheet

import random

class StageOne():
    def __init__(self):
        self.groundTiles = []
        self.obstacleTiles = []
        self.hazards = []

        self.ss1 = Spritesheet.spritesheet("Sprites/Spritesheets/pixelArt.png")

        self.lvl1 = LevelParser.Parser("Level One")
        self.lvl1.parse()

        self.items = []

    def generateGround(self):
        self.lvl1.generate_ground(self.groundTiles)

    def generateObstacles(self):
        self.lvl1.generate_obstacles(self.obstacleTiles)

    def destroy(self):
        self.obstacleTiles.clear()
        self.hazards.clear()
        self.groundTiles.clear()
        self.items.clear()
        self.stopMusic()
        

    def spawnTreasure(self):
        self.items.append(Consumable.Consumable("Cherry Juice", self.ss1.image_at((238, 102, 32, 32), (0, 0, 0, 0)), "Food", 600, 700))
        self.items.append(Consumable.Consumable("Blackberry", self.ss1.image_at((0, 0, 32, 32), (0, 0, 0, 0)), "Food", 500, 700))
        self.items.append(Consumable.Consumable("Cherry", self.ss1.image_at((35, 0, 32, 32), (0, 0, 0, 0)), "Food", 400, 700))
        self.items.append(Consumable.Consumable("Green Apple", self.ss1.image_at((70, 0, 32, 32), (0, 0, 0, 0)), "Food", 300, 700))

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
                
                
            
        


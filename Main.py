import AppEngine
from AppEngine import *

import LevelOne
import JsonParser
import MainMenu
import Character
import Item
import Spritesheet

import Save_Load_Data

import random, time, sys, os


set_window("Roguelike Adventure", 960, 960) # { 15, 14 (*64) [960, 896] }

levelIndex = {
    1 : LevelOne.StageOne()
#   2 : LevelTwo.StageTwo()
}

parser = JsonParser.Parser()
parser.parse("config.json")
musicActive = parser.getMusic()
sfxActive = parser.getSFX()

ss = Spritesheet.spritesheet("Sprites/BlueHairedHero/blue_haired.png")

menuActive = True
heroSpawned = False
inventorySpawned = False

HPred = 0
HPgreen = 255

inventorySlots = []
itemList = []

alpha = (0, 0, 0, 0)

charWalkCycleDown = [ss.image_at((0, 0, 30, 48), alpha), ss.image_at((35, 0, 30, 48), alpha), ss.image_at((70, 0, 30, 48), alpha), ss.image_at((35, 0, 30, 48), alpha)]
charWalkCycleUp = [ss.image_at((0, 156, 30, 48), alpha), ss.image_at((35, 156, 30, 48), alpha), ss.image_at((70, 156, 30, 48), alpha), ss.image_at((35, 156, 30, 48), alpha)]
charWalkCycleRight = [ss.image_at((0, 104, 30, 48), alpha), ss.image_at((35, 104, 30, 48), alpha), ss.image_at((70, 104, 30, 48), alpha), ss.image_at((35, 104, 30, 48), alpha)]
charWalkCycleLeft = [ss.image_at((0, 52, 30, 48), alpha), ss.image_at((35, 52, 30, 48), alpha), ss.image_at((70, 52, 30, 48), alpha), ss.image_at((35, 52, 30, 48), alpha)]

currentSelected = 0
nextAvailableSlot = 320
currentLevel = 1


def start():
    global menuActive, itemList
    menuActive = False
    for x in range(4, 11):
        inventorySlots.append(sprite("Sprites/Inventory/inventory_slot.png", x * 64, 903, "slot" + str(x)))

    levelIndex[currentLevel].generateGround()
    levelIndex[currentLevel].generateObstacles()
    itemList = levelIndex[currentLevel].spawnTreasure()
    if musicActive == True:
        levelIndex[currentLevel].startMusic()
    spawnHero()


def spawnHero():
    global hero, heroChar, heroSpawned, inventorySpawned
    hero = sprite(charWalkCycleRight[0], 128, 453, "hero")
    hero.setHP(100)
    heroSpawned = True
    inventorySpawned = True

    heroChar = Character.Character(hero)
    Sword = Item.Item("Sword", "Sprites/BlueHairedHero/sword.png", False, True, "Primary Weapon", 260, 905)
    Sword.assignInvSlot(1)
    heroChar.addDimensions(Sword.spriteImage.width, Sword.spriteImage.height, heroChar.availableSlot)
    heroChar.addToInventory(Sword)
    Sword.pickedUp = True
    itemList.append(Sword)


def deleteHero(hero):
    global heroSpawned
    del(hero)
    heroSpawned = False


menu = MainMenu.Menu()
if musicActive == True:
    menu.startMusic()

hoverText = text("", 13, black, 0, 0)

optionClicked = False

walkCycleRate = 0
walkFrame = 0

while(True):

    if walkCycleRate != 4:
        walkCycleRate += 1
    else:
        if walkFrame != 3:
            walkFrame += 1
        else:
            walkFrame = 0
        walkCycleRate = 0

    if menuActive == True:
        menu.detectHovers()
        if menu.detectInfoClick() == True:
            optionClicked = True
        if menu.detectLoadClick() == True:
            optionClicked = True
        if optionClicked == True:
            if menu.detectBackArrow() == True:
                optionClicked = False
        if menu.detectPlayClick() == True:
            start()

    for item in itemList:

        if heroChar.storage[currentSelected + 1] == item:
            hoverText.changeText(item.name, black)
            hoverText.x = item.spriteImage.x
            hoverText.y = item.spriteImage.y - 30

        if hero.collide(item.spriteImage) and kb.activeKeys[K_e]:
            if heroChar.findTotalFilled() == 7:
                pass
            else:
                if sfxActive == True:
                    au.playSound("Music/Pick_Up.ogg")
                heroChar.addToInventory(item)
                heroChar.addDimensions(item.spriteImage.width, item.spriteImage.height, heroChar.availableSlot - 1)
                item.assignInvSlot(heroChar.availableSlot - 1)
                item.spriteImage.main = pygame.transform.scale(item.spriteImage.main, (48, 48))
                item.pickedUp = True
                item.spriteImage.x = nextAvailableSlot
                item.spriteImage.y = 905
                nextAvailableSlot += 64


    if kb.activeKeys[K_q] and heroChar.storage[currentSelected + 1] != "":
        if nextAvailableSlot < inventorySlots[currentSelected].x:
            pass
        else:
            nextAvailableSlot = inventorySlots[currentSelected].x
        if sfxActive == True:
            au.playSound("Music/Drop.ogg")
        hoverText.changeText("", black)
        itemSprite = heroChar.storage[currentSelected + 1].spriteImage
        dimen = heroChar.itemDimensions[currentSelected + 1].split(" ")
        itemSprite.main = pygame.transform.scale(itemSprite.main, ( int(dimen[0]) , int(dimen[1]) ))
        itemSprite.x = hero.x
        itemSprite.y = hero.y
        heroChar.storage[currentSelected + 1].pickedUp = False
        heroChar.storage[currentSelected + 1].invSlot = ""
        heroChar.removeFromInventory(currentSelected + 1)

    if kb.activeKeys[K_1]:
        currentSelected = 0
    elif kb.activeKeys[K_2]:
        currentSelected = 1
    elif kb.activeKeys[K_3]:
        currentSelected = 2
    elif kb.activeKeys[K_4]:
        currentSelected = 3
    elif kb.activeKeys[K_5]:
        currentSelected = 4
    elif kb.activeKeys[K_6]:
        currentSelected = 5
    elif kb.activeKeys[K_7]:
        currentSelected = 6
    
    if inventorySpawned == True:
        for s in range(7):
            if s == currentSelected:
                inventorySlots[s].modifyImage("Sprites/Inventory/inventory_slot_selected.png")
            else:
                inventorySlots[s].modifyImage("Sprites/Inventory/inventory_slot.png")

    if heroSpawned == True:
        hero.drawHealthText(hero.x - 3, hero.y - 24, 20, (HPred, HPgreen, 0), str(hero.HP))
        if (kb.activeKeys[K_w] or kb.activeKeys[K_UP]) and hero.edgeTop > 0:
            hero.modifyImage(charWalkCycleUp[walkFrame])
            hero.y -= 4
        if (kb.activeKeys[K_s] or kb.activeKeys[K_DOWN]) and hero.edgeBottom < 896:
            hero.modifyImage(charWalkCycleDown[walkFrame])
            hero.y += 4
        if (kb.activeKeys[K_a] or kb.activeKeys[K_LEFT]) and hero.edgeLeft > 0:
            hero.modifyImage(charWalkCycleLeft[walkFrame])
            hero.x -= 4
        if (kb.activeKeys[K_d] or kb.activeKeys[K_RIGHT]) and hero.edgeRight < 960:
            hero.modifyImage(charWalkCycleRight[walkFrame])
            hero.x += 4

        for item in levelIndex[currentLevel].obstacleTiles:
            if item.collide(hero):
                if hero.HP != 0:
                    hero.HP -= 1
                if HPred != 255:
                    HPred += 5.1
                    HPred = round(HPred)
                elif HPgreen != 0:
                    HPgreen -= 5.1
                    HPgreen = round(HPgreen)

    gameLoop(black)
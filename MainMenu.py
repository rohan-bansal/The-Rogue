import AppEngine
from AppEngine import *

import tkinter as tk
from tkinter import filedialog

class Menu():
    def __init__(self):
        self.hoverable = True

        self.root = tk.Tk()
        self.root.withdraw()

        self.file_ = ""

        self.render()

    def render(self):
        self.nameText = sprite("Sprites/Menu/RogueTitle1.png", 150, 100, "titleText")

        self.playButton = sprite("Sprites/Menu/playButton.png", 400, 700, "playButton")
        self.playText = sprite("Sprites/Menu/playHoverText2.png", 300, 650, "playHoverText")

        self.infoIcon = sprite("Sprites/Menu/infoIcon2.png", 180, 710, "InfoPageIcon")
        self.infoText = sprite("Sprites/Menu/infoHoverText.png", 20, 650, "InfoPageHoverText")

        self.loadIcon = sprite("Sprites/Menu/loadGame.png", 717, 710, "LoadGameIcon")
        self.loadText = sprite("Sprites/Menu/loadGameHoverText2.png", 580, 655, "LoadGameHoverText")

        self.backButton = sprite("Sprites/Menu/back.png", 20, 850, "backButton")

        self.infoTitle = text("How> To> Play>", 80, gray, 25, 50)
        self.infoTitle.changeFont("Fonts/Barbarian.ttf")

        self.info_1 = text("Use arrow keys or WASD to move.", 15, (165, 152, 13), 20, 200)
        self.info_2 = text('Press "E" to pick up items.', 15, (165, 152, 13), 20, 240)
        self.info_3 = text('Press "Q" to drop items.', 15, (165, 152, 13), 20, 280)
        self.info_4 = text('Press "U" to use items.', 15, (165, 152, 13), 20, 320)
        self.info_5 = text('Find items, fight monsters, and progress through puzzle and PvE levels.', 15, (165, 152, 13), 20, 380)
        self.info_6 = text('More information will be given in-game.', 15, (165, 152, 13), 20, 420)
        self.infoList = [self.info_1, self.info_2, self.info_3, self.info_4, self.info_5, self.info_6]

        for item in self.infoList:
            item.changeFont("Fonts/Fipps-Regular.otf")

        self.playText.hide()
        self.infoText.hide()
        self.infoTitle.hide()
        self.loadText.hide()
        self.backButton.hide()
        
        self.modInfos("hide")

        self.menuWidgets = [self.nameText, self.playButton, self.playText, self.infoIcon, self.infoText, self.loadIcon, self.loadText]

    def modInfos(self, method):
        if method == "hide":
            for item in self.infoList:
                item.hide()
        if method == "show":
            for item in self.infoList:
                item.show()

    def detectHovers(self):
        if ms.hoverSprite(self.playButton):
            if self.hoverable == True:
                self.playText.show()
            self.playButton.modifyImage("Sprites/Menu/playButtonLarge.png")
        else:
            self.playText.hide()
            self.playButton.modifyImage("Sprites/Menu/playButton.png")
        
        if ms.hoverSprite(self.infoIcon):
            if self.hoverable == True:
                self.infoText.show()
            self.infoIcon.modifyImage("Sprites/Menu/infoIcon2Large.png")
        else:
            self.infoText.hide()
            self.infoIcon.modifyImage("Sprites/Menu/infoIcon2.png")

        if ms.hoverSprite(self.loadIcon):
            if self.hoverable == True:
                self.loadText.show()
            self.loadIcon.modifyImage("Sprites/Menu/loadGameLarge.png")
        else:
            self.loadText.hide()
            self.loadIcon.modifyImage("Sprites/Menu/loadGame.png")

    def removeWidgets(self):
        for item in self.menuWidgets:
            item.hide()

    def detectPlayClick(self):
        if ms.hoverSprite(self.playButton) and ms.spriteClicked(self.playButton):
            del(self)
            return True

    def detectInfoClick(self):
        if ms.hoverSprite(self.infoIcon) and ms.spriteClicked(self.infoIcon):
            self.hoverable = False
            self.removeWidgets()
            self.backButton.show()
            self.infoTitle.show()
            self.modInfos("show")

            return True

    def detectLoadClick(self):
        if ms.hoverSprite(self.loadIcon) and ms.spriteClicked(self.loadIcon):
            try:
                self.file_ = filedialog.askopenfile()
            except:
                print("Error importing file dialog. Exiting.")
                raise ImportError

            return True

    def detectBackArrow(self):
        if ms.hoverSprite(self.backButton):
            self.backButton.modifyImage("Sprites/Menu/backLarge.png")
        else:
            self.backButton.modifyImage("Sprites/Menu/back.png")
        if ms.hoverSprite(self.backButton) and ms.spriteClicked(self.backButton):
            self.infoTitle.hide()
            self.modInfos("hide")
            self.backButton.hide()
            self.render()
            self.hoverable = True  
            return True

    def startMusic(self):
        au.playMusic("Music/MainMenu.ogg", -1)
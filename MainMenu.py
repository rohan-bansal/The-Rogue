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

        self.info = sprite("Sprites/Menu/InfoText.png", 25, 200, "InfoText")

        self.playText.hide()
        self.infoText.hide()
        self.loadText.hide()
        self.backButton.hide()
        self.info.hide()

        self.menuWidgets = [self.nameText, self.playButton, self.playText, self.infoIcon, self.infoText, self.loadIcon, self.loadText]

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
            self.info.show()
            self.backButton.show()
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
            self.info.hide()
            self.backButton.hide()
            self.render()
            self.hoverable = True  
            return True

    def startMusic(self):
        au.playMusic("Music/MainMenu.ogg", -1)
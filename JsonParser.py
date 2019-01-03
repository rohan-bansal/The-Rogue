import sys, json

class Parser():
    
    def __init__(self):
        self.info = ""
        self.settings = ""

        self.startingLevel = ""
        self.music = True
        self.sfx = True

    def parse(self, file_):
        self.info = open(file_, "r").read()
        self.settings = json.loads(self.info)

        self.startingLevel = self.settings['levelSettings']['starting_level']
        self.music = self.settings['musicSettings']['music']
        self.sfx = self.settings['musicSettings']['SFX']

    def getStartingLevel(self):
        return self.startingLevel

    def getMusic(self):
        return self.music

    def getSFX(self):
        return self.sfx
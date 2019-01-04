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

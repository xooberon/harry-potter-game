'''
Created on 4/02/2017

@author: Miranda
'''

import json

class CharacterInfo:
    characterName = ""
    
    gold = 0
    level = 1
    xp = 0
    initiative = 0
    speed = 5

    def __init__(self):
        with open('data/CharacterInfoData.json') as data_file:
            data = json.load(data_file)
        self.backgroundValues       = data["backgroundValues"]
        self.characteristicValues   = data["characteristicValues"]
        self.wandCoreValues         = data["wandCoreValues"]
        self.wandWoodValues         = data["wandWoodValues"]
        self.houseValues            = data["houseValues"]

        self.background     = self.backgroundValues[0]
        self.characteristic = self.characteristicValues[0]
        self.wandCore       = self.wandCoreValues[0]
        self.wandWood       = self.wandWoodValues[0]
        self.house          = self.houseValues[0]

    def setCharacterName(self, characterName):
        self.characterName = characterName

    def getCharacterName(self):
        return self.characterName

    def setBackground(self, background):
        self.background = background

    def getBackground(self):
        return self.background

    def setCharacteristic(self, characteristic):
        self.characteristic = characteristic

    def getCharacteristic(self):
        return self.characteristic

    def setStartingGold(self):
        if( self.characteristic == "Wealthy" ):
            self.addGold(300, 0, 0)
        else:
            self.addGold(150, 0, 0)

    def addGold(self, galleons, sickles, knuts):
        self.gold = self.gold + knuts + sickles*29 + galleons*29*17

    def removeGold(self, galleons, sickles, knuts):
        knutsToRemove = knuts + sickles*29 + galleons*17*29
        if( self.gold > knutsToRemove ):
            self.gold = self.gold - knutsToRemove
        else:
            return "You can not afford this!"

    def getGold(self):
        galleons = int(self.gold/(29*17))
        remainder = self.gold - galleons*29*17
        sickles = int(remainder/29)
        knuts = self.gold - galleons*29*17 - sickles*29
        
        return [str(galleons), str(sickles), str(knuts)]

    def setWandCore(self, wandCore):
        self.wandCore = wandCore

    def getWandCore(self):
        return self.wandCore

    def setWandWood(self, wandWood):
        self.wandWood = wandWood

    def getWandWood(self):
        return self.wandWood

    def setHouse(self, house):
        self.house = house

    def getHouse(self):
        return self.house

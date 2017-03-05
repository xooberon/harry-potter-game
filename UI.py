import tkinter as tk
from CharacterInfo import CharacterInfo

def createWhiteSpace(frame):
    whiteSpace = tk.Label(frame, text="", background="white")
    whiteSpace.pack()

def createMessage(frame, text):
    nameMessage = tk.Label(frame, text=text, background="white")
    nameMessage.pack()

def createMenu(frame, options, callback):
    defaultOption = tk.StringVar(frame)
    defaultOption.set(options[0])
    menu = tk.OptionMenu(frame, defaultOption, *options, command=callback)
    menu.config(background="white")
    menu["menu"].config(background="white")
    menu.pack()

def createEntryField(frame, buttonText, callback):
    entryFieldFrame = tk.Frame(frame, background="white")
    entryFieldFrame.pack()

    defaultText = tk.StringVar(frame)
    entry = tk.Entry(entryFieldFrame, textvariable=defaultText)
    entry.pack(side=tk.LEFT)
    button = tk.Button(entryFieldFrame, text=buttonText, command=callback, background="white")
    button.pack(side=tk.LEFT)

    return entry

def createNextButton(frame, callback):
    nextButton = tk.Button(frame, text="Next page", command=callback, background="white")
    createWhiteSpace(frame)
    nextButton.pack()

def createWandMenus(self):
    wandFrame = tk.Frame(self, background="white")
    wandFrame.pack()

    def wandCoreWasSet(wandCore):
        self.characterInfo.setWandCore(wandCore)
    def wandWoodWasSet(wandWood):
        self.characterInfo.setWandWood(wandWood)

    wandCores = self.createMenu(wandFrame, self.characterInfo.wandCoreValues, wandCoreWasSet)
    wandCores.pack(side=tk.LEFT)

    wandWoods = self.createMenu(wandFrame, self.characterInfo.wandWoodValues, wandWoodWasSet)
    wandWoods.pack(side=tk.LEFT)

def createHouseMenu(self):
    def houseWasSet(house):
        self.characterInfo.setHouse(house)
    houses = self.createMenu(self, self.characterInfo.houseValues, houseWasSet)
    houses.pack()

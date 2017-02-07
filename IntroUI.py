'''
Created on 4/02/2017

@author: Miranda
'''

import tkinter as tk
from tkinter import messagebox
from CharacterInfo import CharacterInfo
from DiagonAlley import DiagonAlley

class IntroUI(tk.Frame):
  
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        self.characterInfo = CharacterInfo()
        self.currentPage = 0
        self.nextButtonExists = False

        self.parent.title("Character Sheet")
        self.pack(fill=tk.BOTH, expand=1)

    def createIntroPage(self):
        if( self.currentPage == 0 ):
            self.createIntroFirstPage()
        elif( self.currentPage == 1 ):
            self.createIntroSecondPage()
        else:
            self.createIntroThirdPage()

    def createIntroFirstPage(self):
        self.createMessage("Welcome to the wizarding world! What is your name?")
        self.createCharacterNameField()
        whiteSpace1 = tk.Label(self, text="", background="white")
        whiteSpace1.pack()
        self.createMessage("Were you raised in the Muggle world or in the wizarding world?")
        self.createBackgroundMenu()
        whiteSpace2 = tk.Label(self, text="", background="white")
        whiteSpace2.pack()
        self.createMessage("What characteristic have you chosen?")
        self.createCharacteristicMenu()

    def createIntroSecondPage(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.nextButtonExists = False
        self.characterInfo.setStartingGold()
        gold = self.characterInfo.getGold()
        self.createMessage("Welcome to Diagon Alley! You have " + gold[0] + " galleons, " + gold[1] + " sickles, and " + gold[2] + " knuts to spend.")
        whiteSpace = tk.Label(self, text="", background="white")
        whiteSpace.pack()
        diagonAlley = DiagonAlley(self)
        diagonAlley.displayUI()

        def goToKnockturnAlley():
            print("knockturn")
        knockturnAlleyButton = tk.Button(self, text="Knockturn Alley", command=goToKnockturnAlley, background="white")
        knockturnAlleyButton.place(relx=0, rely=.2, anchor=tk.NW)
#        self.createMessage("The wand chooses the wizard! What wand chose you?")
#        self.createWandMenus()

    def createIntroThirdPage(self):
        self.createMessage("Your house is like your family at Hogwarts. What house are you in?")
        self.createHouseMenu()

    def createMessage(self, text):
        nameMessage = tk.Label(self, text=text, background="white")
        nameMessage.pack()

    def createMenu(self, parent, options, callback):
        defaultOption = tk.StringVar(self)
        defaultOption.set(options[0])
        menu = tk.OptionMenu(parent, defaultOption, *options, command=callback)
        menu.config(background="white")
        menu["menu"].config(background="white")
        return menu

    def createEntryField(self, buttonText, callback):
        frame = tk.Frame(self, background="white")
        frame.pack()
        
        defaultText = tk.StringVar(self)
        entry = tk.Entry(frame, textvariable=defaultText)
        entry.pack(side=tk.LEFT)
        button = tk.Button(frame, text=buttonText, command=callback, background="white")
        button.pack(side=tk.LEFT)

        return entry

    def createCharacterNameField(self):
        def characterNameWasSet():
            name = nameEntry.get()
            if( len(name)!=0 ):
                self.characterInfo.setCharacterName(nameEntry.get())
                self.parent.title("Character Sheet for " + self.characterInfo.getCharacterName())
                self.createNextButton()

        nameEntry = self.createEntryField("Set name", characterNameWasSet)

    def createNextButton(self):
        if( self.nextButtonExists == False ):
            def moveToPageTwo():
                result = tk.messagebox.askokcancel("Are you sure?", "You cannot go back and edit these values.")
                if( result ):
                    self.currentPage = self.currentPage+1
                    self.createIntroPage()
            nextButton = tk.Button(self, text="Next page", command=moveToPageTwo, background="white")
            whiteSpace = tk.Label(self, text="", background="white")
            whiteSpace.pack()
            nextButton.pack()
            self.nextButtonExists = True

    def createBackgroundMenu(self):
        def backgroundWasSet(background):
            self.characterInfo.setBackground(background)

        backgrounds = self.createMenu(self, self.characterInfo.backgroundValues, backgroundWasSet)
        backgrounds.pack()

    def createCharacteristicMenu(self):
        def characteristicWasSet(characteristic):
            self.characterInfo.setCharacteristic(characteristic)

        characteristics = self.createMenu(self, self.characterInfo.characteristicValues, characteristicWasSet)
        characteristics.pack()

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

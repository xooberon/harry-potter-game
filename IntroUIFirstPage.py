import tkinter as tk
from tkinter import messagebox
from CharacterInfo import CharacterInfo
import UI


class IntroUIFirstPage(tk.Frame):
    def __init__(self, parent, root):
        tk.Frame.__init__(self, parent, background="white")

        self.parent = parent
        self.root = root
        self.characterInfo = CharacterInfo()
        self.nameSet = False
        self.backgroundSet = False
        self.characteristicSet = False

    def displayUI(self):
        def nameCallback():
            name = nameEntry.get()
            if(len(name) != 0):
                self.characterInfo.setCharacterName(nameEntry.get())
                name = self.characterInfo.getCharacterName()
                self.root.title("Character Sheet for " + name)
                self.nameSet = True
                self.updateNextButton()

        def backgroundCallback(background):
            self.characterInfo.setBackground(background)
            self.backgroundSet = True
            self.updateNextButton()

        def characteristicCallback(characteristic):
            self.characterInfo.setCharacteristic(characteristic)
            self.characteristicSet = True
            self.updateNextButton()

        UI.createWhiteSpace(self)
        welcomeMessage = "Welcome to the wizarding world! What is your name?"
        UI.createMessage(self, welcomeMessage)
        nameEntry = UI.createEntryField(self, "Set name", nameCallback)
        UI.createWhiteSpace(self)
        backgroundMessage1 = "Were you raised in the Muggle world"
        backgroundMessage2 = " or in the wizarding world?"
        UI.createMessage(self, backgroundMessage1 + backgroundMessage2)
        backgroundValues = self.characterInfo.backgroundValues
        UI.createMenu(self, backgroundValues, backgroundCallback)
        UI.createWhiteSpace(self)
        UI.createMessage(self, "What characteristic have you chosen?")
        characteristicValues = self.characterInfo.characteristicValues
        UI.createMenu(self, characteristicValues, characteristicCallback)

    def updateNextButton(self):
        def moveToPageTwo():
            messageTitle = "Are you sure?"
            messageText = "You cannot go back and edit these values."
            result = tk.messagebox.askokcancel(messageTitle, messageText)
            if(result):
                self.parent.displayNextPage()
                for widget in self.winfo_children():
                    widget.destroy()

        if(self.nameSet is True & self.backgroundSet is True & self.characteristicSet is True):
            UI.createNextButton(self, moveToPageTwo)

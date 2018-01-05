import tkinter as tk
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

        def storyCallback():
            text = "You are ready to enter the world of Hogwarts!"
            UI.createMessage(self, text)

        UI.createWhiteSpace(self)
        welcomeMessage = "Welcome to the wizarding world! What is your name?"
        UI.createMessage(self, welcomeMessage)
        nameEntry = UI.createEntryField(self, "Set name", nameCallback)
        UI.createWhiteSpace(self)
        storyMessage1 = "Enter your story below "
        storyMessage2 = "or simply tell the GM about your life so far."
        UI.createMessage(self, storyMessage1 + storyMessage2)
        size = UI.bodyWidth(self.root)
        text = "I'm finished!"
        UI.createMultiLineEntryField(self, text, size, size, storyCallback)
        # in future will need to assign the above to some variable and send it
        # to the character manager

    def updateNextButton(self):
        def moveToPageTwo():
            self.parent.displayNextPage()
            for widget in self.winfo_children():
                widget.destroy()

        if(self.nameSet is True):
            UI.createNextButton(self, moveToPageTwo)

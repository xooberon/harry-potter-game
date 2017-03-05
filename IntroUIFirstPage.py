import tkinter as tk
from CharacterInfo import CharacterInfo
import UI

class IntroUIFirstPage(tk.Frame):
    def __init__(self, parent, root):
        tk.Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        self.root = root
        self.characterInfo = CharacterInfo()
        self.nextButtonExists = False

    def displayUI(self):
        def characterNameCallback():
            def moveToPageTwo():
                result = tk.messagebox.askokcancel("Are you sure?", "You cannot go back and edit these values.")
                if( result ):
                    self.parent.displayNextPage()
            name = nameEntry.get()
            if( len(name)!=0 ):
                self.characterInfo.setCharacterName(nameEntry.get())
                self.root.title("Character Sheet for " + self.characterInfo.getCharacterName())
                if( self.nextButtonExists == False ):
                    UI.createNextButton(self, moveToPageTwo)
                    self.nextButtonExists == True
        def backgroundCallback(background):
            self.characterInfo.setBackground(background)
        def characteristicCallback(characteristic):
            self.characterInfo.setCharacteristic(characteristic)

        UI.createWhiteSpace(self)
        UI.createMessage(self, "Welcome to the wizarding world! What is your name?")
        nameEntry = UI.createEntryField(self, "Set name", characterNameCallback)
        UI.createWhiteSpace(self)
        UI.createMessage(self, "Were you raised in the Muggle world or in the wizarding world?")
        UI.createMenu(self, self.characterInfo.backgroundValues, backgroundCallback)
        UI.createWhiteSpace(self)
        UI.createMessage(self, "What characteristic have you chosen?")
        UI.createMenu(self, self.characterInfo.characteristicValues, characteristicCallback)

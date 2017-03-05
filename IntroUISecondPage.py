import tkinter as tk
from CharacterInfo import CharacterInfo
from DiagonAlley import DiagonAlley
import UI

class IntroUISecondPage(tk.Frame):
    def __init__(self, parent, root):
        tk.Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        self.root = root
        self.characterInfo = CharacterInfo()

    def displayUI(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.characterInfo.setStartingGold()
        gold = self.characterInfo.getGold()
        UI.createMessage(self,"Welcome to Diagon Alley! You have " + gold[0] + " galleons, " + gold[1] + " sickles, and " + gold[2] + " knuts to spend.")
        UI.createWhiteSpace(self)
        diagonAlley = DiagonAlley(self)
        diagonAlley.displayUI()

        def goToKnockturnAlley():
            print("knockturn")
        knockturnAlleyButton = tk.Button(self, text="Knockturn Alley", command=goToKnockturnAlley, background="white")
        knockturnAlleyButton.place(relx=0, rely=.8, anchor=tk.NW)


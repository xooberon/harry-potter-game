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
        self.characterInfo.setStartingGold()
        gold = self.characterInfo.getGold()
        UI.createMessage(self, "Welcome to Diagon Alley!")
        text = ("You have " + gold[0] + " galleons, " + gold[1] + " sickles,"
                "and " + gold[2] + " knuts to spend.")
        UI.createMessage(self, text)
        UI.createWhiteSpace(self)
        diagonAlley = DiagonAlley(self, self.root)
        diagonAlley.displayUI()

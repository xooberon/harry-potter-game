import tkinter as tk
from CharacterInfo import CharacterInfo
import UI


class Shop(tk.Frame):
    def __init__(self, parent, name, fileName):
        tk.Frame.__init__(self, parent, background="white")

        self.parent = parent
        self.characterInfo = CharacterInfo()
        self.pack()

    def showUI(self):
        UI.createMessage(self, "test")
        # nameMessage = tk.Label(self, text="test", background="white")
        # nameMessage.pack()

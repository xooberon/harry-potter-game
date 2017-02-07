import tkinter as tk
from CharacterInfo import CharacterInfo

class Shop(tk.Frame):
    def __init__(self, parent, name, inventory):
        tk.Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        self.characterInfo = CharacterInfo()
        self.pack()

    def showUI(self):
        nameMessage = tk.Label(self, text="test", background="white")
        nameMessage.pack()

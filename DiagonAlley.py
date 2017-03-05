import tkinter as tk
import json
from CharacterInfo import CharacterInfo
from Shop import Shop

class DiagonAlley(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        self.characterInfo = CharacterInfo()
        self.pack()

        with open('data/DiagonAlleyData.json') as data_file:
            self.shops = json.load(data_file)

    def displayUI(self):
        self.buttons = []
        shopNames = list(self.shops)
        for i in range(len(self.shops)):
            x = int(i/3)
            y = i%3
            name = shopNames[i]
            callback = lambda name=name:goToShop(name)
            if( y==0 ):
                self.buttons.append([])
            self.buttons[x].append(tk.Button(self, text=name, command=callback, background="white"))
            self.buttons[x][y].pack()

        def goToShop(name):
            self.goToShop(name)

    def goToShop(self, name):
        inventory = self.shops[name]["inventory"]
        shop = Shop(self.parent, name, inventory)
        for widget in self.winfo_children():
            widget.destroy()
        shop.showUI()

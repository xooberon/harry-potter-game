import tkinter as tk
import json
import UI
from CharacterInfo import CharacterInfo
from Shop import Shop


class DiagonAlley(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="white")

        self.parent = parent
        self.characterInfo = CharacterInfo()
        self.pack()

        with open('data/diagonAlleyData.json') as data_file:
            self.shops = json.load(data_file)

    def displayUI(self):
        self.buttons = []
        shopNames = list(self.shops)
        for i in range(len(self.shops)):
            x = int(i / 3)
            y = i % 3
            name = shopNames[i]

            callback = lambda name=name:goToShop(name)
            if(y == 0):
                self.buttons.append([])
            self.buttons[x].append(tk.Button(self, text=name, command=callback, background="white"))
            self.buttons[x][y].pack()
        UI.createWhiteSpace(self)

        def goToKnockturnAlley():
            print("knockturn")
        knockturnAlleyButton = tk.Button(self, text="Knockturn Alley", command=goToKnockturnAlley, background="white")
        knockturnAlleyButton.pack()

        def goToShop(name):
            self.goToShop(name)

    def goToShop(self, name):
        for widget in self.winfo_children():
            print("test")
            widget.destroy()
        print(name)
        fileName = self.shops[name]["fileName"]
        shop = Shop(self, name, fileName)
        shop.showUI()

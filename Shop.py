import tkinter as tk
import json
from CharacterInfo import CharacterInfo
import UI


class Shop(tk.Frame):
    def __init__(self, parent, root, name, fileName, callback):
        tk.Frame.__init__(self, parent, background="white")

        self.parent = parent
        self.root = root
        self.name = name
        self.callback = callback
        self.characterInfo = CharacterInfo()
        self.pack()
        with open('data/' + fileName) as data_file:
            print(fileName)
            self.shopData = json.load(data_file)

    def showUI(self):
        inventory = self.shopData["inventory"]
        inventory_size = len(inventory)
        width = UI.bodyWidth(self.root)
#        height = UI.bodyHeight(self.root)
        item_size = 100
        inventory_frame = tk.Frame(self, background="white")
        inventory_frame.pack()

        col = width // item_size
#        row = height // item_size
#        pages = inventory_size // (col * row)

        for i in range(inventory_size):
            name = inventory[i]["name"]
            shopItem = UI.createShopItem(inventory_frame, name, item_size, item_size)
            shopItem.grid(row=i // col, column=i % col)
        button_text = "Return to Diagon Alley"
        backButton = backButton = UI.createBackButton(inventory_frame, button_text, self.callback)
        backButton.grid(row=999, column=col // 2)

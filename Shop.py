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
        inventoryFrame = tk.Frame(self, background="white")
        inventoryFrame.pack()

        startIndices = []
        startIndices.append(0)
        self.displayPage(inventory, inventoryFrame, 0, startIndices)

    def displayPage(self, inventory, frame, pageNumber, startIndices):
        itemSize = 100
        labelHeight = 2
        width = UI.bodyWidth(self.root)
        col = width // itemSize

        for widget in frame.winfo_children():
            widget.destroy()

        start = startIndices[pageNumber]
        for i in range(start, len(inventory)):
            name = inventory[i]["name"]
            column = i % col
            itemImage = UI.createShopItemImage(frame, name, itemSize, itemSize)
            itemImage.grid(row=i // col * 4, column=column)
            itemLabel = UI.createShopItemLabel(frame, name, itemSize, labelHeight)
            itemLabel.grid(row=i // col * 4 + 1, column=column)
            buttonFrame = tk.Frame(frame, background="yellow")
            UI.createBuyButton(buttonFrame)
            UI.createDetailsButton(buttonFrame)
            buttonFrame.grid(row=i // col * 4 + 2, column=column)
            if(column == col - 1 and self.readyForNextPage(frame, itemSize, itemLabel, buttonFrame)):
                startIndices.append(i + 1)
                break
            UI.emptyRow(frame).grid(row=i // col * 4 + 3, column=column)

        def goForwardCallback():
            self.displayPage(inventory, frame, pageNumber + 1, startIndices)

        def goBackCallback():
            self.displayPage(inventory, frame, pageNumber - 1, startIndices)

        if(pageNumber != 0):
            backButton = UI.createButton(frame, "Previous", goBackCallback)
            backButton.grid(row=999, column=0)

        buttonText = "Return to Diagon Alley"
        diagonAlleyButton = UI.createButton(frame, buttonText, self.callback)
        diagonAlleyButton.grid(row=999, column=col // 2)

        if(i + 1 != end):
            nextButton = UI.createButton(frame, "More", goForwardCallback)
            nextButton.grid(row=999, column=col - 1)

    def readyForNextPage(self, frame, imageHeight, label, button):
        frame.update()
        frameHeight = frame.winfo_height()
        labelHeight = label.winfo_height()
        buttonHeight = button.winfo_height()
        itemHeight = imageHeight + labelHeight + buttonHeight
        # Create a next page if the current height plus the height of one more
        # item is more than the window height
        return frameHeight + itemHeight > UI.windowHeight(self.root)

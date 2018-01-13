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
        shopType = self.shopData["shop-type"]
        inventory = self.shopData["inventory"]
        inventoryFrame = tk.Frame(self, background="white")
        inventoryFrame.pack()

        if(shopType == "grid"):
            startIndices = []
            startIndices.append(0)
            buttonText = "Return to Diagon Alley"
            self.displayPage(inventory, inventoryFrame, 0, startIndices, buttonText, self.callback)
        elif(shopType == "subsection"):
            self.displaySubsections(inventory, inventoryFrame)

    def displaySubsections(self, inventory, frame):
        buttons = []
        sectionNames = list(inventory)
        for i in range(len(inventory)):
            name = sectionNames[i]

            callback = lambda name=name:goToSection(name)
            buttons.append(tk.Button(frame, text=name, command=callback, background="white"))
            buttons[i].pack()
        UI.createWhiteSpace(frame)
        UI.createWhiteSpace(frame)

        buttonText = "Return to Diagon Alley"
        diagonAlleyButton = UI.createButton(frame, buttonText, self.callback)
        diagonAlleyButton.pack()

        def goToSection(name):
            for widget in frame.winfo_children():
                widget.destroy()

            def buttonCallback():
                for widget in frame.winfo_children():
                    widget.destroy()
                self.displaySubsections(inventory, frame)

            startIndices = []
            startIndices.append(0)
            sectionInventory = inventory[name]["inventory"]
            buttonText = "Return to " + self.name
            self.displayPage(sectionInventory, frame, 0, startIndices, buttonText, buttonCallback)


    def displayPage(self, inventory, frame, pageNumber, startIndices, buttonText, buttonCallback):
        imageSize = 100
        labelHeight = 2
        width = UI.bodyWidth(self.root)
        col = width // imageSize    # Put as many columns as can fit based on the image size
        itemSize = width / col      # However the item may take up the full available width
        print("itemSize")
        print(itemSize)
        print(width)

        for widget in frame.winfo_children():
            widget.destroy()

        start = startIndices[pageNumber]
        for i in range(start, len(inventory)):
            name = inventory[i]["name"]
            price = inventory[i]["price"]
            column = i % col
            itemImage = UI.createShopItemImage(frame, name, imageSize, imageSize)
            itemImage.grid(row=i // col * 4, column=column)
            itemLabel = UI.createShopItemLabel(frame, name, price, itemSize, labelHeight)
            itemLabel.grid(row=i // col * 4 + 1, column=column)
            buttonFrame = tk.Frame(frame, background="white")
            UI.createBuyButton(buttonFrame)
            UI.createDetailsButton(buttonFrame)
            buttonFrame.grid(row=i // col * 4 + 2, column=column)
            if(column == col - 1 and self.readyForNextPage(frame, imageSize, itemLabel, buttonFrame)):
                startIndices.append(i + 1)
                break
            UI.emptyRow(frame).grid(row=i // col * 4 + 3, column=column)

        def goForwardCallback():
            self.displayPage(inventory, frame, pageNumber + 1, startIndices, buttonText, buttonCallback)

        def goBackCallback():
            self.displayPage(inventory, frame, pageNumber - 1, startIndices, buttonText, buttonCallback)

        navigationFrame = tk.Frame(frame, background="white")
        backButton = UI.createButton(navigationFrame, "Previous", goBackCallback)
        backButton.grid(row=0, column=0)
        if(pageNumber == 0):
            backButton.config(state=tk.DISABLED)

        diagonAlleyButton = UI.createButton(navigationFrame, buttonText, buttonCallback)
        diagonAlleyButton.grid(row=0, column=1)

        nextButton = UI.createButton(navigationFrame, "More", goForwardCallback)
        nextButton.grid(row=0, column=2)
        if(i + 1 == len(inventory)):
            nextButton.config(state=tk.DISABLED)

        navigationFrame.grid_columnconfigure(1, weight=1)
        navigationFrame.grid(row=999, column=0, columnspan=col, sticky=tk.E + tk.W)
        print(col // 2)
        print(col)

    def readyForNextPage(self, frame, imageHeight, label, button):
        frame.update()
        frameHeight = frame.winfo_height()
        labelHeight = label.winfo_height()
        buttonHeight = button.winfo_height()
        itemHeight = imageHeight + labelHeight + buttonHeight
        # Create a next page if the current height plus the height of one more
        # item is more than the window height
        return frameHeight + itemHeight > UI.windowHeight(self.root)

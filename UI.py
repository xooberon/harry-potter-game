import tkinter as tk
from PIL import Image, ImageTk
from CharacterInfo import CharacterInfo


def bannerWidth(root):
    return (int)(windowWidth(root) / 5)


def bannerHeight(root):
    return windowHeight(root)


def bodyWidth(root):
    return (int)(windowWidth(root) * 3 / 5)


def bodyHeight(root):
    return windowHeight(root)


def windowWidth(root):
    return int(root.winfo_screenheight() - 80)


def windowHeight(root):
    return int(root.winfo_screenheight() - 80)


def createWhiteSpace(frame):
    whiteSpace = tk.Label(frame, text="", background="white")
    whiteSpace.pack()


def createMessage(frame, text):
    nameMessage = tk.Label(frame, text=text, background="white")
    nameMessage.pack()


def createMenu(frame, options, callback):
    defaultOption = tk.StringVar(frame)
    defaultOption.set("Please choose a value")
    menu = tk.OptionMenu(frame, defaultOption, *options, command=callback)
    menu.config(background="white")
    menu["menu"].config(background="white")
    menu.pack()


def createEntryField(frame, buttonText, callback):
    entryFieldFrame = tk.Frame(frame, background="white")
    entryFieldFrame.pack()

    defaultText = tk.StringVar(frame)
    entry = tk.Entry(entryFieldFrame, textvariable=defaultText)
    entry.pack(side=tk.LEFT)
    button = tk.Button(entryFieldFrame, text=buttonText, command=callback, background="white")
    button.pack(side=tk.LEFT)

    return entry


def createNextButton(frame, callback):
    nextButton = tk.Button(frame, text="Next page", command=callback, background="white")
    createWhiteSpace(frame)
    nextButton.pack()


def createBackButton(frame, text, callback):
    backButton = tk.Button(frame, text=text, command=callback, background="white")
    return backButton


def createWandMenus(self):
    wandFrame = tk.Frame(self, background="white")
    wandFrame.pack()

    def wandCoreWasSet(wandCore):
        self.characterInfo.setWandCore(wandCore)

    def wandWoodWasSet(wandWood):
        self.characterInfo.setWandWood(wandWood)

    wandCoreValues = self.characterInfo.wandCoreValues
    wandCores = self.createMenu(wandFrame, wandCoreValues, wandCoreWasSet)
    wandCores.pack(side=tk.LEFT)

    wandWoodValues = self.characterInfo.wandWoodValues
    wandWoods = self.createMenu(wandFrame, wandWoodValues, wandWoodWasSet)
    wandWoods.pack(side=tk.LEFT)


def createHouseMenu(self):
    def houseWasSet(house):
        self.characterInfo.setHouse(house)
    houses = self.createMenu(self, self.characterInfo.houseValues, houseWasSet)
    houses.pack()


def createShopItem(self, text, image_width, image_height):
    shopItemFrame = tk.Frame(self, background="white")
    shopItemImage = getShopItemImage(text, image_width, image_height)
    shopItem = tk.Label(shopItemFrame, image=shopItemImage)
    shopItem.image = shopItemImage
    shopItem.pack()
    createMessage(shopItemFrame, text)
    return shopItemFrame

def getShopItemImage(text, width, height):
    shopItemFile = "images/default-icon.png"
    shopItemFullSize = Image.open(shopItemFile)
    shopItemResized = shopItemFullSize.resize((width, height), Image.ANTIALIAS)
    shopItemImage = ImageTk.PhotoImage(shopItemResized)
    return shopItemImage

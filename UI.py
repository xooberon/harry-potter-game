import tkinter as tk
from tkinter.font import Font
from PIL import Image, ImageTk
# from CharacterInfo import CharacterInfo


def font():
    return Font(family="Helvetica", size=10)


def smallFont():
    return Font(family="Helvetica", size=5)


def bannerWidth(root):
    return (int)(windowWidth(root) / 5)


def bannerHeight(root):
    return windowHeight(root)


def bodyWidth(root):
    return (int)(windowWidth(root) * 3 / 5)


def bodyHeight(root):
    return windowHeight(root)


def windowWidth(root):
    return int(root.winfo_screenheight() - 65)


def windowHeight(root):
    return int(root.winfo_screenheight() - 65)


def createWhiteSpace(frame):
    whiteSpace = tk.Label(frame, text="", font=smallFont())
    whiteSpace.config(background="white")
    whiteSpace.pack()


def createMessage(frame, text):
    message = tk.Label(frame, text=text, font=font(), background="white")
    message.pack()


def createWrappedMessage(frame, text, wrapLength, heightInLines):
    text = truncateText(text, wrapLength, heightInLines, font())
    message = tk.Label(frame, text=text, font=font(), background="white")
    message.config(wraplength=wrapLength)
    message.config(height=heightInLines)
    message.config(anchor=tk.N)
    return message


def truncateText(text, width, heightInLines, font):
    numberOfLines = font.measure(text) / width
    while(numberOfLines > heightInLines):
        text = text.rsplit(' ', 1)[0]
        text += "..."
        numberOfLines = font.measure(text) / width
    return text


def createMenu(frame, options, callback):
    defaultOption = tk.StringVar(frame)
    defaultOption.set("Please choose a value")
    menu = tk.OptionMenu(frame, defaultOption, *options, font=font())
    menu.config(command=callback)
    menu.config(background="white")
    menu["menu"].config(background="white")
    menu.pack()


def createEntryField(frame, buttonText, callback):
    entryFieldFrame = tk.Frame(frame, background="white")
    entryFieldFrame.pack()

    defaultText = tk.StringVar(frame)
    entry = tk.Entry(entryFieldFrame, textvariable=defaultText, font=font())
    entry.pack(side=tk.LEFT)
    button = tk.Button(entryFieldFrame, font=font(), background="white")
    button.config(text=buttonText)
    button.config(command=callback)
    button.pack(side=tk.LEFT)
    print(entry.cget('font'))

    return entry


def createMultiLineEntryField(frame, buttonText, width, height, callback):
    entryFieldFrame = tk.Frame(frame, background="blue")
    entryFieldFrame.config(width=width)
    entryFieldFrame.config(height=height)
    entryFieldFrame.pack()
    entryFieldFrame.pack_propagate(False)

    entry = tk.Text(entryFieldFrame, width=width, height=height, font=font())
    entry.pack(fill=tk.BOTH, expand=1)
    button = tk.Button(frame, font=font(), background="white")
    button.config(text=buttonText)
    button.config(command=callback)
    button.pack(side=tk.LEFT)

    return entry


def createNextButton(frame, callback):
    nextButton = tk.Button(frame, font=font(), background="white")
    nextButton.config(text="Next page")
    nextButton.config(command=callback)
    nextButton.pack(side=tk.RIGHT)


def createButton(frame, text, callback):
    backButton = tk.Button(frame, text=text, font=font(), background="white")
    backButton.config(text=text)
    backButton.config(command=callback)
    return backButton


def createShopItemImage(frame, text, image_width, image_height):
    itemImage = getShopItemImage(text, image_width, image_height)
    itemImageLabel = tk.Label(frame, image=itemImage)
    itemImageLabel.image = itemImage
    return itemImageLabel


def createShopItemLabel(frame, text, text_width, heightInLines):
    itemLabel = createWrappedMessage(frame, text, text_width, heightInLines)
    return itemLabel


def createBuyButton(frame):
    buyButton = tk.Button(frame, text="Buy 1", font=font(), background="white")
    buyButton.config(text="Buy 1")
    buyButton.pack(side=tk.LEFT)


def createDetailsButton(frame):
    detailsButton = tk.Button(frame, text="Details", font=font())
    detailsButton.config(background="white")
    detailsButton.config(text="Details")
    detailsButton.pack(side=tk.RIGHT)


def emptyRow(frame):
    emptyFrame = tk.Frame(frame, background="white")
    createWhiteSpace(emptyFrame)
    return emptyFrame


def getShopItemImage(text, width, height):
    shopItemFile = "images/default-icon.png"
    shopItemFullSize = Image.open(shopItemFile)
    shopItemResized = shopItemFullSize.resize((width, height), Image.ANTIALIAS)
    shopItemImage = ImageTk.PhotoImage(shopItemResized)
    return shopItemImage

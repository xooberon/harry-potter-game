'''
Created on 4/02/2017

@author: Miranda
'''

import tkinter as tk
from PIL import Image, ImageTk
from CharacterInfo import CharacterInfo
from IntroUIFirstPage import IntroUIFirstPage
from IntroUISecondPage import IntroUISecondPage
import UI


class IntroUI(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="white")

        self.parent = parent
        self.bannerWidth = UI.bannerWidth(parent)
        self.bannerHeight = UI.bannerHeight(parent)
        self.characterInfo = CharacterInfo()
        self.currentPage = 0
        self.parent.title("Character Sheet")
        self.pack(fill=tk.BOTH, expand=1)

    def displayNextPage(self):
        # This is used to maintain the correct width
        width = UI.windowWidth(self.parent)
        topBannerImage = ImageTk.PhotoImage(Image.new("RGB", (width, 1), "white"))
        topBanner = tk.Label(self, image=topBannerImage)
        topBanner.image = topBannerImage
        topBanner.grid(row=0, column=0, columnspan=3)

        leftBannerImage = self.getLeftImage()
        leftBanner = tk.Label(self, image=leftBannerImage)
        leftBanner.image = leftBannerImage
        leftBanner.grid(row=1, column=0, sticky=tk.NW)

        if(self.currentPage == 0):
            mainDisplay = self.createIntroFirstPage()
        elif(self.currentPage == 1):
            mainDisplay = self.createIntroSecondPage()
        else:
            self.createIntroThirdPage()
        mainDisplay.grid(row=1, column=1, sticky=tk.N)

        rightBannerImage = self.getRightImage()
        rightBanner = tk.Label(self, image=rightBannerImage)
        rightBanner.image = rightBannerImage
        rightBanner.grid(row=1, column=2, sticky=tk.NE)

        self.currentPage = self.currentPage + 1

    def createIntroFirstPage(self):
        firstPage = IntroUIFirstPage(self, self.parent)
        firstPage.displayUI()
        return firstPage

    def createIntroSecondPage(self):
        secondPage = IntroUISecondPage(self, self.parent)
        secondPage.displayUI()
        return secondPage

    def createIntroThirdPage(self):
        message = ("Your house is like your family at Hogwarts."
                   "What house are you in?")
        self.createMessage(message)
        self.createHouseMenu()

    def getLeftImage(self):
        leftBannerFile = "images/left-banner-" + str(self.currentPage) + ".png"
        leftFullSize = Image.open(leftBannerFile)
        leftResized = leftFullSize.resize((self.bannerWidth, self.bannerHeight), Image.ANTIALIAS)
        leftBannerImage = ImageTk.PhotoImage(leftResized)
        return leftBannerImage

    def getRightImage(self):
        rightFile = "images/right-banner-" + str(self.currentPage) + ".png"
        rightFullSize = Image.open(rightFile)
        rightResized = rightFullSize.resize((self.bannerWidth, self.bannerHeight), Image.ANTIALIAS)
        rightBannerImage = ImageTk.PhotoImage(rightResized)
        return rightBannerImage

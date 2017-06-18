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
        self.width = UI.windowWidth(parent)
        self.height = UI.windowHeight(parent)
        self.characterInfo = CharacterInfo()
        self.currentPage = 0
        self.parent.title("Character Sheet")
        self.pack(fill=tk.BOTH, expand=1)

    def displayNextPage(self):
        topHeight = int(self.height / 5)
        topBannerImage = self.getTopImage(topHeight)
        topBanner = tk.Label(self, image=topBannerImage)
        topBanner.image = topBannerImage
        topBanner.grid(row=0, column=0, columnspan=3)

        leftBannerImage = self.getLeftImage(topHeight)
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

        rightBannerImage = self.getRightImage(topHeight)
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

    def getTopImage(self, height):
        topBannerFile = "images/top-banner-" + str(self.currentPage) + ".png"
        topFullSize = Image.open(topBannerFile)
        width = self.width
        topResized = topFullSize.resize((width, height), Image.ANTIALIAS)
        topBannerImage = ImageTk.PhotoImage(topResized)
        return topBannerImage

    def getLeftImage(self, topHeight):
        leftBannerFile = "images/left-banner-" + str(self.currentPage) + ".png"
        leftFullSize = Image.open(leftBannerFile)
        width = int(self.width / 5)
        height = self.height - topHeight
        leftResized = leftFullSize.resize((width, height), Image.ANTIALIAS)
        leftBannerImage = ImageTk.PhotoImage(leftResized)
        return leftBannerImage

    def getRightImage(self, topHeight):
        rightFile = "images/right-banner-" + str(self.currentPage) + ".png"
        rightFullSize = Image.open(rightFile)
        width = int(self.width / 5)
        height = self.height - topHeight
        rightResized = rightFullSize.resize((width, height), Image.ANTIALIAS)
        rightBannerImage = ImageTk.PhotoImage(rightResized)
        return rightBannerImage

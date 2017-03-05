'''
Created on 4/02/2017

@author: Miranda
'''

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import UI
from CharacterInfo import CharacterInfo
from IntroUIFirstPage import IntroUIFirstPage
from IntroUISecondPage import IntroUISecondPage

class IntroUI(tk.Frame):
  
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        self.characterInfo = CharacterInfo()
        self.currentPage = 0
        self.parent.title("Character Sheet")
        self.pack(fill=tk.BOTH, expand=1)

    def displayNextPage(self):
        topBannerImageFile = "images/top-banner-" + str(self.currentPage) + ".png"
        topBannerImage = ImageTk.PhotoImage(Image.open(topBannerImageFile))
        topBanner = tk.Label(self, image=topBannerImage)
        topBanner.image = topBannerImage
        topBanner.grid(row=0, column=0, columnspan=3)

        leftBannerImageFile = "images/left-banner-" + str(self.currentPage) + ".png"
        leftBannerImage = ImageTk.PhotoImage(Image.open(leftBannerImageFile))
        leftBanner = tk.Label(self, image=leftBannerImage)
        leftBanner.image = leftBannerImage
        leftBanner.grid(row=1, column=0, sticky=tk.NW)

        if( self.currentPage == 0 ):
            mainDisplay = self.createIntroFirstPage()
        elif( self.currentPage == 1 ):
            mainDisplay = self.createIntroSecondPage()
        else:
            self.createIntroThirdPage()
        mainDisplay.grid(row=1, column=1, sticky=tk.N)

        rightBannerImageFile = "images/right-banner-" + str(self.currentPage) + ".png"
        rightBannerImage = ImageTk.PhotoImage(Image.open(rightBannerImageFile))
        rightBanner = tk.Label(self, image=rightBannerImage)
        rightBanner.image = rightBannerImage
        rightBanner.grid(row=1, column=2, sticky=tk.NE)

        self.currentPage = self.currentPage+1
        
    def createIntroFirstPage(self):
        firstPage = IntroUIFirstPage(self, self.parent)
        firstPage.displayUI()
        return firstPage

    def createIntroSecondPage(self):
        secondPage = IntroUISecondPage(self, self.parent)
        secondPage.displayUI()
        return secondPage

    def createIntroThirdPage(self):
        self.createMessage("Your house is like your family at Hogwarts. What house are you in?")
        self.createHouseMenu()

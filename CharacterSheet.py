'''
Created on 4/02/2017

@author: Miranda
'''

import tkinter
from IntroUI import IntroUI
import UI

print("Hello world")
root = tkinter.Tk()
width = UI.windowWidth(root)
height = UI.windowHeight(root)
root.geometry(str(int(width)) + "x" + str(height) + "+0+0")
root.resizable(width=False, height=False)
root.IntroUI = IntroUI(root)
root.IntroUI.displayNextPage()
root.mainloop()

'''
Created on 4/02/2017

@author: Miranda
'''

import tkinter
from IntroUI import IntroUI

root = tkinter.Tk()
root.geometry("755x792+0+0")
root.resizable(width=False, height=False)
root.IntroUI = IntroUI(root)
root.IntroUI.displayNextPage()
root.mainloop()

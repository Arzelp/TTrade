#!/usr/bin/env python3

from __future__ import print_function
import sys
import os
from macros import *
from loop import mainloop

## response = requests.get("https://bittrex.com/api/v1.1/public/getmarkets")
## data = json.loads(response.text)

def printnb():
    print("40")

## def initscr():
##     window = Tk()
##     width = 1080
##     height = 800
##     bgCanvas = Canvas(window, width=width, height=height)
##     bgImage = ImageTk.PhotoImage(file="bite.jpg")
##     bgCanvas.create_image(0, 0, image=bgImage, anchor=NW)
##     bgCanvas.pack()
##     return (window)

## def main():
##     try:
##         window = initscr()
##     except:
##         print("Error while initializing")
##     try:
##         mainloop(window)
##     except:
##         print("Error, will exit.")

def main():
    try:
        mainloop()
    except:
        print("Error, will exit.")

if (__name__ == '__main__'):
    try:
        main()
    except:
        print("Error")
        exit (84)
    exit (0)

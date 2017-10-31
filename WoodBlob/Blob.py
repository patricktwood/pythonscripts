#################################################################
# A script to creates and moves random Blobs in a tKinter frame
# Heavliy modified from: http://effbot.org/tkinterbook/canvas.htm
# Author: Jim Graham
# Date: 2/27/2013
#
# Modified by: Patrick T Wood
# Modified Date: 4/11/2017
#################################################################
try:
    from tkinter import *
except:
    from Tkinter import *
from BlobClass import BlobClass
import time # bring in the time library so we can "wait" between drawing
import random # random needed for random coordinates and colors

words1 = 'The Blob Simulation v1'
words2 = '''Created by: Jim Graham
Modified by: Patrick T Wood'''
words3 = 'Created: April 7th 2017'
words4 = 'Humboldt State University'
words5 = 'Go Jacks!'
words6 = 'PlaceHolder'

#################################################################
    # FUNCTIONS
#################################################################
# This is the function that makes the add button work
def AddBlob():
    # a and b are coordinates of the blob, c is the and d are the speed and direction
    a = random.randint(0,1200)
    b = random.randint(0,600)
    c = random.randint(-10,10)
    d = random.randint(-10,10)
    # This part creates the random color of the blob when it is created
    NewColorList = ["blue","green", "gold", "red", "purple", "white", "teal", "pink"]
    ColorNumber = random.randint(0, 7)
    NewColor = ColorList[ColorNumber]
            
    NewBlob=BlobClass(canvas, (a, b), NewColor, c, d)

    TheItems.append(NewBlob)

# This is the function that makes the Freeze button work
def FreezeBlobs():
    if len(TheItems) > 0:
        canvas.delete(TheItems.pop())

# This is the function that makes the clock work
def tick():
    s = time.strftime('%H:%M:%S')
    if s != clock["text"]:
        clock["text"] = s
        #time1 = time2
        #clock.config(text=time2)
    clock.after(200,tick)

# This is the function that makes the About button work
def change_text():
    canvas.itemconfig(Words, text=words2)
    global words1, words2, words3, words4, words5
    
    words6 = words2
    words2 = words3
    words3 = words4
    words4 = words5
    words5 = words1
    words1 = words6


#################################################################
        # Main Script
#################################################################
# Setup the GUI with a modeless window labeled "Blobs"
MasterWindow = Tk()
MasterWindow.title("The Blob Simulation v1")
MasterWindow.resizable(0, 0)

# Create the Canvas widget for the blobs to move in
canvas = Canvas(MasterWindow, width=1200, height=600, bd=0, highlightthickness=0, bg = "black")
canvas.pack()

clock = Label(MasterWindow, font=('times', 20, 'bold'), bg= 'green')
clock.pack(fill=BOTH, expand=1)

# This is the words that are displayed behind the blobs
Words = canvas.create_text((600,300), text=words1, fill='green', font=('times', 18, 'bold'))

# This is calls the clock tick function
tick()

# Buttons!
Button(MasterWindow, text="Quit Simulation", command=MasterWindow.destroy).pack(side="bottom")
Button(MasterWindow, text="Add a Blob", command=AddBlob).pack(side="left")
Button(MasterWindow, text="Freeze a Blob", command=FreezeBlobs).pack(side="left")
Button(MasterWindow, text="About Blobs", command=change_text).pack(side="right")

# This creates the random color for the initial blob
ColorList = ["blue","green", "gold", "red", "purple", "white", "teal", "pink"]
startingcolor = random.randint(0, 7)
StartColor = ColorList[startingcolor]

# Create blobs objects
TheItems = [
        BlobClass(canvas, (175, 80), StartColor, -6, -.20) 
]

MasterWindow.update() # fix geometry

# Move the blobs forever
try:
    while True:
        for TheItem in TheItems:
            TheItem.move()
        MasterWindow.update_idletasks() # redraw
        MasterWindow.update() # process events
        time.sleep(.01)

except TclError:
    pass # to avoid errors when the window is closed
    print("Blob Ended!!!!!")

#################################################################
# A blob that can be moved in a canvas
# Heavliy modified from: http://effbot.org/tkinterbook/canvas.htm
# Author: Jim Graham
# Date: 2/27/2013
# 
# Modified by: Patrick T Wood
# Modified Date: 4/11/2017
#################################################################

class BlobClass:
    # Initialize the new object
    # Inputs:
    #  canvas - the canvas widget that the blob will appear in
    #  Position - a list of the x and y pixel coordinate for the starting location of the blob
    #  FillColor - the color of the Blob
    #  XMovementAmount - The Amount to move the Blob for each time Move() is called
    def __init__(self, TheCanvas, StartCoordinate, FillColor, XMovementAmount, YMovementAmount):

        self.TheCanvas = TheCanvas # save the canvas the blob is in

        # save the amount to move for later
        self.XMovementAmount = XMovementAmount
        self.YMovementAmount = YMovementAmount
        
        # create the oval at an x and y location based on movement
        self.id = self.TheCanvas.create_rectangle(StartCoordinate[0], StartCoordinate[1],
                                                     StartCoordinate[0]+60, StartCoordinate[1]+60, fill=FillColor)


    # move the blob based on the XMovementAmount
    def move(self):
        # get the existing coordinate of the blob
        Bounds = self.TheCanvas.coords(self.id)

        # if the blob has moved off the frame, reverse the direction of movement
        
        if Bounds[1] >= self.TheCanvas.winfo_height():
            self.YMovementAmount = -self.YMovementAmount
        if Bounds[3] < 0:
            self.YMovementAmount = -self.YMovementAmount
       
        if Bounds[2] >= self.TheCanvas.winfo_width():
                self.XMovementAmount = -self.XMovementAmount
        if Bounds[0] < 0:
                self.XMovementAmount = -self.XMovementAmount

        self.TheCanvas.move(self.id, self.XMovementAmount, self.YMovementAmount)


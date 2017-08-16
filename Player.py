from Item import *

'''This class defines how out player will behave. It "inherits" from its parent class Item so it can do 
everything Item can do but we can also add more behavior without having to duplicate code. Pretty neat!'''
class Player(Item):
    
    #Here we set up the player
    def __init__(self, animage, xlocation, ylocation):
        #We call on Player's parent constuctor to set up the basic image, location, and size information
        Item.__init__(self, animage, xlocation, ylocation, animage.width, animage.height)
        
    #This is where we tell the player how to move left using its location
    def moveLeft(self):

        if(self.xlocation - 10 > 0):
            #PUT SOME CODE HERE
            pass
    
    #This is where we tell the player how to move right using its location
    def moveRight(self):

        if(self.xlocation + 10 < width):
            #PUT SOME CODE HERE
            pass
        
        
        
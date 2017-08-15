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
        #print("Move Left");
        if(self.xlocation - 10 > 0):
            #/**********************************/
            
            #Make the player move to the left
            
            #/**********************************/
            #PUT SOME CODE HERE
            self.xlocation -= 10
    
    #This is where we tell the player how to move right using its location
    def moveRight(self):
        #print("Move Right");
        if(self.xlocation + 10 < width):
        
            #/**********************************/
        
            #make the player move to the right
        
            #/**********************************/
            #PUT SOME CODE HERE
            self.xlocation += 10
        
        
        
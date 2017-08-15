from Item import *

'''This class will define how our fruits behave. It "inherits" from its parent class Item so it can do 
everything Item can do but we can also add more behavior without having to duplicate code. Pretty neat!'''
class Fruit(Item):
    
    #Here we set up the Fruit
    def __init__(self, animage, xlocation, aspeed, value):
        #We call on Fruit's parent constuctor to set up the basic image, location, and size information
        #We set ylocation to 0 because we want our fruits to first appear at the top of the screen
        Item.__init__(self, animage, xlocation, 0, animage.width, animage.height)
        
        #Here we add more information to fruit about how fast it's going to move
        self.speed = aspeed
        #Here we set how many points the fruit is worth
        self.value = value
    
    #This is where we define how the fruit will move, we move its y location by adding the speed to 
    #make it look like it's falling
    def move(self):
        self.ylocation = self.ylocation + self.speed
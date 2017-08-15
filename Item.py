'''This is the "parent" class for both Fruit and Player. It defines important functionality that they both share
such as location, size, image and collision detection functionality'''

class Item:
    
    #Here we set up the Item
    def __init__(self, animage, xlocation, ylocation, mywidth, myheight):
        self.myimage = animage
        self.xlocation = xlocation
        self.ylocation = ylocation
        self.mywidth = mywidth
        self.myheight = myheight
       
    #This function draws the Item with and image at the x,y location 
    def draw(self):
        image(self.myimage, self.xlocation, self.ylocation)
        
    #This is where we can check if two items have collided or intersected, this will be important for
    #Checking if our player has "caught" a fruit
    #This function returns true if the items have intersected and False if not
    def Intersects(self, anitem):
        itemwidth = anitem.mywidth
        itemheight = anitem.myheight
        itemxloc = anitem.xlocation
        itemyloc = anitem.ylocation
    
        if(itemxloc < self.xlocation + self.mywidth and 
        itemxloc + itemwidth > self.xlocation and 
        itemyloc < self.ylocation + self.myheight and 
        itemheight + itemyloc > self.ylocation):
            return True
    
        return False
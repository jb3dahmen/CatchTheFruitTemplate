add_library('sound')

from Fruit import *
from Player import *

'''The GameManager class controls and stores important aspects of the game. It controls how the player and fruits move
as well as keeping track of time and score'''
class GameManager:
    
    #Here we set up the GameManager
    def __init__(self, bgimage, framerate, playerimage, timer, fruitimage, itemCatchMusicPlayer, backgroundMusicPlayer):
        
        #The game background image
        self.backgroundimage = bgimage
        #The player image
        self.playerimage = playerimage
        #The game framerate in frames/second
        self.framerate = framerate
        #The game timer that will help control how long the game lasts
        self.timer = timer
        
        #This boolean will help us check if the game is done (the timer ran out)
        self.done = False
        #We can load custom fonts to display the fruit points and total score
        self.scorefont = loadFont("Sansation-Bold-35.vlw");
        self.pointsfont = loadFont("Sansation-Bold-35.vlw");
        
        #The total score so far
        self.score = 0
        #How "fast" the fruits will fall
        self.fruitspeed = 7
        #The time that will be used to spawn fruits TODO: rename
        self.time = 0
        #This is a list that will store the fruits TODO: rename
        self.items = []
        #How many points the fruits are worth
        self.pointsValue = 0
        #Where the fruit points will appear once a fruit is caught TODO: maybe this should be an attribute of fruit?
        self.pointsx = 0
        self.pointsy = 0
        #Checks whether the fruit points should be displayed
        self.pointsOn = False
        #How many frames the fruit points should be displayed for
        self.pointsFrameCount = 0
        
        #How long the game will last in seconds
        self.gameDurationSeconds = 30
        
        #The fruit image
        self.fruitimage = fruitimage
        
        #The background and caught fruit sounds
        self.itemCatchMusicPlayer = itemCatchMusicPlayer
        self.backgroundMusicPlayer = backgroundMusicPlayer
        
        #Set up the game's player
        self.player = Player(self.playerimage, width/2, height - 100)
        
        
        
        
    #This calls all the methods that will be needed to make the game run
    def playGame(self):
        
        #Increase the difficulty (speed of fruit) over time
        self.difficultyChange()
        #Spawn the fruits
        self.spawn()
        #Move the fruits
        self.moveFruit()
        #Draw the player, fruits, and points
        self.drawWorld()
        #Check if the game has ended
        self.checkEnd()
        #Check if the player has caught a fruit
        self.checkCollision()
        #Show the score and current fruit speed
        self.displayScore()
        self.displaySpeed()
        
        #Every time this is used add 1 second to the game time
        self.time = self.time + 1

    #Here we draw all the fruits and player on our game screen
    def drawWorld(self):
       
        #draw all the fruits that have been spawned by looping through the items list
        for i in range(len(self.items)):
            aFruit = self.items[i]
            aFruit.draw()
            
        #draw the player on the screen
        self.player.draw()
      
    #Here we create fruits and add them to the items list 
    def spawn(self):
        #Control how often the fruits will spawn
        if(self.time == self.framerate / 2):
            
            #reset the fruit spawn time
            self.time = 0
            #Create a fruit with a random x location
            aFruit = Fruit(self.fruitimage, int(random(30,470)), self.fruitspeed, 3)
            
            #CHALLENGE1: Add a new type of fruit
            
            #CHALLENGE2: Add a powerup
            
            #Add the fruit to the list
            self.items.append(aFruit)
        
    #Here we move the fruits by using their move() method    
    def moveFruit(self):
        #/**********************************/
  
        #Finish this for loop to make the fruits fall 
        
        #/**********************************/
        
        
        for i in range(len(self.items)):
            #inside the loop
            aFruit = self.items[i]
            aFruit.move()
            
    #Here we check if the game has ended by checking the time
    #How could we change this to end the game by reaching a certain score?
    def checkEnd(self):
        #If the elapsed time has reached the game duration time 
        if(self.timer.currentTime() == self.gameDurationSeconds):
            self.done = True
            self.timer.pause()
            
    #Here we increase the speed of the fruits falling every 5 seconds that pass
    #What other ways could difficulty increase?    
    def difficultyChange(self):
        #Increase the difficulty every 5 seconds
        if(self.timer.currentTime() % 5 == 0 and self.timer.currentTime() != 0 and frameCount % self.framerate == 0 and frameCount != 0):
            self.fruitspeed = self.fruitspeed + 1
    #Here we check if the player has collide with or caught a fruit  
    def checkCollision(self):
        
        #store items you want removed in this list, never a good idea to modify a list you are iterating over in python
        itemsToRemove = []
        
        #loop through the fruits
        #We need to check every fruit to see if it is touching the player
        for i in range(len(self.items)):
        
            aFruit = self.items[i]
            
            #If the player caught a fruit
            #Display the fruit points
            if(self.player.Intersects(aFruit)):
            
                self.score = self.score + aFruit.value
                self.pointsValue = aFruit.value
                self.pointsx = aFruit.xlocation
                self.pointsy = aFruit.ylocation
                
                self.pointsOn = True
                
                #remove the fruit from the items list
                itemsToRemove.append(aFruit)
                
                #print("CAUGHT!")
                self.itemCatchMusicPlayer.play()
            
            self.displayPoints(self.pointsValue, self.pointsx, self.pointsy)
        
        #remove caught fruits from the list  
        #TODO: maybe remove fruits that move off screen?
        for i in range(len(itemsToRemove)):
            itemToRemove = itemsToRemove[i]
            self.items.remove(itemToRemove)
            
    #Here we show the fruit points
    def displayPoints(self, value, x, y):
       
        if(self.pointsOn and self.pointsFrameCount < 90):
            textFont(self.pointsfont, 30)
            fill(255)
            text("+" + str(value), x, y)
            self.pointsFrameCount = self.pointsFrameCount + 1
        else:
            self.pointsOn = False
            self.pointsFrameCount = 0
        
    #Here we show the fruit speed
    def displaySpeed(self):
        fill(255)
        textFont(self.scorefont, 20)
        text("Speed: " + str(self.fruitspeed), 10,31)
    #Here we show the total score
    def displayScore(self):
        fill(255)
        textFont(self.scorefont, 20)
        text("Score: " + str(self.score), 10,15)
     
    #Here we show the game over message   
    def displayGameOverMessage(self):
        textFont(self.scorefont, 40)
        text("Good Job!",10,40)
        textFont(self.scorefont,20)
        text("SCORE: " + str(self.score),10,70)
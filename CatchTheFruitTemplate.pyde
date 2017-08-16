#OpenProcessing Tweak of *@*http://www.openprocessing.org/sketch/112419*@*
#!do not delete the line above, required for linking your tweak if you upload again

#Use processing libraries
add_library('sound')

#Use the classes we defined in Fruit.py, Item.py etc.
from GameManager import *
from Player import *
from Timer import *

'''The setup() function is run once, when the program starts. 
It's used to define initial enviroment properties such as screen size and to load media such as images and fonts as the program starts. 
There can only be one setup() function for each program and it shouldn't be called again after its initial execution.'''
def setup():
    
    #This sets the size of our game screen or "canvas"
    #think of it like a coordinate grid to place images with x,y locations
    size(640,380)
    
    #These are image objects that will store what our player, background, and fruit will look like
    #Try changing the filenames to get different looks
    #Edit the filenames here to change your player, background and fruit images
    playerimage = loadImage("playerimages/Luma.png")
    backgroundimage = loadImage("backgroundimages/spacebg.png")
    fruitimage = loadImage("fruitimages/starfruit.png")
    
    #Resize the fruit and player images to fit on the drawing canvas
    #PUT SOME CODE HERE
    #PUT SOME CODE HERE

    #This object is the music player for the background game music
    #Try changing the filenames to get different sounds
    #Edit the filename here to change your background music
    backgroundMusicPlayer = SoundFile(this,"backgroundmusic/Hyperbola.mp3")
    
    #This object is the music player for the sound effect when the player catches a fruit
    #Try changing the filenames to get different sounds
    #Edit the filename here to change your sound effect noise
    itemCatchMusicPlayer = SoundFile(this, "soundeffects/boip.mp3")
   
    #This will be how many frames per second our game will run at
    #Determines how many times per second the draw() function is called
    framerate = 30

    #This object is the timer that will control how long the game lasts
    #The arguments are the x,y coordinates where the timer text will display
    gametimer = Timer(width - 200,60)
    
    #This object will control important aspects of our game
    #It is set to global to make it accessible everywhere in our code
    global gameManager
   
    #Here we construct gameManager object
    #We tell it what background we want as well as framerate, player image, timer, fruit image, and music
    gameManager = GameManager(backgroundimage, framerate, playerimage, gametimer, fruitimage, itemCatchMusicPlayer, backgroundMusicPlayer)
    
    #Here we tell our timer inside the gameManager to start, to start the game
    gameManager.timer.start()
    
    #Here we tell the background music player inside gameManager to start playing our game music!
    gameManager.backgroundMusicPlayer.play()
  

#This function is used to check if we have pressed a key using conditionals
def keyPressed():
    '''if (key == CODED):
       
       #If the left arrow key is pressed move the player left
       if(keyCode == ):
         #ADD SOME CODE HERE
       
       #If the right arrow key is pressed move the player right
       if(keyCode == ):
         #ADD SOME CODE HERE'''

'''Called directly after setup(), the draw() function continuously 
executes the lines of code contained inside 
its block until the program is stopped or noLoop() is called. 
draw() is called automatically and should never be called explicitly. 
All Processing programs update the screen at the end of draw(), 
never earlier. The number of times draw() executes in each second 
may be controlled with the frameRate() function.'''
def draw():
    
    #Using the information stored inside gameManager
    #We draw the background image and set the frame rate
    background(gameManager.backgroundimage)
    frameRate(gameManager.framerate)
    
    #Here we set how long the game will last in seconds
    #How can we change the variable gameDurationSeconds to make the 
    #game laster longer?
    gameDurationSeconds = 10
    #Here we tell our timer to display the time as text
    gameManager.timer.DisplayTime(gameDurationSeconds)
    
    #This conditional is used to check if we are still playing the game or if time has run out
    #If the game is over then we display the game over message!
    #What could we code to make the game restart?
    if(not gameManager.done):
        gameManager.playGame()
    else:
        gameManager.displayGameOverMessage()

    
       
    
  
    

    
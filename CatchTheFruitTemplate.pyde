#OpenProcessing Tweak of *@*http://www.openprocessing.org/sketch/112419*@*
#!do not delete the line above, required for linking your tweak if you upload again

#Use processing libraries
add_library('sound')

#Use the classes we defined in Fruit.py, Item.py etc.
from GameManager import *
from Player import *
from Timer import *

#This function TODO:
def setup():
    
    #This sets the size of our game screen or "canvas"
    #think of it like a coordinate grid to place images with x,y locations
    size(640,380)
    
    #These are image objects that will store what our player, background, and fruit will look like
    #Try changing the filenames to get different looks
    playerimage = loadImage("playerimages/Luma.png")
    backgroundimage = loadImage("backgroundimages/spacebg.png")
    fruitimage = loadImage("fruitimages/starfruit.png")
    
    #Here we can change the size (width, height) of our images in pixels to make our player and fruits bigger or smaller
    fruitimage.resize(50,50)
    playerimage.resize(100,100)
    

    #This object is the music player for the background game music
    #Try changing the filenames to get different sounds
    backgroundMusicPlayer = SoundFile(this,"backgroundmusic/Hyperbola.mp3")
    #This object is the music player for the sound effect when the player catches a fruit
    #Try changing the filenames to get different sounds
    itemCatchMusicPlayer = SoundFile(this, "soundeffects/boip.mp3")
   
    #This will be how many frames per second our game will run at
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
    if (key == CODED):
       
       #/**********************************/
       
       #finish this conditional statement to make the player move left and right
       
       #/**********************************/
       
       #If the left arrow key is pressed move the player left
       if(keyCode == LEFT):
         gameManager.player.moveLeft()
       
       #If the right arrow key is pressed move the player right
       if(keyCode == RIGHT):
         gameManager.player.moveRight()

#This function TODO:
def draw():
    
    #Using the information stored inside gameManager
    #We draw the background image and set the frame rate
    background(gameManager.backgroundimage)
    frameRate(gameManager.framerate)
    
    #Here we set how long the game will last in seconds
    gameDurationSeconds = 30
    #Here we tell our timer to display the time as text
    gameManager.timer.DisplayTime(gameDurationSeconds)
    
    #This conditional is used to check if we are still playing the game or if time has run out
    #If the game is over then we display the game over message!
    #What could we code to make the game restart?
    if(not gameManager.done):
        gameManager.playGame()
    else:
        gameManager.displayGameOverMessage()

    
       
    
  
    

    
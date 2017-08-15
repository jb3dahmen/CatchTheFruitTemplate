#Copyright 2009, Leutenegger
#Credit to this Timer Class: From http://www.cs.du.edu/~leut/1671/09_Fall/ProcessingNotes7.pdf
#rewritten using Python syntax

#This class is used to define the game timer
#It will control how long the game lasts
class Timer:
    def __init__(self, inX, inY):
        self.x = inX
        self.y = inY
        self.running = False
        self.timeSoFar = 0
        self.startTime = 0
        
    def currentTime(self):
        if(self.running):
            return int((millis() - self.startTime) / 1000.0)
        else:
            return int(self.timeSoFar / 1000.0)
        
    def start(self):
        self.running = True
        self.startTime = millis()
        
    def restart(self):
        self.start()
        
    def pause(self):
        if(self.running):
            self.timeSoFar = millis() - self.startTime
            self.running = False
            
    def continueRunning(self):
        if(not self.running):
            self.startTime = millis() - self.timeSoFar
            self.running = True
            
    def DisplayTime(self, maxtime):
        theTime = self.currentTime()
        output = "Time: " + str(maxtime - theTime)
        fill(255)
        font = loadFont("Sansation-Bold-35.vlw")
        textFont(font)
        text(output, self.x, self.y)
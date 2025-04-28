\# by Ava

"""
Processing was having glitches so this doesn't run but here is a detailed explanation of what should happen: 
Opens to a screen with a light blue background and the powerhop logo with text prompting the user to press
any key to get advance to the next screen. Once a key is pressed it switches to a screen with a green section
with two roads of cars at the bottom and a blue section with logs moving in it. There are 5 sections of land at the top.
The frog starts at the bottom of the screen and can move using the arrow keys or w, a, s, and d. Every 3 seconds a fly
appears and every 4 seconds a powerup appears. There are 3 types of powerups that can appear, the type is chosen 
randomly. The player can collect the flies by colliding with them to get points. The player can collide with a powerup 
to get it's effect. The effects are: slow time, double points, and health bonus. The effects last for 2 seconds. 
The player is trying to get to the land chunks at the end. Once one frog makes it, a new frog appears. The
player has to get all 5 frogs to the end while getting as many points as possible. If the player gets hit by a car
or falls in the water they lose a life. Once the player loses all of their lives they die and are taken to a screen 
telling them they lost and asking if they want to play again. If the player wins they are taken to a simallar screen
exact it says that they won, their points, and remaining lives.

"""

# imports
from Car import Car
from Fly import Fly
from Log import Log
from Player import Player 
from Powerup import Powerup
import random

# defines variables
logo = None
f = None
play = False  
car_img = None
cars = []
powups = []
activePowups[]
expirations[]
flies = []
logs = []
score = 0 
time = millis()
letter = "d"
Frog_img = None
lives = 0

def setup():
    global logo, car_img, f, car
    size(800, 600)
    logo = loadImage("logo.png")
    background(100, 100, 255)
    f = createFont("Arial", 30)
    textFont(f, 30)
    textAlign(CENTER)
    
# Instantiate Car class 
    cars.append(Car(100,height*.6, direction="right", speed=5, vehicle_type="car"))
    cars.append(Car(200,height*.6, direction="right", speed=5, vehicle_type="truck"))
    cars.append(Car(0,height*.6, direction="right", speed=5, vehicle_type="car"))
    cars.append(Car(100,height*.8, direction="right", speed=5, vehicle_type="truck"))
    cars.append(Car(300,height*.8, direction="right", speed=5, vehicle_type="car"))
    cars.append(Car(400,height*.8, direction="right", speed=5, vehicle_type="car"))
    
# Instantiate Log class
    logs.append(Log(0,height*.1))
    logs.append(Log(200,height*.1))
    logs.append(Log(400,height*.1))
    logs.append(Log(0,height*.2))
    logs.append(Log(300,height*.2))
    logs.append(Log(100,height*.3))
    logs.append(Log(500,height*.3))
    logs.append(Log(700,height*.3))
    logs.append(Log(0,height*.4))
    logs.append(Log(650,height*.5))
    logs.append(Log(320,height*.5))
    logs.append(Log(100,height*.5))
    
    #instantiate first player
    p1 = Player(width/2,height,3,3,Frog_img)
    currentFrog = p1

#controls game screens and objects
def draw():
    if play:
        playScreen()
        #instantiate cars
        for Car in cars:
            car.dispay()
            car.move()
            
        # instantiate fly class every 3 seconds
        if time%3000 == 0:
            flies.append(Fly())
    
        # instantiate powerup class every 4 seconds
        num = randInt(1,3)
        if num == 1:
            letter = "a"
        elif num == 2:
            letter = "b"
        else:
            letter = "c"
        if time%4000 == 0:
            powups.append(Powerup(letter))
            
        #add more players once current player has reached goal. End the game if all players are at goals
        if currentFrog.y <= .1:
            p2 = Player(width/2, height, 3,3,Frog_img)
            if currentFrog == p1:
                p2 = Player(width/2,height,3,3,Frog_img)
                currentFrog = p2
            elif currentFrog == p2:
                p3 = Player(width/2,height,3,3,Frog_img)
                currentFrog = p3
            elif currentFrog == p3:
                p4 = Player(width/2,height,3,3,Frog_img)
                currentFrog = p4
            elif currentFrog == p4:
                p5 = Player(width/2,height,3,3,Frog_img)
                currentFrog = p5
            else:
                won = true
                play = not play
                
        #checks for lives deduction
        # checks for collision with car
        for car in cars:
            if car.check_collision == True:
                lives = lives - 1
        #checks if frog fell in water
        if currentForg.y <= .5 * height and currentFrog.y >= .1 * height and log.checkCol(currentPlayer) == False:
            lives = lives -1
        
        # checks for points by getting flies
        for fly in flies:
            if Player.collides_with(fly):
                score = score + 50
                #need code here to add more points if powerup type b is claimed. Waiting on timer for powerups
                
                
        # adds claimed powerups to a class of active powerups        
        for p in powups:
            if play.collides_with(p):
                activePowups.append(p)
                #starts timer for powerup
                expirationTime = time + 2000
                expirations.append(experationTime)
                
                #checks if timer has ended
        for t in expirations:
             if t == expirationTime:
                 expiringPowup = activePowups[expirations.index[t]]
                 activePowups.remove(expiringPowup)                    
                               
          #loops through powerup effects                         
        for p in activePowups:
            expireTime = time + 2000        
            if p(letter) == "a":
                #method to execute powerup once katelyn adds it
            elif p(letter) == "b":
                #method to execute powerup once katelyn adds it
            else:
                #method to execute powerup once katelyn adds it
              
                #goes through screens for when game is over  
    elif won:
        wonScreen()   
    elif dead:
        deadScreen()
    else:  
        startScreen()

# Optional: Add key press to toggle
def keyPressed():
    global play
    play = not play

def playScreen():
    background(255)
    #street
    fill(107, 103, 110)
    rect(0, height * 0.8, width, height * 0.1)  # Adjust for screen size
    rect(0, height * 0.6, width, height * 0.1)

    # Water blue
    fill(85, 153, 242)
    rect(0, 0, width, height * 0.5)

    # Grass green
    fill(16, 125, 45)
    rect(0, height * 0.9, width, height * 0.1)
    rect(0, height * 0.7, width, height * 0.1)
    rect(0, height * 0.5, width, height * 0.1)

    # Safe goals level ended
    rect(0, 0, width * 0.125, height * 0.1)
    rect(width * 0.225, 0, width * 0.125, height * 0.1)
    rect(width * 0.45, 0, width * 0.125, height * 0.1)
    rect(width * 0.675, 0, width * 0.125, height * 0.1)
    rect(width * 0.9, 0, width * 0.125, height * 0.1)

    # Yellow dashes
    fill(232, 229, 30)
    dash_width = width * 0.075  # Set width of the dashes relative to canvas size
    rect(0, height * 0.85, dash_width, 5)
    for i in range(1, 7):
        rect(i * width * 0.15, height * 0.85, dash_width, 5)

    # Yellow dashes higher line
    for i in range(7):
        rect(i * width * 0.15, height * 0.65, dash_width, 5)
        
    # dashboard
    rect(0,0, width * .2, height * .2)
    text("Score" + str(score), width*.1, height *.05)
    text("lives" +str(lives), width*.1, height * .1)
    text("active powerups:", width*.1, height * .1)
    # once timer is implemented add code to display active powerups
#intro screen
def startScreen():
    background(120, 170, 255)
    image(img, 250, 300, img.width*9, img.height*9)
    fill(0)
    text("Welcome to PowerHop", 400, 200)
    text("Press any key to start", 400,250)
    
#gameover screen if the player won
def wonScreen():
    global play
    play = not play
    background(255)
    fill(0)
    text("Game won!", 400,200)
    text("score: " + str(score) + "remaining lives: " + str(lives), 400, 250)
    text("Press any kjey to play again", 400, 300)
    
#game over screen if the player lost
def deadScreen():
    global play
    play = not play
    background(255)
    fill(0)
    text("Game lost!", 400,200)
    text("score: " + str(score), 400, 250)
    text("Press any key to play again", 400, 300)

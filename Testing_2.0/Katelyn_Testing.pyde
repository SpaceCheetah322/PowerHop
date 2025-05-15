"""
This is the program I (Katelyn) have been using to test certain classes and functions.
Working:
    - All the classes
    - Sporadic powerup/fly spawning
    - Health and score system
WIP:
    - Time-slow powerup
"""

from Fly import Fly
from Player import Player
from Powerup import Powerup
from Car import Car
from Timer import Timer
import random

def setup():
    global fly_one, player, frog_img, p1, c1, heart, fly_spawn, pow_spawn, flies, pows
    imageMode(CENTER)
    size(500, 500)
    frog_img = loadImage("Frogger_Frog.gif")
    fly_one = Fly()
    player = Player(250, 450, 40, 3, frog_img)
    p1 = Powerup('b')
    c1 = Car(500, 250, "l", "a")
    heart = loadImage("Frogger_Life_Icon.gif")
    pow_spawn = Timer(15000)
    fly_spawn = Timer(10000)
    car_spawn = Timer(random.randint(2000, 5000))
    fly_spawn.start()
    pow_spawn.start()
    flies = []
    pows = []
    cars = [c1]

def draw():
    global p1, fly_one, c1, player, fly_spawn, pow_spawn, flies, pows, cars
    if fly_spawn.done():
        flies.append(Fly())
        fly_spawn.start()
    if pow_spawn.done():
        pows.append(Powerup(random.randint(1,3)))
        pow_spawn.start()
    # Scoreboard
    background(255)
    fill(200)
    noStroke()
    rect(0, 0, 100, 50, 7)
    textSize(20)
    fill(0)
    if (player != None): # Health and Score!
        text("Score: " + str(player.score), 10, 30)
        player.display()
        lives = player.lives
        for i in range (lives):
            image(heart, 480 - i * 25, 20)
    if (p1 != None):
        p1.display()
        if (player != None and p1.collision(player) == True):
            p1 = None
    for i in range (len(flies)):
        if (flies[i] != None):
            flies[i].move()
            if (player != None and flies[i].collision(player) == True):
                flies.remove(flies[i])
                player.score += 10
    for i in range (len(pows)):
        if (pows[i] != None):
            pows[i].display()
            if (player != None and pows[i].collision(player) == True):
                pows.remove(pows[i])
    c1.move()
    if (player != None and c1.check_collision(player) == True):
        player.lives -= 1
        if player.lives == 0:
            player = None
        else:
            player.x = 250
            player.y = 450

def keyPressed():
    global player
    if player != None:
        player.move(keyCode)

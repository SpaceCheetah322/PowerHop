from Player import Player
from Fly import Fly
from Powerup import Powerup
from Log import Log
from Car import Car
import random

def setup():
    global player, frog_img, fly_one, score, fly_respawn_timer, fly_respawn_delay, p1, p2, p3, lives
    global grass_img
    grass_img = loadImage("grass.png")
    size(500, 500)
    frameRate(30)
    frog_img = loadImage("Frogger_Frog_Front_Two.gif")
    fly_one = Fly()
    player = Player(width/2-20, 436, 40, 3, frog_img)
    score = 0
    fly_respawn_timer = 0
    fly_respawn_delay = 0
    lives = 3
    
    p1 = Powerup("a")
    p2 = Powerup("b")
    p3 = Powerup("c")
    p1.display()
    p2.display()
    p3.display()


def draw():
    global player, fly_one, score, fly_respawn_timer, fly_respawn_delay, p1, p2, p3, lives
    background(0, 0, 71)
    fill(0)
    rect(0,220,530,280)
    fill(177, 24, 219)
    
    p1.display()
    p2.display()
    p3.display()
    
    for i in range(16):
        image(grass_img, i * grass_img.width, 209)


    if fly_one is not None:
            fly_one.move()
            if player.collides_with(fly_one):
                score += 10
                fly_one = None
                fly_respawn_timer = frameCount  # record when it was destroyed
                fly_respawn_delay = int(random(270, 330))  # random 9-11 seconds. Take into account 30fps for time calc

    else:
        # Check if enough time passed
        if frameCount - fly_respawn_timer > fly_respawn_delay:
            fly_one = Fly()  # Spawn new fly!

    fill(0)
    textSize(24)
    text("Score: " + str(score), 10, 30)

    player.display()


def keyPressed():
    player.move(keyCode)

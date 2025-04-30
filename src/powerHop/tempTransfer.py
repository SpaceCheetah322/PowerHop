from Player import Player
from Fly import Fly
from Powerup import Powerup

def setup():
    global player, frog_img, fly_one, score, fly_respawn_timer, fly_respawn_delay, p1, p2, p3, lives
    size(500, 500)
    frameRate(30)
    frog_img = loadImage("Frogger_Frog_Front_Two.gif")
    fly_one = Fly()
    player = Player(width/2-20, 436, 40, 3, frog_img)
    print(fly_one.frame_1)
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
    background(2, 33, 84)
    fill(177, 24, 219)
    noStroke()
    rect(0, 420, 500, 80)
    

    p1.display()
    p2.display()
    p3.display()


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














# Written by Katelyn
# NOTE: GIF and Movement working! Working on collision.

# Imports
import time
import random
from Timer import Timer

# Class
class Fly:
    # Constructor
    def __init__(self): # Initialization
        # Variable Declaration
        self.frame_num = 0
        self.height = 30
        self.width = 30
        self.x = random.randint(100, 400)
        self.y = random.randint(100, 400)
        self.speed = 1
        self.x_loc = random.randint(0, 500) # Target location! Replace 500 with game width!
        self.y_loc = random.randint(0, 500) # Target location! Replace 500 with game height!
        self.waiting = False
        # Defining Images
        self.frame_1 = loadImage("Frogger_Fly_Frame1.gif")
        self.frame_2 = loadImage("Frogger_Fly_Frame2.gif")
        self.frame_3 = loadImage("Frogger_Fly_Frame3.gif")
        self.frame_4 = loadImage("Frogger_Fly_Frame2.gif")
        # Compiling a list of frames
        self.animation = [self.frame_1, self.frame_2, self.frame_3, self.frame_4]
        self.fly_time = Timer(2000)
        
    # Methods
    def display(self): # Displays fly, uses frame_num as a counter to change frames
        image(self.animation[self.frame_num // 2], self.x, self.y) # Multiples of two to slow down animation
        if (self.frame_num >= 0 and self.frame_num < 6):
            self.frame_num += 1
        elif (self.frame_num == 6):
            self.frame_num = 0 # Loop

    def move(self): # Moves fly towards random location. If location reached, wait a couple seconds and choose a new target.
        if self.waiting == True: # If the timer is already started (and the fly is stopped)
            if (self.fly_time.done() == True): # Checks if timer has ended
                self.x_loc = random.randint(0, 500)
                self.y_loc = random.randint(0, 500)
                self.speed = 1
                self.waiting = False
        else:
            # Moves Left/Right
            if (self.x < self.x_loc):
                self.x += self.speed
            elif (self.x > self.x_loc):
                self.x -= self.speed
            # Moves Up/Down
            if (self.y < self.y_loc):
                self.y += self.speed
            elif (self.y > self.y_loc):
                self.y -= self.speed
            # Checks if target is reached and begins timer
            if (self.x == self.x_loc and self.y == self.y_loc):
                time_start = False
                self.speed = 0
                self.fly_time.start()
                self.waiting = True
        self.display()






class Player:
    def __init__(self, x, y, speed, lives, img):
        self.x = x
        self.y = y
        self.speed = 40
        self.lives = lives
        self.img = img
        self.width = img.width
        self.height = img.height

    def move(self, key_code):
        if key_code == LEFT or key == 'a':
            self.x -= self.speed
        elif key_code == RIGHT or key == 'd':
            self.x += self.speed
        elif key_code == UP or key == 'w':
            self.y -= self.speed
        elif key_code == DOWN or key == 's':
            self.y += self.speed
    
        # Keep the player inside the screen
        self.x = constrain(self.x, 0, width - self.width)
        self.y = constrain(self.y, 0, height - self.height)


    def display(self):
        image(self.img, self.x, self.y)
        
    def collides_with(self, other):
        return (
            self.x < other.x + other.width and
            self.x + self.width > other.x and
            self.y < other.y + other.height and
            self.y + self.height > other.y
        )












# Written by Katelyn
# NOTES: Display is functioning! Powerup should appear in a random location when called. Collision detection also functional!
# Might end up having to resize graphics.
"""
Powerups:
a. Slow time
b. Point X2
c. Extra life
Use the letters each powerup is assigned when calling them in, eg. 'health = Powerup("c")'
More might be added in the future; these are some basic ones that should be easy to put in.

Other Ideas:
d. Luck boost (Increased chances of powerup/fly spawning?)
e. Long Leap (Jump further. Not sure if this is as helpful to the player as it seems.)
"""
import time
import random

class Powerup:
    # Constructor
    def __init__(self, type):
        self.type = type
        self.x = random.randint(0, 500) # 500 is temporary! Replace with game length.
        self.y = random.randint(0, 500) # 500 is temporary! Replace with game height.
        self.time_slow = loadImage("Frogger_Clock_Powerup.gif") # Shows up as a blue icon with a frozen clock.
        self.double_points = loadImage("Frogger_Point_Powerup.gif") # Shows up as a yellow icon witih a four-pointed star. A bit off-center, nothing to be done about it though.
        self.health_bonus = loadImage("Frogger_Health_Powerup.gif") # Shows up as a red icon with a medical (+) sign.

    # Methods
    def display(self): # Displays powerup
        if self.type == "a": 
            image(self.time_slow, self.x, self.y)
        elif self.type == "b": 
            image(self.double_points, self.x, self.y)
        elif self.type == "c": 
            image(self.health_bonus, self.x, self.y)

    def collision(self, player_x, player_y):
        distance = dist(self.x, self.y, player_x, player_y)
        if distance < 64:
            return True
        else:
            return False










# -*- coding: utf-8 -*-
class Timer:
    def __init__(self, total_time):
        self.saved_time = 0
        self.total_time = total_time

    def start(self):
        self.saved_time = millis()

    def done(self):
        return (millis() - self.saved_time) > self.total_time











# Written by Katelyn
# NOTE: GIF and Movement working! Working on collision.
# Graphics may need to be resized.

# Imports
import time
import random

# Class
class Fly:
    # Constructor
    def __init__(self): # Initialization
        # Variable Declaration
        self.frame_num = 0
        self.x = 250 # Spawn location! Temporary and can/will change!
        self.y = 250 # Spawn location! Temporary and can/will change!
        self.x_speed = random.randint(1, 3)
        self.y_speed = random.randint(1, 3)
        self.x_loc = random.randint(0, 500) # Replace 500 with game width!
        self.y_loc = random.randint(0, 500) # Replace 500 with game height!
        # Defining Images
        self.frame_1 = loadImage("Frogger_Fly_Frame1.gif")
        self.frame_2 = loadImage("Frogger_Fly_Frame2.gif")
        self.frame_3 = loadImage("Frogger_Fly_Frame3.gif")
        self.frame_4 = loadImage("Frogger_Fly_Frame2.gif")
        # Compiling a list of frames
        self.animation = [self.frame_1, self.frame_2, self.frame_3, self.frame_4]

    # Methods
    def display(self): # Displays fly, uses frame_num as a counter to change frames
        image(self.animation[self.frame_num / 2], self.x, self.y) # Multiples of two to slow down animation
        if (self.frame_num >= 0 and self.frame_num < 6):
            self.frame_num += 1
        elif (self.frame_num == 6):
            self.frame_num = 0 # Loop

    def move(self): # Moves fly towards random location. If location reached, wait a couple seconds and choose a new target.
        # Moves Left/Right
        if (self.x < self.x_loc):
            self.x += self.x_speed
        elif (self.x > self.x_loc):
            self.x -= self.x_speed
        # Moves Up/Down
        if (self.y < self.y_loc):
            self.y += self.y_speed
        elif (self.y > self.y_loc):
            self.y -= self.y_speed
        # Stops and chooses new target if achieved
        if (self.x == self.x_loc and self.y == self.y_loc):
            self.x_loc = random.randint(0, 500)
            self.y_loc = random.randint(0, 500)
            time.sleep(2) # How long the fly stops; might change later!
        self.display()
        # Not really necessary, and attempt to change the speed of the fly. Not entirely sure if it works.
        self.x_speed = random.randint(1, 3)
        self.y_speed = random.randint(1, 3)

"""
Code used for Testing:

from Fly import Fly

def setup():
    global fly_one
    size(500, 500)
    fly_one = Fly()

def draw():
    background(255)
    fly_one.move()
"""

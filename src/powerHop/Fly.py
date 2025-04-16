# Written by Katelyn
# NOTE: Movement semi-works, GIF work-in-progress

# Imports
import time
import random

# Class
class Fly:
    # Constructor
    def __init__(self): # Initialization
        # Variable Declaration
        self.x = 250
        self.y = 250
        self.x_speed = random.randint(1, 3)
        self.y_speed = random.randint(1, 3)
        self.x_loc = random.randint(0, 500) # Replace 500 with game width!
        self.y_loc = random.randint(0, 500) # Replace 500 with game height!
        # Defining Images
        self.frame_1 = loadImage("Frogger_Fly_Frame1.gif")
        self.frame_2 = loadImage("Frogger_Fly_Frame2.gif")
        self.frame_3 = loadImage("Frogger_Fly_Frame3.gif")
        self.frame_4 = loadImage("Frogger_Fly_Frame2.gif")

    # Methods
    def display(self): # Displays fly; might house GIF frames someday
        image(self.frame_1, self.x, self.y)

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
        # Stops and chooses mew target if achieved
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
    fly_one.display()
    fly_one.move()

def draw():
    background(255)
    fly_one.move()
"""

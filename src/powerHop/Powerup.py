"""
Ideas for Powerups:
a. Slow time
b. Point X2
c. Extra life
"""
import time
import random

class Powerup:
    # Constructor
    def __init__(self, type):
        self.type = type
        self.x = random.randint(500, 500)
        self.y = random.randint(500, 500)
        # Graphics WIP
        self.time_slow = loadImage("Frogger_Clock_Powerup.gif")
        self.double_points = loadImage()
        self.health_bonus = loadImage()

    # Methods
    def display(self): # Displays fly; might house GIF frames someday
        if self.type == 'a': 
            image(, self.x, self.y)
        elif self.type == 'a': 
            image(, self.x, self.y)
        elif self.type == 'a': 
            image(, self.x, self.y)

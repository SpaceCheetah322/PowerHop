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
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 500)
        # Graphics WIP
        self.time_slow = loadImage("Frogger_Clock_Powerup.gif")
        self.double_points = loadImage("Frogger_Clock_Powerup.gif")
        self.health_bonus = loadImage("Frogger_Clock_Powerup.gif")

    # Methods
    def display(self): # Displays fly; might house GIF frames someday
        if self.type == 'a': 
            image(time_slow, self.x, self.y)
        elif self.type == 'b': 
            image(double_points, self.x, self.y)
        elif self.type == 'c': 
            image(health_bonus, self.x, self.y)

    def collision(self):
        pass # For now!

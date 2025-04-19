# Written by Katelyn
# NOTES: Display is functioning! Powerup should appear in a random location when called. No collision detection yet.
"""
Powerups:
a. Slow time
b. Point X2
c. Extra life
Use the letters each powerup is assigned when calling them in, eg. 'health = Powerup("c")'
More might be added in the future; these are some basic ones that should be easy to put in.
"""
import time
import random

class Powerup:
    # Constructor
    def __init__(self, type):
        print("Initiating")
        self.type = type
        self.x = random.randint(0, 500) # 500 is temporary! Replace with game length.
        self.y = random.randint(0, 500) # 500 is temporary! Replace with game height.
        self.time_slow = loadImage("Frogger_Clock_Powerup.gif")
        self.double_points = loadImage("Frogger_Point_Powerup.gif") # The four-pointed star on this one is a bit off-center. Nothing to be dfone about it though.
        self.health_bonus = loadImage("Frogger_Health_Powerup.gif")

    # Methods
    def display(self): # Displays powerup
        print("Display entered")
        if self.type == "a": 
            image(self.time_slow, self.x, self.y)
        elif self.type == "b": 
            image(self.double_points, self.x, self.y)
        elif self.type == "c": 
            image(self.health_bonus, self.x, self.y)

    def collision(self):
        pass # For now!

"""
Code used for Testing:

from Powerup import Powerup

def setup():
    size(500, 500)
    print("Working")
    p1 = Powerup("a")
    p2 = Powerup("b")
    p3 = Powerup("c")
    print("Created")
    p1.display()
    p2.display()
    p3.display()

def draw():
    pass
"""

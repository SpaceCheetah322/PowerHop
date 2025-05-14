# Written by Katelyn
# NOTES: Display is functioning! Powerup should appear in a random location when called. No collision detection yet.
# Might end up having to resize graphics.
"""
Powerups:
1. Slow time
2. Point X2
3. Extra life
Use the letters each powerup is assigned when calling them in, eg. 'health = Powerup("c")'
More might be added in the future; these are some basic ones that should be easy to put in.

Other Ideas:
d. Luck boost (Increased chances of powerup/fly spawning?)
e. Long Leap (Jump further. Not sure if this is as helpful to the player as it seems.)
"""
import time
import random
from Car import Car

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
        if self.type == 1: 
            image(self.time_slow, self.x, self.y)
        elif self.type == 2: 
            image(self.double_points, self.x, self.y)
        elif self.type == 3: 
            image(self.health_bonus, self.x, self.y)

    def collision(self, player):
        distance = dist(self.x, self.y, player.x, player.y)
        if distance < 64:
            if self.type == 1:
                pass
                # car.speed /= 2
            elif self.type == 2:
                player.score += 10
            elif self.type == 3:
                player.lives += 1
            return True
        else:
            return False

"""
Code used for Testing:

from Powerup import Powerup

def setup():
    size(500, 500)
    p1 = Powerup("a")
    p2 = Powerup("b")
    p3 = Powerup("c")
    p1.display()
    p2.display()
    p3.display()

def draw():
    pass
"""

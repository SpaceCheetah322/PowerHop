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
        self.time_slow = loadImage("Frogger_Fly_Frame1.gif")
        self.double_points = loadImage("Frogger_Fly_Frame2.gif")
        self.health_bonus = loadImage("Frogger_Fly_Frame3.gif")

    # Methods
    def display(self, type): # Displays fly; might house GIF frames someday
        image(self.frame_1, self.x, self.y)

    def move(self): # Moves fly towards random location. If location reached, wait a couple seconds and choose a new target.
        if (self.x < self.x_loc):
            self.x += self.x_speed
        elif (self.x > self.x_loc):
            self.x -= self.x_speed
        if (self.y < self.y_loc):
            self.y += self.y_speed
        elif (self.y > self.y_loc):
            self.y -= self.y_speed
        if (self.x == self.x_loc and self.y == self.y_loc):
            self.x_loc = random.randint(0, 500)
            self.y_loc = random.randint(0, 500)
            time.sleep(2)
        self.display()
        self.x_speed = random.randint(1, 3)
        self.y_speed = random.randint(1, 3)

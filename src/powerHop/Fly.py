# NOTE: Movement semi-works, GIF work-in-progress
import time
import random

class Fly:
    # Constructor
    def __init__(self):
        self.x = 250
        self.y = 250
        self.x_speed = random.randint(1, 3)
        self.y_speed = random.randint(1, 3)
        self.x_loc = random.randint(0, 500)
        self.y_loc = random.randint(0, 500)
        self.frame_1 = loadImage("Frogger_Fly_Frame1.gif")
        self.frame_2 = loadImage("Frogger_Fly_Frame2.gif")
        self.frame_3 = loadImage("Frogger_Fly_Frame3.gif")
        self.frame_4 = loadImage("Frogger_Fly_Frame2.gif")

    # Methods
    def display(self): # Displays fly; might house GIF frames someday
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

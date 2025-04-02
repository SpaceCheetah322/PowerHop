# NOTE: Movement semi-works, GIF work-in-progress
import time
import random

class Fly:
    # Constructor
    def __init__(self):
        print("Entered Class")
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
        print("Initiation complete")

    # Methods
    def display(self):
        image(self.frame_1, self.x, self.y)
        print("Displayed")

    def move(self):
        print("Move classs entered")
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
        print("Direction determined")
        self.display()
        print("Moved")
        self.x_speed = random.randint(1, 3)
        self.y_speed = random.randint(1, 3)
        print("Speed adjusted")

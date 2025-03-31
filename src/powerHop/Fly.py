import math
import time
import random

# MOVEMENT IS WIP!

class Fly:
    def __init__(self, image_path):
        self.x = 0
        self.y = 0
        x_speed = random.randint(1, 3)
        y_speed = random.randint(1, 3)
        x_loc = random.randint(0, 500)
        y_loc = random.randint(0, 500)
        self.isCollected = False
        self.image = image_path  # Placeholder for the image. Not exactly sure how to do this yet but the image is ready in the folder.

    def spawn(self):
        pass  # Logic for spawning the fly

    def move(x, y):
        # Fly will rest for 3 seconds, then move to a random location on screen.
        while (x != x_loc or y != y_loc):
                if (x < x_loc):
                    x += x_speed
                elif (x > x_loc):
                    x -= x_speed
                if (y < y_loc):
                    y += y_speed
                elif (y > y_loc):
                    y -= y_speed
        if (x == x_loc and y == y_loc):
            x_loc = random.randint(0, 500)
            y_loc = random.randint(0, 500)
            time.sleep(3)

    def checkCol(self, player): # Not at ALL sure if this works or not.
        # player_loc = [player.x, player.y]
        # loc = [x, y]
        # distance = math.dist(player_loc, loc)
        # if (distance <= 5):
        #     main.points += 5
        #     isCollected = True
        #     DELETE FLY
        pass  # Logic for checking collision with the player
        

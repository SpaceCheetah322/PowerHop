import math
import time
import random

class Fly:
    def __init__(self, image_path):
        self.x = 0
        self.y = 0
        self.direction = 1
        self.isCollected = False
        self.image = image_path  # Placeholder for the image. Not exactly sure how to do this yet but the image is ready in the folder.

    def spawn(self):
        pass  # Logic for spawning the fly

    def move(x, y):
        time.sleep(7)
        x += (random.randint(-15,15)) * direction
        y += (random.randint(-15,15)) * direction

    def checkCol(self, player): # Not at ALL sure if this works or not.
        # player_loc = [player.x, player.y]
        # loc = [x, y]
        # distance = math.dist(player_loc, loc)
        # if (distance <= 5):
        #     main.points += 5
        #     isCollected = True
        #     DELETE FLY
        pass  # Logic for checking collision with the player

import math
class Fly:
    def __init__(self, image_path):
        self.x = 0
        self.y = 0
        self.isCollected = False
        self.image = image_path  # Placeholder for the image

    def spawn(self):
        pass  # Logic for spawning the fly

    def checkCol(self, player):
        # player_loc = [player.x, player.y]
        # loc = [x, y]
        # distance = math.dist(player_loc, loc)
        # if (distance <= 5):
        #     main.points += 5
        pass  # Logic for checking collision with the player

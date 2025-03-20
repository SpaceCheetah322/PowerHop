class Player:
    def __init__(self, x, y, speed, lives, image_path):
        self.x = x
        self.y = y
        self.speed = speed
        self.lives = lives
        self.image = image_path  # Placeholder for the image

    def move(self):
        pass  # Logic for player movement

    def checkCol(self, obj):
        pass  # Logic for checking collision with another object

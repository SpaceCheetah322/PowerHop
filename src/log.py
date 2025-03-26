#by ava
class Log:
    def __init__(self, x, y, speed, direction, image_path):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.image = image_path  # Placeholder for the image

    def move(self):
        pass  # Logic for car movement

    def checkCol(self, obj):
        pass  # Logic for checking collision with another object

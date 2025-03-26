class Car:
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
img = None

def setup():
    # Load the PNG image from the data folder
    global img
    img = loadImage("Car Piskel (1).png")  # Make sure the file is in the data folder
    size(800, 600)  # Set the size of the window

def draw():
    # Clear the screen with a white background
    background(255)

    image(img, 200, 200)

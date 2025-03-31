class Car:
    import random
    
    def __init__(self, x, y, speed, direction,num):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 30
        self.speed = speed
        self.direction = direction
        self.num = random.choice([1, 2, 3])




    def move(self):
        if self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed


    def check_collision(self, frog):
        if frog.x < self.x + self.width and frog.x + frog.width > self.x and frog.y < self.y + self.height and frog.y + frog.height > self.y:
            return True
        return False
img = None

def setup():

    global img
    img = loadImage("Car Piskel (1).png")  # Make sure the file is in the data folder
    size(800, 600)  # Set the size of the window

def draw():

    background(255)

    image(img, 200, 200)

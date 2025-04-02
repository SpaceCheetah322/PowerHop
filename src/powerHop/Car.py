class Car:
    import random
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        global crr
        crr = loadImage("Car.png")  
        crr = None





    def move(self):
        if self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed


    def check_collision(self, frog):
        if frog.x < self.x + self.width and frog.x + frog.width > self.x and frog.y < self.y + self.height and frog.y + frog.height > self.y:
            return True
        return False
    def display():
        background(255)
        image(crr, 200, 200, img.width*4, img.height*4)

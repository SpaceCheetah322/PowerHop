class Car:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = 50
        self.height = 30
    
    def update(self):
        self.x += self.speed
        # Wrap around screen
        if self.x > width:
            self.x = -self.width
        elif self.x < -self.width:
            self.x = width
    
    def display(self):
        fill(255, 0, 0)  # Red car
        rect(self.x, self.y, self.width, self.height)

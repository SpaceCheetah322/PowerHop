class Frog:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 30
    
    def display(self):
        fill(0, 255, 0)  # Green frog
        # Body
        ellipse(self.x, self.y, self.size, self.size)
        # Eyes
        fill(255)  # White eyes
        ellipse(self.x - 10, self.y - 10, 10, 10)
        ellipse(self.x + 10, self.y - 10, 10, 10)
        fill(0)  # Black pupils
        ellipse(self.x - 10, self.y - 10, 5, 5)
        ellipse(self.x + 10, self.y - 10, 5, 5)

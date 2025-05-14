"""
Vehicle Types:
    a) Truck
    b) Car
    
Directions:
    'l' = Left
    'r' = Right
"""
class Car:
    def __init__(self, x, y, direction, vehicle_type):
        self.x = x
        self.width = 32
        self.height = 32
        self.start_x = x
        self.y = y
        self.direction = direction
        self.speed = 5
        self.vehicle_type = vehicle_type
        if vehicle_type == "a":
            self.vehicle = loadImage("Frogger_Red_Truck.gif")
        elif vehicle_type == "b":
            pass
    
    def display(self):
        if self.vehicle_type == "a":
            image(self.vehicle, self.x, self.y)
    
    def move(self):
        if self.direction == 'r':
            self.x += self.speed
            if self.x > 800:
                self.x = self.start_x
        elif self.direction == 'l':
            self.x -= self.speed
            if self.x < 0:
                self.x = self.start_x
        self.display()

    def check_collision(self, player):
        if (player.x < self.x + self.width and
            player.x + player.width > self.x and
            player.y < self.y + self.height and
            player.y + player.height > self.y):
            return True
        return False

    # I couldn't figure out how to use this method :( Commented out and replaced for now.
    # def display(self):
    #     if self.vehicle not in get_elements():
    #         add(vehicle)
    #     self.vehicle.set_position(self.x, self.y)

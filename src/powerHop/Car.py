# New version at the bottom!
class Car:
    def __init__(self, x, y, direction="right", speed=5, vehicle_type="car"):
        self.x = x
        self.start_x = x
        self.y = y
        self.direction = direction
        self.speed = speed
        self.vehicle_type = vehicle_type


        image_file = "Car.png"
        if self.vehicle_type == "truck":
            image_file = "Frogger_Red_Truck.gif"

        self.image = Image(image_file)
        

        scale = 0.2 if self.vehicle_type == "car" else 0.3
        self.image.set_size(self.image.get_width() * scale, self.image.get_height() * scale)
        self.image.set_position(self.x, self.y)
        add(self.image)

        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def move(self):
        if self.direction == 'right':
            self.x += self.speed
            if self.x > 800:
                self.x = self.start_x
        elif self.direction == 'left':
            self.x -= self.speed
            if self.x + self.width < 0:
                self.x = self.start_x

        self.image.set_position(self.x, self.y)

    def check_collision(self, frog):
        if (frog.x < self.x + self.width and
            frog.x + frog.width > self.x and
            frog.y < self.y + self.height and
            frog.y + frog.height > self.y):
            return True
        return False

    def display(self):
        if self.image not in get_elements():
            add(self.image)
        self.image.set_position(self.x, self.y)

"""
The following is the new code for this class. It displays and has collision (at least
in the circumstances I tested it in). Do with it as you'd like: use it to change the
current version, replace the current version, whatever.
- Katelyn

New Code:
""f"
Vehicle Types:
    a) Truck
    b) Car
    
Directions:
    'l' = Left
    'r' = Right
""f"
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
        print("still here")
        self.display()
        print(self.x, self.y)

    def check_collision(self, player):
        print("Entered")
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
"""

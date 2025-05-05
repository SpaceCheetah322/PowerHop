from Player import Player
from Fly import Fly
from Powerup import Powerup

game_started = False

def setup():
    global player, frog_img, fly_one, score, fly_respawn_timer, fly_respawn_delay, p1, p2, p3, lives, start_screen, game_started, car, car_img
    start_screen = loadImage("start_screen.png")  # Make sure this file exists in your project
    game_started = False

    size(800, 600)
    frameRate(30)
    frog_img = loadImage("Frogger_Frog_Front_Two.gif")
    fly_one = Fly()
    player = Player(width/2-20, 436, 40, 3, frog_img)
    print(fly_one.frame_1)
    score = 0
    fly_respawn_timer = 0
    fly_respawn_delay = 0
    lives = 3
    
    p1 = Powerup("c")  


def draw():
    global player, fly_one, score, fly_respawn_timer, fly_respawn_delay, p1, p2, p3, lives, game_started, car, car_img

    if not game_started:
        background(0)
        image(start_screen, 0, 0, width, height)
        return  # Skip the game logic until started

    # --- Your actual game code starts here ---

    if (p1 != None): # This prevents the program from trying to display it after it gets deleted.
        p1.display() 
        if (p1.collides_with(p1) == True):
                score += 1
                p1 = None

    
    background(2, 33, 84)
    background(255)
    #street
    fill(107, 103, 110)
    rect(0, height * 0.8, width, height * 0.1)  # Adjust for screen size
    rect(0, height * 0.6, width, height * 0.1)

    # Water blue
    fill(85, 153, 242)
    rect(0, 0, width, height * 0.5)

    # Grass green
    fill(16, 125, 45)
    rect(0, height * 0.9, width, height * 0.1)
    rect(0, height * 0.7, width, height * 0.1)
    rect(0, height * 0.5, width, height * 0.1)

    # Safe goals level ended
    rect(0, 0, width * 0.125, height * 0.1)
    rect(width * 0.225, 0, width * 0.125, height * 0.1)
    rect(width * 0.45, 0, width * 0.125, height * 0.1)
    rect(width * 0.675, 0, width * 0.125, height * 0.1)
    rect(width * 0.9, 0, width * 0.125, height * 0.1)

    # Yellow dashes
    fill(232, 229, 30)
    dash_width = width * 0.075  # Set width of the dashes relative to canvas size
    rect(0, height * 0.85, dash_width, 5)
    for i in range(1, 7):
        rect(i * width * 0.15, height * 0.85, dash_width, 5)

    # Yellow dashes higher line
    for i in range(7):
        rect(i * width * 0.15, height * 0.65, dash_width, 5)
    
    if fly_one is not None:
        fly_one.move()
        if player.collides_with(fly_one):
            score += 10
            fly_one = None
            fly_respawn_timer = frameCount
            fly_respawn_delay = int(random(270, 330))
    else:
        if frameCount - fly_respawn_timer > fly_respawn_delay:
            fly_one = Fly()

    fill(0)
    textSize(24)
    text("Score: " + str(score), 10, 30)

    player.display()


def keyPressed():
    player.move(keyCode)
    
def mousePressed():
    global game_started
    if not game_started:
        game_started = True









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
            image_file = "Truck.png"

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









# Written by Katelyn
# NOTE: GIF and Movement working! Working on collision.

# Imports
import time
import random
from Timer import Timer

# Class
class Fly:
    # Constructor
    def __init__(self): # Initialization
        # Variable Declaration
        self.frame_num = 0
        self.x = random.randint(100, 400) # Spawn location! Temporary and can/will change!
        self.y = random.randint(100, 400) # Spawn location! Temporary and can/will change!
        self.speed = 1
        self.height = 30 #For collision Detection
        self.width = 30 #For collision Detection
        self.x_loc = random.randint(0, 500) # Target location! Replace 500 with game width!
        self.y_loc = random.randint(0, 500) # Target location! Replace 500 with game height!
        self.waiting = False
        # Defining Images
        self.frame_1 = loadImage("Frogger_Fly_Frame1.gif")
        self.frame_2 = loadImage("Frogger_Fly_Frame2.gif")
        self.frame_3 = loadImage("Frogger_Fly_Frame3.gif")
        self.frame_4 = loadImage("Frogger_Fly_Frame2.gif")
        # Compiling a list of frames
        self.animation = [self.frame_1, self.frame_2, self.frame_3, self.frame_4]
        self.fly_time = Timer(2000)
        
    # Methods
    def display(self): # Displays fly, uses frame_num as a counter to change frames
        image(self.animation[self.frame_num // 2], self.x, self.y) # Multiples of two to slow down animation
        if (self.frame_num >= 0 and self.frame_num < 6):
            self.frame_num += 1
        elif (self.frame_num == 6):
            self.frame_num = 0 # Loop

    def move(self): # Moves fly towards random location. If location reached, wait a couple seconds and choose a new target.
        if self.waiting == True: # If the timer is already started (and the fly is stopped)
            if (self.fly_time.done() == True): # Checks if timer has ended
                self.x_loc = random.randint(0, 500)
                self.y_loc = random.randint(0, 500)
                self.speed = 1
                self.waiting = False
        else:
            # Moves Left/Right
            if (self.x < self.x_loc):
                self.x += self.speed
            elif (self.x > self.x_loc):
                self.x -= self.speed
            # Moves Up/Down
            if (self.y < self.y_loc):
                self.y += self.speed
            elif (self.y > self.y_loc):
                self.y -= self.speed
            # Checks if target is reached and begins timer
            if (self.x == self.x_loc and self.y == self.y_loc):
                time_start = False
                self.speed = 0
                self.fly_time.start()
                self.waiting = True
        self.display()











class Player:
    def __init__(self, x, y, speed, lives, img):
        self.x = x
        self.y = y
        self.speed = 60
        self.lives = lives
        self.img = img
        self.width = img.width
        self.height = img.height

    def move(self, key_code):
        if key_code == LEFT or key == 'a':
            self.x -= self.speed
        elif key_code == RIGHT or key == 'd':
            self.x += self.speed
        elif key_code == UP or key == 'w':
            self.y -= self.speed
        elif key_code == DOWN or key == 's':
            self.y += self.speed
    
        # Keep the player inside the screen
        self.x = constrain(self.x, 0, width - self.width)
        self.y = constrain(self.y, 0, height - self.height)


    def display(self):
        image(self.img, self.x, self.y)
        
    def collides_with(self, other):
        return (
            self.x < other.x + other.width and
            self.x + self.width > other.x and
            self.y < other.y + other.height and
            self.y + self.height > other.y
        )












# Written by Katelyn
# NOTES: Display and collision functioning! Powerup should appear in a random location when called. Effects usable(?)
# Might end up having to resize graphics.
"""
Powerups:
a. Slow time
b. Point X2
c. Extra life
Use the letters each powerup is assigned when calling them in, eg. 'health = Powerup("c")'
More might be added in the future; these are some basic ones that should be easy to put in.

Other Ideas:
d. Luck boost (Increased chances of powerup/fly spawning?)
e. Long Leap (Jump further. Not sure if this is as helpful to the player as it seems.)
"""
import time
import random

class Powerup:
    # Constructor
    def __init__(self, type):
        self.type = type
        self.x = random.randint(0, 500) # 500 is temporary! Replace with game length.
        self.y = random.randint(0, 500) # 500 is temporary! Replace with game height.
        self.width = 30
        self.height = 30
        self.time_slow = loadImage("Frogger_Clock_Powerup.gif") # Shows up as a blue icon with a frozen clock.
        self.double_points = loadImage("Frogger_Point_Powerup.gif") # Shows up as a yellow icon witih a four-pointed star. A bit off-center, nothing to be done about it though.
        self.health_bonus = loadImage("Frogger_Health_Powerup.gif") # Shows up as a red icon with a medical (+) sign.

    # Methods
    def display(self): # Displays powerup
        if self.type == "a": 
            image(self.time_slow, self.x, self.y)
        elif self.type == "b": 
            image(self.double_points, self.x, self.y)
        elif self.type == "c": 
            image(self.health_bonus, self.x, self.y)

    def collides_with(self, other):
        return (
            self.x < other.x + other.width and
            self.x + self.width > other.x and
            self.y < other.y + other.height and
            self.y + self.height > other.y
        )












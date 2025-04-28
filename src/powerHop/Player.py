"""
Collision detection is in place and ready to use

In order to use collision detection, use:
if player.collides_with(fly):
    #Do something
"""

class Player:
    def __init__(self, x, y, speed, lives, img):
        self.x = x
        self.y = y
        self.speed = 40
        self.lives = lives
        self.img = img
        self.width = img.width
        self.height = img.height
        #self.width = width
        #self.height = height

    def move(self, key_code):
        if key_code == LEFT or key == 'a':
            self.x -= self.speed
        elif key_code == RIGHT or key == 'd':
            self.x += self.speed
        elif key_code == UP or key == 'w':
            self.y -= self.speed
        elif key_code == DOWN or key == 's':
            self.y += self.speed

    def display(self):
        image(self.img, self.x, self.y)
        
    def collides_with(self, other):
        return (
            self.x < other.x + other.width and
            self.x + self.width > other.x and
            self.y < other.y + other.height and
            self.y + self.height > other.y
        )



"""
from Player import Player
from Fly import Fly

def setup():
    global player, frog_img, fly_one
    size(500, 500)
    frameRate(30)
    frog_img = loadImage("Frogger_Frog_Front_Two.gif")
    fly_one = Fly()
    player = Player(width/2-20, 450, 40, 3, frog_img)
    print(fly_one.frame_1)


def draw():
    background(2, 33, 84)
    fill(177, 24, 219)
    noStroke()
    rect(0,420,500,80)
    fly_one.move()
    player.display()


def keyPressed():
    player.move(keyCode)

"""

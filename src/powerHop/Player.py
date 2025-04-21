class Player:
    def __init__(self, x, y, speed, lives, img):
        self.x = x
        self.y = y
        self.speed = 40
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

    def display(self):
        image(self.img, self.x, self.y)



"""
from Player import Player

def setup():
    global player, frog_img
    size(500, 500)
    frameRate(30)
    
    frog_img = loadImage("Frogger_Frog_Front_Two.gif")
    player = Player(100, 100, 40, 3, frog_img)


def draw():
    background(187, 185, 195)
    player.display()


def keyPressed():
    player.move(keyCode)
"""

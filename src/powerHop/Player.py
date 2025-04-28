"""
Collision detection is in place and ready to use. Class NEEDS: a height and a width

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

"""
from Player import Player
from Fly import Fly

def setup():
    global player, frog_img, fly_one, score, fly_respawn_timer, fly_respawn_delay
    size(500, 500)
    frameRate(30)
    frog_img = loadImage("Frogger_Frog_Front_Two.gif")
    fly_one = Fly()
    player = Player(width/2-20, 450, 40, 3, frog_img)
    print(fly_one.frame_1)
    score = 0
    fly_respawn_timer = 0
    fly_respawn_delay = 0


def draw():
    global player, fly_one, score, fly_respawn_timer, fly_respawn_delay
    background(2, 33, 84)
    fill(177, 24, 219)
    noStroke()
    rect(0, 420, 500, 80)

    if fly_one is not None:
            fly_one.move()
            if player.collides_with(fly_one):
                score += 10
                fly_one = None
                fly_respawn_timer = frameCount  # record when it was eaten
                fly_respawn_delay = int(random(270, 330))  # random 9-11 seconds (30 fps * 9-11 sec)

    else:
        # Check if enough time passed
        if frameCount - fly_respawn_timer > fly_respawn_delay:
            fly_one = Fly()  # spawn new fly!

    player.display()
    print(score)


        


def keyPressed():
    player.move(keyCode)


"""

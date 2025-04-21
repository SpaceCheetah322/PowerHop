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

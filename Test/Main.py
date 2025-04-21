
play = False

def setup():
    size(800,600)
    background(180,200,255)
    img = loadImage("powerHopLogo.png")

def draw():
    if play:
        playScreen()
    else:
        print("working")
        startScreen()
        
def startScreen():
    background(120,170,255)
    print("here")
    image(img, 250, 300, img.width*9, img.height*9)
    print("point")
    fill(0)
    print("text")
    text("Welcome to PowerHop",400,200)
    text("Press any key to start",400,250)
    
def playScreen():
    background(0)

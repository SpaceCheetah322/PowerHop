img = None
f = None
play = False  # Added as global
global crr
crr = loadImage("Car.png")  


''' THIS IS THE CODE FOR THE GAME BOARD:
background(255)  # Set the background color to white
    # Draw a rectangle at position (x,y,width,height)
    #street grey
    fill(107, 103, 110)
    rect(0, 320, 400, 40)
    rect(0, 240, 400, 40)
    #water blue
    fill(85, 153, 242)
    rect(0, 0, 400, 200)
    #grass green
    fill(16, 125, 45)
    rect(0, 360, 400, 40)
    rect(0, 280, 400, 40)
    rect(0, 200, 400, 40)
    #safe goals level ended
    rect(0, 0, 50, 40)
    rect(90, 0, 50, 40)
    rect(180, 0, 50, 40)
    rect(270, 0, 50, 40)
    rect(360, 0, 50, 40)
    #yellow dashes
    fill(232, 229, 30)
    rect(0,340,30,5)
    rect(60,340,30,5)
    rect(120,340,30,5)
    rect(180,340,30,5)
    rect(240,340,30,5)
    rect(300,340,30,5)
    rect(360,340,30,5)
    #yellow dashes higher line
    rect(0,260,30,5)
    rect(60,260,30,5)
    rect(120,260,30,5)
    rect(180,260,30,5)
    rect(240,260,30,5)
    rect(300,260,30,5)
    rect(360,260,30,5)
'''

def setup():
    global img, f
    size(800, 600)
    img = loadImage("logo.png")
    background(100, 100, 255)
    f = createFont("Arial", 30)
    textFont(f, 30)
    textAlign(CENTER)

def draw():
    if play:
        background(255)
        image(crr, 200, 200, img.width*4, img.height*4)
    else:  
        background(120, 170, 255)
        image(img, 250, 300, img.width*9, img.height*9)
        fill(0)
        text("Welcome to PowerHop", 400, 200)
        text("Press any key to start", 400,250)

# Optional: Add key press to toggle
def keyPressed():
    global play
    play = not play

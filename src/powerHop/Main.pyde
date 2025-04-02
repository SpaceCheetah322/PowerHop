from Car import Car
img = None
f = None
play = False  # Added as global
c1 = Car(50,50)
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
        c1.display()
    else:  
        background(120, 170, 255)
        image(img, 250, 300, img.width*9, img.height*9)
        fill(0)
        text("Welcome to PowerHop", 400, 200)
        text("Press any key to start", 400,250)

# Optional: Add key press to toggle
def keyPressed():
    global play
    play = False

'''THIS CODE IS FOR THE GAME BOARD PUT IT INTO DRAW:
# Street grey
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
'''

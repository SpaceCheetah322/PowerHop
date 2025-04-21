# This code has the working UI but not the classes

img = None
f = None
play = False  # Added as global
car_img = None

''' THIS CODE IS FOR LOG TO SEND MULTIPLE LOGS AFTER ONE ANOTHER
log1 = Log(0, 200, direction="right", speed=2)
log2 = Log(-300, 200, direction="right", speed=2)
log2 = Log(-600, 200, direction="right", speed=2)
logs = [log1, log2, log3]

# Game loop
def game_loop():
    for log in logs:
        log.move()
        log.display()

set_interval(game_loop, 30)

'''
def setup():
    global img, car_img, f, car
    size(800, 600)
    img = loadImage("logo.png")
    background(100, 100, 255)
    f = createFont("Arial", 30)
    textFont(f, 30)
    textAlign(CENTER)
# Instantiate your existing Car class (adjust this as per your actual class)
    car = Car(width // 2 - 30, height * 0.82, car_img)  # Assuming Car takes x, y, and image

def draw():
    if play:
        playScreen()
    else:  
        startScreen()
        background(120, 170, 255)
        image(img, 250, 300, img.width*9, img.height*9)
        fill(0)
        text("Welcome to PowerHop", 400, 200)
        text("Press any key to start", 400,250)

# Optional: Add key press to toggle
def keyPressed():
    global play
    play = not play

def playScreen():
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
        
    car.display()
    
def startScreen():
    background(120, 170, 255)
    image(img, 250, 300, img.width*9, img.height*9)
    fill(0)
    text("Welcome to PowerHop", 400, 200)
    text("Press any key to start", 400,250)

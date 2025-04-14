img = None         # Logo image
f = None           # Font
play = False       # Controls the screen switch
car_img = None     # Car image
car = None         # Car object

def setup():
    global img, car_img, f, car
    size(800, 600)
    
    img = loadImage("logo.png")      # Logo for start screen
    car_img = loadImage("car.png")   # Car sprite/image
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

def startScreen():
    background(120, 170, 255)
    image(img, 250, 300, img.width * 9, img.height * 9)
    fill(0)
    text("Welcome to PowerHop", 400, 200)
    text("Press any key to start", 400, 250)

def keyPressed():
    global play
    play = True  # Switch to gameplay screen

def playScreen():
    background(255)

    # Street
    fill(107, 103, 110)
    rect(0, height * 0.8, width, height * 0.1)
    rect(0, height * 0.6, width, height * 0.1)

    # Water
    fill(85, 153, 242)
    rect(0, 0, width, height * 0.5)

    # Grass
    fill(16, 125, 45)
    rect(0, height * 0.9, width, height * 0.1)
    rect(0, height * 0.7, width, height * 0.1)
    rect(0, height * 0.5, width, height * 0.1)

    # Safe goal zones
    fill(16, 125, 45)
    rect(0, 0, width * 0.125, height * 0.1)
    rect(width * 0.225, 0, width * 0.125, height * 0.1)
    rect(width * 0.45, 0, width * 0.125, height * 0.1)
    rect(width * 0.675, 0, width * 0.125, height * 0.1)
    rect(width * 0.9, 0, width * 0.125, height * 0.1)

    # Yellow dashes on both streets
    fill(232, 229, 30)
    dash_width = width * 0.075
    for i in range(7):
        rect(i * width * 0.15, height * 0.85, dash_width, 5)
        rect(i * width * 0.15, height * 0.65, dash_width, 5)

    # Draw the car
    car.display()  # Or car.show(), depending on your Car class
''''
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
        #c1.display()
    else:  
        c1.display(self)
        background(120, 170, 255)
        image(img, 250, 300, img.width*9, img.height*9)
        fill(0)
        text("Welcome to PowerHop", 400, 200)
        text("Press any key to start", 400,250)

# Optional: Add key press to toggle
def keyPressed():
    global play
    play = False

'"from Car import Car

img = None
f = None
play = False
c1 = Car(50, 50)

def setup():
    global img, f
    size(800, 600)
    img = loadImage("logo.png")  # Ensure this is in your "data/" folder
    f = createFont("Arial", 30)
    textFont(f)
    textAlign(CENTER)

def draw():
    global play
    background(120, 170, 255)

    if not play:
        if img is not None:
            image(img, 250, 300, img.width * 0.5, img.height * 0.5)  # Adjust scale as needed

        fill(0)
        text("Welcome to PowerHop", width / 2, 200)
        text("Press any key to start", width / 2, 250)
    else:
        background(255)  # Blank white screen when key is pressed
        # You can also draw game elements here later
        # c1.display()  <-- maybe put the car here later

def keyPressed():
    global play
    play = True  """"

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

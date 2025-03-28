from car import Car

img = None

def setup():
    global img
    img = loadImage("logo.png") 
    size(800, 600) 
    background(100,100,255)
    global f
    f = createFont("Arial",30)
    textFont(f,30)
    textAlign(CENTER)
    
    

def draw():
    background(120,170,255)
    image(img, 250,300, img.width*9, img.height*9)
    fill(0)
    text("Welcome to PowerHop",400,200)
    



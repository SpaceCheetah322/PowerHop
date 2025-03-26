#Ava

"""
import pygame

from player import Player  # Import the Player class from player.py
from car import Car        # Import the Car class from car.py
from log import Log        # Import the Log class from log.py
from pow import Pow        # Import the Pow class from pow.py
from fly import Fly        # Import the Fly class from fly.py

# Initialize Pygame
pygame.init()

# Define screen dimensions and create game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Frogger Game")

# Game start function
def startGame():
    # Initialize objects
    player = Player(100, 100, 5, 3, "player.png")  # Example player
    cars = [Car(200, 200, 3, "right", "car.png")]  # Example cars
    logs = [Log(100, 300, 2, 100, "log.png")]  # Example logs
    powerups = [Pow(150, 150, "speed_boost", "pow.png")]  # Example powerups
    fly = Fly("fly.png")  # Example fly object

    running = True
    while running:
        screen.fill((255, 255, 255))  # Clear screen

        # Update and check game objects
        for car in cars:
            car.update()  # Update cars
            car.checkCol(player)  # Check car collision with player

        for log in logs:
            log.move()  # Move logs
            log.checkCol()  # Check log collision with player

        for powerup in powerups:
            powerup.checkCol(player)  # Check power-up collision
            powerup.applyEffect(player)  # Apply power-up effect if collected

        fly.checkCol(player)  # Check if player collects fly


        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

"""
#how to create window



#make text





img = None

def setup():
    global img
    img = loadImage("hopLogo.JPEG") 
    size(800, 600) 

def draw():
    background(255)
    image(img, 90,80, img.width*3, img.height*3)
    

"""
import time #Timer/Stopwatch?
play = True #Controls if app is running
game = False #Controls if game is running

print("Welcome to <INSERT NAME HERE> !") #Intro Message
# if (mouse_click)
#   CLEAR SCREEN
#   game = True #Game start

print ("Arrow Keys or WASD to move.") #Instructions
print ("Avoid cars, don't fall into the water.")
print ("Collect flies and powerups for benefits.")
print ("Reach the end before the timer runs out and without expending all your lives.")
print ("Enjoy!")
time.sleep(5)
# CLEAR SCREEN

if (game = True and play = True):
    # GAME LOGIC
    game = False #Shuts off gameplay

print ("Game Over") #End Screen
print ("Score: " + score)

if (replay_Pressed = True):
  game = True #Rerun
elif (quit_Pressed = True):
  play = False #End Program

"""

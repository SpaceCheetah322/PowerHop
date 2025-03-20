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
# Main loop
play = True
while play:
    print("Welcome to PowerHop")
    play = False

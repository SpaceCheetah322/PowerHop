class Player:
    def __init__(self, x, y, speed, lives, image_path):
        self.x = x
        self.y = y
        self.speed = 20   # May Break
        self.lives = lives
        self.image = image_path  # Placeholder for the image

    def move(self):
        # Movement logic using pygame
        if keys[pygame.K_LEFT]:  # Left arrow key or 'A'
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:  # Right arrow key or 'D'
            self.x += self.speed
        if keys[pygame.K_UP]:  # Up arrow key or 'W'
            self.y -= self.speed
        if keys[pygame.K_DOWN]:  # Down arrow key or 'S'
            self.y += self.speed

    def checkCol(self, obj):
        pass  # Logic for checking collision with another object

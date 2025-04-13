class Player:
    def __init__(self, x, y, speed, lives, image_path):
        self.x = x
        self.y = y
        self.speed = 20   #needs fine tuning
        self.lives = lives
        self.image = image_path

    def move(self, keys):
    if keys[pygame.K_LEFT]:
        self.x -= self.speed
    if keys[pygame.K_RIGHT]:
        self.x += self.speed
    if keys[pygame.K_UP]:
        self.y -= self.speed
    if keys[pygame.K_DOWN]:
        self.y += self.speed

    def checkCol(self, obj):
        pass

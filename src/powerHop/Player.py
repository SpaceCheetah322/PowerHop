import pygame

class Player:
    def __init__(self, x, y, speed, lives, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.lives = lives
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed

        self.rect.topleft = (self.x, self.y)

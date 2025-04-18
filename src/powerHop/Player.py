import pygame

class Player:
    def __init__(self, x, y, speed, lives, image):
        self.x = x
        self.y = y
        self.speed = speed = 40 #Fine tuning needed
        self.lives = lives
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                self.x -= self.speed
            if event.key in [pygame.K_RIGHT, pygame.K_d]:
                self.x += self.speed
            if event.key in [pygame.K_UP, pygame.K_w]:
                self.y -= self.speed
            if event.key in [pygame.K_DOWN, pygame.K_s]:
                self.y += self.speed

            self.rect.topleft = (self.x, self.y)

class Powerup:
    def __init__(self, x, y, effect, image_path):
        self.x = x
        self.y = y
        self.effect = effect  # The effect of the power-up (e.g., speed boost)
        self.image = image_path  # Placeholder for the image

    def applyEffect(self, player):
        pass  # Logic for applying the power-up effect to the player

    def checkCol(self, player):
        pass  # Logic for checking collision with the player

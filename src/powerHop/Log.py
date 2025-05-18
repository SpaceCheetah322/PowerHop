class Log:
    def __init__(self, x, y, direction="right", speed=2):
        self.x = x
        self.start_x = x
        self.y = y
        self.direction = direction
        self.speed = speed

        self.image = loadImage("Log.png")
        self.scale = 1.5  # scale image

        self.width = self.image.width * self.scale
        self.height = self.image.height * self.scale

    def move(self):
        cycle = 800 + self.width   # total distance a log should travel for each loop

        if self.direction == "right":
            self.x += self.speed
            if self.x > 800:
                # move back by exactly "cycle" pixels
                self.x -= cycle
        
        elif self.direction == "left":
            self.x -= self.speed
            if self.x + self.width < 0:
                # move forward by exactly "cycle" pixels
                self.x += cycle


    def display(self):
        imageMode(CORNER)
        image(self.image, self.x, self.y, self.width, self.height)
        
        
    def check_collision(self, frog):              #Defining the borders of the image
        left = max(self.x, frog.x)
        right = min(self.x + self.width, frog.x + frog.width)
        top = max(self.y, frog.y)
        bottom = min(self.y + self.height, frog.y + frog.height)

        if left >= right or top >= bottom:
            return False  # no overlap

        for px in range(int(left), int(right)):     #Checking pixel overlaps while ignoring scale
            for py in range(int(top), int(bottom)):
                log_img_x = int((px - self.x) / self.scale)
                log_img_y = int((py - self.y) / self.scale)
                frog_img_x = int((px - frog.x) / frog.scale)
                frog_img_y = int((py - frog.y) / frog.scale)

                if (0 <= log_img_x < self.image.width and
                    0 <= log_img_y < self.image.height and
                    0 <= frog_img_x < frog.img.width and
                    0 <= frog_img_y < frog.img.height):

                    log_pixel = self.image.get(log_img_x, log_img_y)
                    frog_pixel = frog.img.get(frog_img_x, frog_img_y)

                    # If both pixels are not transparent collision detected
                    if alpha(log_pixel) > 10 and alpha(frog_pixel) > 10:
                        return True

        return False

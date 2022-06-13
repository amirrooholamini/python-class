import arcade

class Bird(arcade.Sprite):
    def __init__(self):
        super().__init__('resources/bird.png')
        self.center_x = 1000
        self.center_y = 90
        self.speed = 4
        
    def move(self):
        self.center_x -= self.speed

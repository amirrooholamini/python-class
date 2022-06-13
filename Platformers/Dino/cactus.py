import arcade

class Cactus(arcade.Sprite):
    def __init__(self):
        super().__init__('resources/cactus.png')
        self.center_x = 1000
        self.center_y = 50
        self.speed = 4
        
    def move(self):
        self.center_x -= self.speed

import arcade
from time import time
class Dino(arcade.Sprite):
    def __init__(self, stand_up):
        
        super().__init__()
        self.walk_1 = arcade.load_texture('resources/dino-walk-0.png')
        self.walk_2 = arcade.load_texture('resources/dino-walk-1.png')

        self.down_1 = arcade.load_texture('resources/dino-down-0.png')
        self.down_2 = arcade.load_texture('resources/dino-down-1.png')

        self.stand_up = stand_up
        if(self.stand_up):
            self.texture = self.walk_1
        else:
            self.texture = self.down_1
        self.t = time()
        self.scale = 0.25
        self.speed = 7

        self.center_x = 50
        self.center_y = 50

        self.walk = True
        

    def update_animation(self):
        if(time() - self.t > 0.2 and self.walk):
            if(self.stand_up):
                if(self.texture == self.walk_1):
                    self.texture = self.walk_2
                else:
                    self.texture = self.walk_1
            else:
                if(self.texture == self.down_1):
                    self.texture = self.down_2
                else:
                    self.texture = self.down_1

            
            self.t = time()
    def sit_down(self):
        self.stand_up = False
    
    def stand_me_up(self):
        self.stand_up = True
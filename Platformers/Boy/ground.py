import arcade

class Ground(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__()
        self.texture = arcade.load_texture("resources/ground.png")
        self.center_x = center_x
        self.center_y = center_y
        

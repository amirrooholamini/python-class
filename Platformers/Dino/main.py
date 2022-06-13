import arcade
from dino import Dino
from ground import Ground
from cactus import Cactus
from bird import Bird
from time import time
from random import random

class Game(arcade.Window):
    def __init__(self):

        self.pause = False
        self.w = 700
        self.h = 200
        super().__init__(self.w, self.h, 'Dino')
        arcade.set_background_color(arcade.color.DARK_CYAN)
        self.me = Dino()
        self.st = time()

        self.grounds = arcade.SpriteList()
        for i in range(0,self.w + 50, 50):
            self.grounds.append(Ground(i,0))
        
        self.my_physics_engin = arcade.PhysicsEnginePlatformer(self.me, self.grounds, 0.3)
        self.cactuses = arcade.SpriteList()

    def on_draw(self):
        arcade.start_render()
        self.me.update_animation()
        self.me.draw()
        for ground in self.grounds:
            ground.draw()
        
        for cactus in self.cactuses:
            cactus.draw()
    def on_update(self, delta_time: float):
        self.my_physics_engin.update()
        if(time() - self.st > 2 and not self.pause):
            if(random() > 0.5):
                item = Cactus()
            else:
                item = Bird()
            self.cactuses.append(item)
            self.st = time()
        if not self.pause:
            for cactus in self.cactuses:
                cactus.move()
    def on_key_press(self, symbol: int, modifiers: int):
        if(symbol == arcade.key.SPACE and not self.pause and self.my_physics_engin.can_jump()):
            self.me.change_y = self.me.speed
        elif(symbol == arcade.key.ENTER):
            self.pause = not self.pause
            if(self.pause):
                self.me.walk = False
            else:
                self.me.walk = True
        elif(symbol == arcade.key.DOWN):
            self.me.sit_down()
    def on_key_release(self, symbol: int, modifiers: int):
        if(symbol == arcade.key.SPACE):
            self.me.change_y = 0
        elif(symbol == arcade.key.DOWN):
            self.me.stand_me_up()
game = Game()
arcade.run()


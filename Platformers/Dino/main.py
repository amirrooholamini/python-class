import arcade
from dino import Dino
from ground import Ground
from cactus import Cactus
from bird import Bird
from time import time
from random import random

class Game(arcade.Window):
    def __init__(self):
        self.max_score = 0
        self.jump_music = arcade.load_sound(':resources:sounds/phaseJump1.ogg')
        self.collision_music = arcade.load_sound(':resources:sounds/hit3.wav')
        self.pause = False
        self.game_over = False
        self.score = 0
        self.w = 700
        self.h = 200
        super().__init__(self.w, self.h, 'Dino')
        arcade.set_background_color(arcade.color.DARK_CYAN)
        self.me = Dino(stand_up=True)
        self.me_sit_down = Dino(stand_up=False)
        self.st = time()
        

        self.grounds = arcade.SpriteList()
        for i in range(0,self.w + 50, 50):
            self.grounds.append(Ground(i,0))
        
        self.my_physics_engin = arcade.PhysicsEnginePlatformer(self.me, self.grounds, 0.3)
        self.my_physics_engin2 = arcade.PhysicsEnginePlatformer(self.me_sit_down, self.grounds, 0.3)
        self.enemies = arcade.SpriteList()

    def on_draw(self):
        arcade.start_render()
        if(self.me.stand_up):
            self.me.update_animation()
            self.me.draw()
        else:
            self.me_sit_down.update_animation()
            self.me_sit_down.draw()
        for ground in self.grounds:
            ground.draw()
        
        for enemy in self.enemies:
            enemy.draw()
        arcade.draw_text(str(self.score) + "/" + str(self.max_score), self.w - 100 ,self.h - 20, arcade.csscolor.WHITE, 12)
    def on_update(self, delta_time: float):
        if(self.score % 200 == 0):
            div = self.score // 200
            if(div % 2 ==0):
                arcade.set_background_color(arcade.color.DARK_CYAN)
            else:
                arcade.set_background_color(arcade.color.BLACK)
        if(self.score == 0):
            self.start_game = time()
        self.my_physics_engin.update()
        self.my_physics_engin2.update()
        if(not self.game_over):
            self.score = max(int((time() - self.start_game)*10),1)
        if(time() - self.st > 2 and not self.pause):
            if(random() > 0.5 or self.score < 200):
                item = Cactus()
            else:
                item = Bird()
            
            self.enemies.append(item)
            self.st = time()
        if not self.pause:
            for enemy in self.enemies:
                enemy.move()
                enemy.speed = (self.score // 20) + 4

        if(not self.game_over):
            for item in self.enemies:
                if(self.me.stand_up and arcade.check_for_collision(self.me, item)):
                    self.pause = True
                    self.game_over = True
                    self.me.walk = False
                    self.me_sit_down.walk = False
                    self.collision_music.play()
                elif(not self.me.stand_up and arcade.check_for_collision(self.me_sit_down, item)):
                    self.pause = True
                    self.game_over = True
                    self.me.walk = False
                    self.me_sit_down.walk = False
                    self.collision_music.play()

    def on_key_press(self, symbol: int, modifiers: int):
        if(symbol == arcade.key.UP and not self.pause and self.my_physics_engin.can_jump() and self.me.stand_up):
            self.me.change_y = self.me.speed
            self.jump_music.play()

        elif(symbol == arcade.key.ENTER):
            if(self.game_over):
                self.enemies.clear()
                self.max_score = max(self.max_score, self.score)
                self.score = 0
                self.game_over = False
            self.pause = not self.pause
            if(self.pause):
                self.me.walk = False
            else:
                self.me.walk = True

        elif(symbol == arcade.key.DOWN and self.my_physics_engin.can_jump()):
            self.me.sit_down()
    def on_key_release(self, symbol: int, modifiers: int):
        if(symbol == arcade.key.SPACE):
            self.me.change_y = 0
        elif(symbol == arcade.key.DOWN):
            self.me.stand_me_up()
game = Game()
arcade.run()


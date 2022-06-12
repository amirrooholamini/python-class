from time import time
import arcade
from player import Player
from enemy import Enemy
from ground import Ground

class Game(arcade.Window):
    def __init__(self):
        self.game_over = False
        self.w = 800
        self.h = 500
        self.gravity = 0.4
        self.st = time()
        self.background_image = arcade.load_texture('resources/background.png')
        super().__init__(self.w, self.h, 'Boy')
        self.me = Player()
        self.enemies = arcade.SpriteList()
        self.key = arcade.Sprite(':resources:images/items/keyBlue.png')
        self.key.width = self.key.height = 50
        self.key.center_x = 100
        self.key.center_y = 400

        self.lock = arcade.Sprite(':resources:images/tiles/lockRed.png')
        self.lock.width = self.lock.height = 30
        self.lock.center_x = 750
        self.lock.center_y = 75

        self.grounds = arcade.SpriteList()
        for i in range(500, 700, 50):
            self.grounds.append(Ground(i,200))

        for i in range(100, 300, 50):
            self.grounds.append(Ground(i,350))

        for i in range(25, self.w, 50):
            self.grounds.append(Ground(i,25))

        self.my_physics_engin = arcade.PhysicsEnginePlatformer(self.me, self.grounds, self.gravity)
        self.enemies_physics_engins = []

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.background_image)
        if(not self.game_over):
            self.me.draw()
            self.lock.draw()
            if(not self.me.has_key):
                self.key.draw()
            for ground in self.grounds:
                ground.draw()
            for enemy in self.enemies:
                enemy.draw()

            health_text = ""
            for h in range(self.me.health):
                health_text += "♥"
            arcade.draw_text(health_text, 10 ,10, arcade.csscolor.RED, 36)
        else:
            arcade.draw_text("Game Over", 10 ,self.h//2, arcade.color.RED, 40,width=self.w, align="center")

    def on_update(self, delta_time: float):
        self.my_physics_engin.update()
        et = time()
        if(et - self.st > 5):
            new_enemy = Enemy()
            self.enemies.append(new_enemy)
            self.enemies_physics_engins.append(arcade.PhysicsEnginePlatformer(new_enemy, self.grounds, self.gravity))
            self.st = et
        for enemy_engin in self.enemies_physics_engins:
            enemy_engin.update()
        self.me.update_animation()
        for enemy in self.enemies:
            enemy.update_animation()

        if(not self.me.has_key and arcade.check_for_collision(self.me, self.key)):
            self.me.has_key = True
        if(self.me.has_key and arcade.check_for_collision(self.me, self.lock)):
            print('lock opened')

        now = time()
        if(now - self.me.collision_time > 3 ):
            for enemy in self.enemies:
                if(arcade.check_for_collision(enemy, self.me)):
                    self.me.health -= 1
                    if(self.me.health == 0):
                        self.game_over = True
                    self.me.collision_time = time()


    def on_key_press(self, symbol: int, modifiers: int):
        if(symbol == arcade.key.RIGHT):
            self.me.change_x += self.me.speed_x
        elif(symbol == arcade.key.LEFT):
            self.me.change_x -= self.me.speed_x
        elif(symbol == arcade.key.UP and self.my_physics_engin.can_jump()):
            self.me.change_y += self.me.speed_y

    def on_key_release(self, symbol: int, modifiers: int):
        if(symbol == arcade.key.RIGHT or symbol == arcade.key.LEFT):
            self.me.change_x = 0
        elif(symbol == arcade.key.UP):
            self.me.change_y = 0

game = Game()
arcade.run()
        

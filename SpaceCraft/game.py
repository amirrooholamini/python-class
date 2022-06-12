import random
import time
import math
import arcade

class SpaceCraft(arcade.Sprite):
    fire_music = arcade.load_sound(':resources:sounds/hit2.wav')
    def __init__(self, game_width, game_height):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.width = 48
        self.hegiht = 48
        self.center_x = game_width // 2
        self.center_y = self.hegiht
        self.angle = 0
        self.speed = 0
        self.bullets = []

    def rotate(self):
        self.angle += self.speed
    
    def fire(self):
        self.bullets.append(Bullet(self.center_x,self.center_y,self.angle))
        SpaceCraft.fire_music.play()

class Enemy(arcade.Sprite):
    def __init__(self, game_width, game_height,size,speed):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.width = size
        self.height = size
        self.center_x = random.randint(0,game_width)
        self.center_y = game_height + 48
        self.angle = 180
        self.speed = speed

    def move(self):
        self.center_y -= self.speed

class Bullet(arcade.Sprite):
    def __init__(self, center_x, center_y, angle):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.speed = 8
        self.center_x = center_x
        self.center_y = center_y
        self.angle = angle
    
    def move(self):
        radian =  math.radians(self.angle)
        self.center_x -= self.speed * math.sin(radian)
        self.center_y += self.speed * math.cos(radian)

class Game(arcade.Window):
    enemy_times = [0.5,1,2,2.5,3,3.5]
    def __init__(self):
        self.collision_music = arcade.load_sound(':resources:sounds/hit3.wav')
        self.w=600
        self.h=500
        self.title="space craft"
        self.background_color = arcade.color.BLACK
        self.background_image = ":resources:images/backgrounds/stars.png"
        super().__init__(self.w,self.h,self.title)
        arcade.set_background_color(self.background_color)

        self.start_time = time.time()
        self.start_game = time.time()
        self.enemy_next_time = random.choice(Game.enemy_times)
        self.me = SpaceCraft(self.w, self.h)
        self.enemies = []
        self.score = 0
        self.health = 3
        self.continue_game = True
    def on_draw(self):
        arcade.start_render()
        if(self.continue_game):
            health_text = ""
            for h in range(self.health):
                health_text += "♥"
            arcade.draw_text(health_text, 10 ,10, arcade.csscolor.RED, 18)
            arcade.draw_text(str(self.score), self.width - 30 ,10, arcade.csscolor.WHITE, 18,200)
            arcade.draw_lrwh_rectangle_textured(0,0,self.w,self.h,arcade.load_texture(self.background_image))
            self.me.draw()
            for bullet in self.me.bullets:
                bullet.draw()
            for enemy in self.enemies:
                enemy.draw()
        else:
            arcade.draw_text("Game Over", 10 ,self.h//2, arcade.color.RED, 40,width=self.w, align="center")

    def on_update(self, delta_time: float):
        end_time = time.time()
        if(end_time - self.start_time > self.enemy_next_time):
            diff = time.time() - self.start_game
            
            speed = math.floor(diff/20) + 2
            self.enemies.append(Enemy(self.w,self.h,random.choice([48,32]),speed))
            self.start_time = end_time
            self.enemy_next_time = random.choice(Game.enemy_times)
        self.me.rotate()

        for bullet in self.me.bullets:
            bullet.move()
            if(bullet.center_x > self.w + 100 or bullet.center_x < -100 or bullet.center_y > self.h + 100 or bullet.center_y < -100):
                self.me.bullets.remove(bullet)

        for enemy in self.enemies:
            enemy.move()
            if(enemy.center_y < -20):
                self.enemies.remove(enemy)
                self.health -= 1
                if(self.health == 0):
                    self.continue_game = False
               
        
        for bullet in self.me.bullets:
            for enemy in self.enemies:
                if(arcade.check_for_collision(bullet, enemy)):
                    self.enemies.remove(enemy)
                    self.me.bullets.remove(bullet)
                    self.score += 1
                    self.collision_music.play()

    def on_key_press(self, symbol: int, modifiers: int):
        if(symbol == arcade.key.A):
            self.me.speed = 4
        elif(symbol == arcade.key.D):
            self.me.speed = -4

    def on_key_release(self, symbol: int, modifiers: int):
        if(symbol == arcade.key.A or symbol == arcade.key.D):
            self.me.speed = 0

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if(button == 1):
            self.me.fire()

game = Game()
arcade.run()
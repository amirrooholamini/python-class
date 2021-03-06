import arcade
from time import time
class Player(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()
        # self.texture = arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png')
        self.stand_left_textures=[arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png', mirrored=True)]
        self.stand_right_textures =[arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png')]

        self.walk_right_textures = [
            arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_walk0.png'),
            arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_walk1.png'),
            arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_walk2.png'),
            arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_walk3.png'),
            arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_walk4.png'),
            arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_walk5.png'),
            arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_walk6.png'),
            arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_walk7.png'),
        ]
        self.walk_left_textures = [
            arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_walk0.png', mirrored=True),
            arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_walk1.png', mirrored=True),
            arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_walk2.png', mirrored=True),
            arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_walk3.png', mirrored=True),
            arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_walk4.png', mirrored=True),
            arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_walk5.png', mirrored=True),
            arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_walk6.png', mirrored=True),
            arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_walk7.png', mirrored=True),
        ]
        self.center_x = 20
        self.center_y = 500
        self.speed_x = 4
        self.speed_y = 12

        self.has_key = False
        self.health = 3
        self.collision_time = time()

        
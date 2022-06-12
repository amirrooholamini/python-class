import random
import arcade
SCREEN_WIDTH = 500
SCREEN_HEIGH = 500

class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        self.color = arcade.color.RED
        self.radius = 8
        self.center_x = random.randint(0, SCREEN_WIDTH)
        self.center_y = random.randint(0, SCREEN_HEIGH)

    def draw(self):
        arcade.draw_circle_filled(
            self.center_x,
            self.center_y,
            self.radius,
            self.color
            )

class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        self.color = arcade.color.BLUE
        self.change_x = 0
        self.change_y = 0
        self.center_x = SCREEN_WIDTH//2
        self.center_y = SCREEN_HEIGH//2
        self.speed = 4
        self.score = 0
        self.body = []

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)
        for item in self.body:
            arcade.draw_rectangle_filled(item[0],item[1],self.width,self.height,arcade.color.GREEN)

    def move_left(self):
        self.change_x = -1
        self.change_y = 0
    def move_right(self):
        self.change_x = 1
        self.change_y = 0
    def move_up(self):
        self.change_x = 0
        self.change_y = 1
    def move_down(self):
        self.change_x = 0
        self.change_y = -1

    def move(self):

        self.body.append([self.center_x,self.center_y])
        if(len(self.body)> self.score):
            del self.body[0]

        if(self.change_x > 0):
            self.center_x += self.speed
        elif(self.change_x < 0):
            self.center_x -= self.speed
        if(self.change_y > 0):
            self.center_y += self.speed
        elif(self.change_y < 0):
            self.center_y -= self.speed
        
        if(self.center_x > SCREEN_WIDTH):
            self.center_x = 0
        elif(self.center_x < 0):
            self.center_x = SCREEN_WIDTH

        if(self.center_y > SCREEN_HEIGH):
            self.center_y = 0
        elif(self.center_y < 0):
            self.center_y = SCREEN_HEIGH

    def eat(self):
        self.score += 1


class Game(arcade.Window):
    def __init__(self):
        super().__init__(
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGH,
            title="snake"
        )
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake()
        self.apple = Apple()

    def on_draw(self):
        arcade.start_render()
        
        self.snake.draw()
        self.apple.draw()

    # منطق بازی در این متد است
    def on_update(self, delta_time: float):
        self.snake.move()
        if(arcade.check_for_collision(self.snake, self.apple)):
            self.snake.eat()
            self.apple = Apple()

    def on_key_press(self, symbol: int, modifiers: int):
        if(symbol == arcade.key.LEFT):
            self.snake.move_left()
        elif(symbol == arcade.key.RIGHT):
            self.snake.move_right()
        elif(symbol == arcade.key.UP):
            self.snake.move_up()
        elif(symbol == arcade.key.DOWN):
            self.snake.move_down()


game = Game()
arcade.run()

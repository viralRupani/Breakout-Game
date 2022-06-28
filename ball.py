import turtle
import random


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('cyan')
        self.goto(random.randint(-300, 300), -220)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # print(f'x={self.xcor()}')
        # print(f'y={self.ycor()}')

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def respawn(self):
        self.goto(random.randint(-280, 280), -220)
        self.bounce_x()
        self.bounce_y()

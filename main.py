from turtle import Screen
from paddle import *

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
paddle = Paddle()

screen.listen()
screen.onkey(paddle.go_left, 'Left')
screen.onkey(paddle.go_right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
screen.exitonclick()

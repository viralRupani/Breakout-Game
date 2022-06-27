from turtle import Screen
from paddle import Paddle
from ball import Ball
from walls import Walls
import time

WALL_COLOR = ['green', 'yellow', 'orange', 'red']

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')

paddle = Paddle()
ball = Ball()

screen.listen()
screen.onkey(paddle.go_left, 'Left')
screen.onkey(paddle.go_right, 'Right')

wall_list = []
x_pos = -320
y_pos = 0
for row in range(4):
    for col in range(15):
        walls = Walls()
        wall_list.append(walls)
        walls.color(WALL_COLOR[row])
        walls.goto(x_pos, y_pos)
        x_pos += 45
    y_pos += 20
    x_pos = -320

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    if ball.xcor() > 300 or ball.xcor() < -300:
        ball.bounce_x()
    elif ball.ycor() > 280:
        ball.bounce_y()
    elif ball.ycor() < -300:
        ball.respawn()
    elif ball.distance(paddle) < 30:
        ball.bounce_y()

    for wall in wall_list:
        if ball.distance(wall) < 30:
            ball.bounce_y()
            wall.reset()
screen.exitonclick()

from turtle import Screen
from paddle import Paddle
from ball import Ball
from walls import Walls
from scoreboard import ScoreBoard
import time

WALL_COLOR = ['green', 'yellow', 'orange', 'red']

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')

paddle = Paddle()
ball = Ball()
scoreboard = ScoreBoard()

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
    for wall in wall_list:
        if ball.distance(wall) < 30:
            ball.bounce_y()
            wall.reset()

    if ball.xcor() > 300 or ball.xcor() < -300:
        ball.bounce_x()
    elif ball.ycor() > 280:
        ball.bounce_y()
    elif ball.ycor() < -300:
        ball.respawn()
        scoreboard.life_count -= 1
        scoreboard.update()
    elif ball.distance(paddle) < 30:
        ball.bounce_y()

    if scoreboard.life_count < 0:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()

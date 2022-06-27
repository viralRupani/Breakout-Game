from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')

paddle = Paddle()
ball = Ball()

screen.listen()
screen.onkey(paddle.go_left, 'Left')
screen.onkey(paddle.go_right, 'Right')

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
    elif ball.distance(paddle) < 20:
        ball.bounce_y()

screen.exitonclick()

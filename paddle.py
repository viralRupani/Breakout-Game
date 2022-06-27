import turtle


class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color('white')
        self.penup()
        self.goto((0, -250))

    def go_left(self):
        if self.xcor() != -320:
            new_x_cor = self.xcor() - 20
            self.goto(new_x_cor, self.ycor())

    def go_right(self):
        if self.xcor() != 300:
            new_x_cor = self.xcor() + 20
            self.goto(new_x_cor, self.ycor())

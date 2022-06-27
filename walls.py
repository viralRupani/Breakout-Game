import turtle


class Walls(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(1, 2)


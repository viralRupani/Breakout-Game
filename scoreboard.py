import turtle


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 250)
        self.life_count = 5
        self.update()

    def update(self):
        self.clear()
        self.write(f'Remaining Balls: {self.life_count}', align='center',  font=('Arial', 12, 'bold'))

    def game_over(self):
        self.clear()
        self.goto(0, -100)
        self.write(f'Game Over', align='center', font=('Arial', 25, 'bold'))

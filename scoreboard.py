from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write('Score: 0  Lives: 5', align='center', font=('Courier', 24, 'normal'))

from turtle import Turtle


class Ball(Turtle):
    def __init__(self, paddle):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, -240)
        self.dx = 10
        self.dy = 10
        self.paddle = paddle
        # self.speed(9)

    def move(self):
        self.goto(self.xcor()+self.dx, self.ycor()+self.dy)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def reset(self):
        self.goto(0, 0)






from turtle import Turtle


class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(1, 3)
        self.penup()
        self.color('white')



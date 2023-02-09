from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.shape('square')
        self.shapesize(1, 8)
        self.color('#00B4D4')
        self.penup()
        self.goto(0, -250)
        self.my_screen = screen
        self.onmove(self.my_screen, self.goto_handler)

    def onmove(self, screen, fun, add=None):
        # """
        # Bind fun to mouse-motion event on screen.
        #
        # Arguments:
        # screen -- the singular screen instance
        # fun  -- a function with two arguments, the coordinates
        #     of the mouse cursor on the canvas.
        #
        # Example:
        #
        # >>> onmove(screen, lambda x, y: print(x, y))
        # >>> # Subsequently moving the cursor on the screen will
        # >>> # print the cursor position to the console
        # """

        if fun is None:
            screen.cv.unbind('<Motion>')
        else:
            def eventfun(event):
                fun(screen.cv.canvasx(event.x) / screen.xscale, -screen.cv.canvasy(event.y) / screen.yscale)

            screen.cv.bind('<Motion>', eventfun, add)

    def goto_handler(self, x, y):
        self.onmove(self.my_screen, None)  # avoid overlapping events
        # turtle.setheading(turtle.towards(x, -250))
        if 310 >= x >= -320:
            self.goto(x, -250)
        self.onmove(self.my_screen, self.goto_handler)

from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cordinate, y_cordinate):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=x_cordinate, y=y_cordinate)
        self.score = 0

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
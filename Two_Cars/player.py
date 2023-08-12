from turtle import Turtle

MOVE_DISTANCE = 10


class Player1(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(x=-110, y=-210)
        self.setheading(90)

    def change(self):
        if self.xcor() == -110:
            self.goto(x=-40, y=-210)
        else:
            self.goto(x=-110, y=-210)


class Player2(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(x=110, y=-210)
        self.setheading(90)

    def change(self):
        if self.xcor() == 110:
            self.goto(x=40, y=-210)
        else:
            self.goto(x=110, y=-210)

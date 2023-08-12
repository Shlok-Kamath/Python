from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.xmove = 10
        self.ymove = 10

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)

    def bounce(self):
        self.ymove*=-1

    def turn_around(self):
        self.xmove*=-1

    def restart(self):
        self.goto(0,0)
        self.bounce()
        self.turn_around()

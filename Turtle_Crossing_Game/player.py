from turtle import Turtle

STARTING_PLACE = (0, -230)
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_PLACE)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def restart(self):
        self.goto(STARTING_PLACE)
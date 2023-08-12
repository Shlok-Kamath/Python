from turtle import Turtle
from random import randint
import time

game_is_on = True


class Car:
    def __init__(self):
        self.all_cars = []
        self.forward_distance = 5

    def create_car(self):

        random_chance = randint(1, 6)

        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color((randint(0, 255), randint(0, 255), randint(0, 255)))
            new_car.goto(300, randint(-180, 180))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_cars(self):
        for c in self.all_cars:
            c.forward(self.forward_distance)

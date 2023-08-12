from turtle import Screen
from scoreboard import Scoreboard
from car import Car
from player import Player
import time

game_is_on = True


screen = Screen()
screen.setup(width=600, height=500)
screen.listen()
screen.colormode(255)

scoreboard = Scoreboard()
screen.tracer(0)

player = Player()

screen.onkeypress(player.go_up, "Up")

car = Car()
while game_is_on:
    time.sleep(0.05)
    car.create_car()
    car.move_cars()
    screen.update()

    for c in car.all_cars:
        if player.distance(c) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 200:
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        player.restart()
        car.forward_distance+=5

screen.exitonclick()
import time
from turtle import Screen
from scoreboard import Scoreboard
from player import Player1, Player2

is_game_on = True

screen = Screen()
screen.setup(width=300, height=500)
screen.listen()
screen.tracer(0)

scoreboard = Scoreboard()

player1 = Player1()
player2 = Player2()

screen.update()

screen.onkey(player1.change, "a")
screen.onkey(player2.change, "s")

while is_game_on:
    time.sleep(0.05)
    screen.update()

screen.exitonclick()

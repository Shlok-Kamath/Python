from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

SLEEP_TIME = 0.1

game_is_on = True

scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=800, height=600)

screen.tracer(0)

l_paddle = Paddle(350,0)
r_paddle = Paddle(-350,0)

ball = Ball()

screen.listen()

screen.onkeypress(l_paddle.go_up,"Up")
screen.onkeypress(l_paddle.go_down,"Down")

screen.onkeypress(r_paddle.go_up,"w")
screen.onkeypress(r_paddle.go_down,"s")

while game_is_on:
    time.sleep(SLEEP_TIME)
    ball.move()
    screen.update()

    if ball.ycor()>280 or ball.ycor() <-280:
        ball.bounce()

    if (l_paddle.distance(ball) < 50 and ball.xcor() > 330) or (r_paddle.distance(ball) < 50 and ball.xcor() < -330):
        ball.turn_around()
        SLEEP_TIME*=0.9
    elif ball.xcor() > 400:
        ball.restart()
        scoreboard.r_point()
        SLEEP_TIME = 0.1
    elif ball.xcor() < -400:
        ball.restart()
        scoreboard.l_point()
        SLEEP_TIME = 0.1




screen.exitonclick()
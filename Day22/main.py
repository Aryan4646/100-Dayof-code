from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height =600, width = 800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

score = Scoreboard()

c_ball = Ball()
r_paddle = Paddle((375,0))
l_paddle = Paddle((-375,0))


screen.listen()
screen.onkey(r_paddle.Up,"Up")
screen.onkey(r_paddle.Down,"Down")
screen.onkey(l_paddle.Up,"w")
screen.onkey(l_paddle.Down,"s")

game_is_on = True

while game_is_on:
    time.sleep(c_ball.movespeed)
    screen.update()
    c_ball.move()
#     Detect collison with top and bottom walls
    if c_ball.ycor() > 280 or c_ball.ycor() < -280 :
        c_ball.bounce()
#   detect collision with r paddle
    if c_ball.distance(r_paddle) <50 and c_ball.xcor() > 340 or c_ball.distance(l_paddle) < 50 and c_ball.xcor() < -340:
        c_ball.paddle_bounce()

    # R paddle collison
    if c_ball.xcor() > 380:
        c_ball.resetpositon()
        score.lpoint()
    # L paddle collision
    if c_ball.xcor() < -380:
        c_ball.resetpositon()
        score.rpoint()

screen.exitonclick()
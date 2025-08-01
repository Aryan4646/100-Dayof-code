from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(height =600, width = 800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

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
    time.sleep(0.1)
    screen.update()
    c_ball.move()

#     Detect collison with top and bottom walls
    if c_ball.ycor() > 290 or c_ball.ycor() < -290 :
        c_ball.bounce()


screen.exitonclick()
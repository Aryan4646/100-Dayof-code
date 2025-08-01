from turtle import Turtle, Screen
import time
from snake import Snake
screen = Screen()
screen.setup(height= 600, width = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.snake_up,"Up")
screen.onkey(snake.snake_down,"Down")
screen.onkey(snake.snake_left,"Left")
screen.onkey(snake.snake_right,"Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()



screen.exitonclick()
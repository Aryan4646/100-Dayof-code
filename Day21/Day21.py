from turtle import Screen
import time
from snake1 import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(height= 600, width = 600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

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

    if snake.head.distance(food) < 15:
        food.refresh()
        score.refres()
        snake.extend()

#     Detect collison with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_on = False
        score.game_over()
# Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head():
            pass
        elif snake.head.distance(segment) <10:
            game_on = False
            score.game_over()
screen.exitonclick()
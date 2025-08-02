import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

playerr = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()

screen.onkey(playerr.move,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_car()
    # Detect collison
    for car in car_manager.cars:
        if car.distance(playerr) < 20 :
            game_is_on = False
            score.game_over()
#     detect succefull crossing
    if playerr.finish_line():
        playerr.goto_start()
        car_manager.speed_increase()
        score.increase()

screen.exitonclick()
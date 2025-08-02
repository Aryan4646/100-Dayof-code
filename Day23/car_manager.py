from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.cars = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        rand_chance = random.randint(1,6)
        if rand_chance ==1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid= 1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(a = -250,b = 250)
            new_car.goto(300,random_y)
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.backward(self.carspeed)

    def speed_increase(self):
        self.carspeed += MOVE_INCREMENT

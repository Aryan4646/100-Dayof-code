from turtle import Turtle, Screen
import random
timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
timmy.color("red")

# Draw a square
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# Draw a dashed line
# for i in range(20):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

# generate shapes triangle square pentagon hexagon heptagon octagon nonagon decagon
# colors = ["green","hotpink","ivory4","khaki1","LightBlue1","gold","lightgreen"]
# side = 3
# print(timmy)
# while side <= 10:
#     for i in range(side):
#         timmy.pensize(5)
#         angle = 360/side
#         timmy.forward(100)
#         timmy.right(angle)
#     side += 1
#     timmy.color(f"{random.choice(colors)}")

# Generate a random walk

screen.exitonclick()

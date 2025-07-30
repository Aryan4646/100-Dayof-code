from turtle import Turtle, Screen
import colorgram
import random
import turtle
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
# colors = [
#     "red", "blue", "green", "yellow", "orange", "purple", "hotpink", "cyan",
#     "magenta", "turquoise", "ivory4", "khaki1", "LightBlue1", "gold", "lightgreen",
#     "salmon", "plum", "wheat", "slategray", "navy", "lime", "chocolate", "orchid"
# ]

# directions = [0, 90, 180 ,270]
# turtle.colormode(255)
#
# def random_Color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     r_color = (r, g, b)
#     return r_color
#
# def random_walk(x):
#     timmy.speed("fastest")
#     timmy.color(random_Color())
#     timmy.pensize(15)
#     timmy.setheading(x)
#     timmy.forward(30)
#
# for i in range(300):
#     x = random.choice(directions)
#     random_walk(x)

# Make a spirograph

#
# turtle.colormode(255)
# def random_Color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     r_color = (r, g, b)
#     return r_color
#
#
# for i in range(1000):
#     timmy.speed("fastest")
#     timmy.color(random_Color())
#     timmy.circle(100)
#     current_heading = timmy.heading()
#     timmy.setheading(current_heading+5)

# colors = colorgram.extract('download.jpeg',9)
# rgb_col = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_col.append(new_color)
# print(rgb_col)


# Painting
turtle.colormode(255)
color_list = [(235, 234, 232), (237, 238, 240), (243, 235, 240), (230, 241, 236), (166, 96, 23), (227, 137, 74), (15, 32, 55), (237, 78, 95), (45, 106, 147)]


timmy.setheading(225)
timmy.penup()
timmy.forward(50)
timmy.setheading(0)
timmy.pendown()
for j in range(10):
    timmy.hideturtle()
    timmy.penup()
    for i in range(10):
        timmy.dot(20,random.choice(color_list))
        timmy.forward(30)
    timmy.left(90)
    timmy.forward(30)
    timmy.left(90)
    timmy.forward(300)
    timmy.setheading(0)



screen.exitonclick()

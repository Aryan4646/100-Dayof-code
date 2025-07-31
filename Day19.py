from turtle import Turtle, Screen
import random

screen = Screen()

# timmy = Turtle()
# def move_forwards():
#     timmy.forward(10)
#     timmy.left(90)
#     timmy.forward(50)
#
# screen.listen()
# screen.onkey(fun=move_forwards, key = "space" )

# etch a sketch app

# def forwardd():
#     timmy.forward(10)
# def backwardd():
#     timmy.backward(10)
# def c_clock():
#     timmy.left(10)
# def clockk():
#     timmy.right(10)
# def clearr():
#     timmy.reset()
#
# screen.listen()
# screen.onkey(fun = forwardd, key = "W")
# screen.onkey(fun= backwardd, key = "S")
# screen.onkey(fun = c_clock, key = "A")
# screen.onkey(fun = clockk, key = "D")
# screen.onkey(fun = clearr, key = "P" )

# Turtle race
is_race_on = False
screen.setup(500,400)
user_bet = screen.textinput("Bet for turtle","Which Turtle will Win the race? Enter a color: ")
print(user_bet)
colors = ["red","orange", "yellow","green", "blue", "purple"]
y_pos = [-150, -100, -50, 0, 50, 100]
all_turtle =[]

for i in range(0,6):
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.color(colors[i])
    timmy.penup()
    timmy.goto(x= -235, y = y_pos[i])
    all_turtle.append(timmy)

if user_bet:
    is_race_on = "True"

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() < 230:
            rand_distance = random.randint(0,10)
            turtle.forward(rand_distance)
        else:
            is_race_on = False
            if user_bet == turtle.pencolor:
                print(f"Your {turtle.pencolor()} Won the race")
            else:
                print(f"Your {user_bet} lost the race. {turtle.pencolor()} won the race.")


screen.exitonclick()
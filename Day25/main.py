import turtle
import pandas

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

# screen.exitonclick() below is similar to screen.exitonclick( using because if we click then the
# window will close

# turtle.mainloop()
screen = turtle.Screen()
screen.title("U.S. state guess")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
right_guess = []
state_list = (data.state).to_list()
x_list = (data.x).to_list()
y_list = (data.y).to_list()
print(state_list)
print(x_list)
print(y_list)
while len(right_guess)<50:
    answer_state = (screen.textinput(title= f"{len(right_guess)}/50 guessed correct", prompt="What is the name of state")).title()
    if answer_state == "Exit":
        missing_state = []
        for s in state_list:
            if s not in right_guess:
                missing_state.append(s)
        learn_state = pandas.DataFrame(missing_state)
        learn_state.to_csv("learn.csv")
        break
    elif (answer_state not in right_guess) and (answer_state in state_list):
        right_guess.append(answer_state)
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        i = state_list.index(f"{answer_state}")
        text.goto(x_list[i],y_list[i])
        text.write(f"{answer_state}")



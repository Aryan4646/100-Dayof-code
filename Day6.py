# Doing this challenge on https://reeborg.ca/reeborg.html

# for hurdle 1

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def instru():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# for i in range(6):
#     instru()

# For hurdle 2

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def instru():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# while at_goal() != True:
#     instru()

# For hurdle 3

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def instru():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# while at_goal() != True:
#     if front_is_clear():
#         move()
#     else:
#         instru()

# For hurdle 4
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def instru():
#     turn_left()
#     while right_is_clear() != True:
#         move()
#     else:
#         turn_right()
#         move()
#         turn_right()
#     while front_is_clear():
#         move()
#     else:
#         turn_left()
# while at_goal() != True:
#     if front_is_clear():
#         move()
#     else:
#         instru()

# Final Maze:

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# while at_goal() != True:
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
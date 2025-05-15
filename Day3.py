print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
# print("Welcome to the treasure island\nMake choices and take your treasure home")
#
# direction = input("Please enter left or right:\n")
# if direction == "left":
#     sw = input("You would like to swim or wait:\n")
#     if sw == "wait":
#         print("You reached safely with the help of boat.")
#         door = input("Enter the door blue red or yellow:\n")
#         if door == "yellow":
#             print("You won the treasure.")
#         elif door == "red" or door == "blue":
#             print("You chose the wrong door so Game over.")
#         else:
#             print("Invalid door led to Game over")
#     elif sw == "swim":
#         print("You lost the path while swimming.\nGame over")
#     else:
#         print("Invalid option led to game over.")
# elif direction == "right":
#     print("You chose the wrong direction game over.")
# else:
#     print("Invalid option led to game over.")

# With enriched wording
print("Welcome to the mysterious Treasure Island!\nYour destiny awaits—make wise choices and claim your hidden fortune!")

direction = input("You're at a forked jungle path. Do you go left into the thick mist or right toward the howling cliffs?\n")
if direction == "left":
    sw = input("You arrive at a wide, murky river. Will you swim across or wait patiently on the shore?\n")
    if sw == "wait":
        print("A creaky wooden boat emerges from the fog and ferries you safely across the river.")
        door = input("You find a strange hut with three glowing doors: one blue, one red, and one yellow. Which do you choose?\n")
        if door == "yellow":
            print("The door creaks open to reveal a room overflowing with glittering treasure. You won the treasure!")
        elif door == "red" or door == "blue":
            print("You open the door and step into darkness... a trap! You chose the wrong door. Game over.")
        else:
            print("As you fumble with an unknown door, a magical curse seals your fate. Invalid door led to Game over.")
    elif sw == "swim":
        print("You dive in, but swirling currents pull you into the deep. You lost the path while swimming.\nGame over.")
    else:
        print("Confused and hesitant, you make no move. A shadow looms, and the adventure ends. Invalid option led to game over.")
elif direction == "right":
    print("You wander toward the cliffs, only to find a bottomless chasm. One misstep... and it's all over. You chose the wrong direction. Game over.")
else:
    print("Paralyzed by indecision, you stay too long. The island has no mercy. Invalid option led to game over.")



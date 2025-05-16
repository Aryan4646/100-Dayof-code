import random
input_num = int(input("What do you Choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
computer_input = random.randint(0,2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
user_choice = choices[input_num]
computer_choice = choices[computer_input]

if input_num < 0 or input_num > 2:
    print("Invalid number. You must choose 0, 1, or 2.")
else:
    user_choice = choices[input_num]
    computer_choice = choices[computer_input]
    print(f"Your choice:\n{user_choice}")
    print(f"Computer's choice:\n{computer_choice}")

    if input_num == computer_input:
        print("It's a draw!")
    elif (input_num == 0 and computer_input == 2) or \
            (input_num == 1 and computer_input == 0) or \
            (input_num == 2 and computer_input == 1):
        print("You win!")
    else:
        print("You lose.")





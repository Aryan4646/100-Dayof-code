import random

print("Welcome to Number guessing game!")
print("Think of a number between 1 to 100!")
diff = input("Choose difficulty, Type 'Easy' or 'Hard': ")

random_num = random.randint(1,100)
print(random_num)
if diff.lower() == 'hard':
    attempt = 5
    while attempt > 0:
        print(f"You have {attempt} attempts to make the guess")
        input_num = int(input("Make a guess: "))
        if input_num == random_num:
            print("You made the correct guess.")
            break
        elif input_num != random_num:
            attempt -= 1
            print("Made a wrong guess")
            if input_num < random_num:
                print("Too low")
            else:
                print("Too high")
    else:
        print(f"Number was {random_num}, You lost")
elif diff.lower() == 'easy':
    attempt = 10
    while attempt > 0:
        print(f"You have {attempt} attempts to make the guess")
        input_num = int(input("Make a guess: "))
        if input_num == random_num:
            print("You made the correct guess.")
            break
        elif input_num != random_num:
            attempt -= 1
            print("Made a wrong guess")
            if input_num < random_num:
                print("Too low")
            else:
                print("Too high")
    else:
        print(f"Number was {random_num},You lost")
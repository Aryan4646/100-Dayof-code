def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    if y == 0:
        return"Error you can not divide by zero"
    return x / y

op_dict = {"+" : add , "-" : sub,  "*" : mul, "/" : div}
while True :
    print("\n"*100)
    print("Welcome to the calculator!")
    try:
        num1 = float(input("Enter the first number:\n"))
    except ValueError:
        print("Please enter a valid number.")
        continue
    continue_cal = 'y'
    while continue_cal.lower() == 'y':
        op = input("+\n-\n*\n/\n")
        try:
            num2 = float(input("Enter the second number:\n"))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        res = op_dict[op](num1,num2)
        print(f"{num1}{op}{num2}= {res}")
        if type(res) == int or type(res) == float:
            num1 = res
        continue_cal = input(f"Enter 'y' if you want to perform operation on {num1} else enter 'n' for new calculation"
                                 f"Enter 'q' to quit the program.")
        if continue_cal.lower() == "q":
            print("Bye")
            exit()


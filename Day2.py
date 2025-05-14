print("Welcome to the tip calculator")
total = float(input("Enter the total bill: $"))
tip = float(input("Enter what percentage tip you want to give: "))
num = int(input("Enter the number of people you want to divide the bill: "))

bill = (total + (total*(tip/100)))/num

print(f"The total bill was: {total}\nYou want to give tip of {tip}%\nNumber of person to divide the bill :{num}")
# print(f"Each person has to pay: ${round(bill,2)}")
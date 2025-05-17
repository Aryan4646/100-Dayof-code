import random
# Letters
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
# Numbers
numbers_1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# Symbols
symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
    '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^',
    '_', '`', '{', '|', '}', '~'
]
print("Welcome to pypassword generator!")
letter = int(input("Enter how many letters you want to add in your password:\n"))
symbol = int(input("Enter how many symbols you want to add in your password:\n"))
number = int(input("How many number you would like to add in your password:\n"))

password = ""

# Easy password generation
# for i in range(letter):
#     random_letter = random.choice(letters)
#     password += random_letter
# for x in range(symbol):
#     random_symbol = random.choice(symbols)
#     password += random_symbol
# for z in range(number):
#     random_num = random.choice(numbers_1)
#     password += random_num
# print(f"Your password is: {password}")

# Hard password

password = ""
password_list = []

for i in range(letter):
    random_letter = random.choice(letters)
    password_list += random_letter
for x in range(symbol):
    random_symbol = random.choice(symbols)
    password_list += random_symbol
for z in range(number):
    random_num = random.choice(numbers_1)
    password_list += random_num

random.shuffle(password_list)
for char in password_list:
    password += char

print(f"Your password list is: {password_list}")
print(f"Your password is: {password}")



#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
with open(file = "./Input/Names/invited_names.txt") as Name:
    names = Name.readlines()

with open(file = "./Input/Letters/starting_letter.txt") as start_letter:
    letter = start_letter.read()
    for i in names:
        name = i.strip()
        new_letter = letter.replace(PLACEHOLDER, name)
        with open(file = f"./Output/ReadyToSend/letter_for_{name}.txt", mode ="w") as completed:
            completed.write(new_letter)




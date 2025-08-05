# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [i*i for i in numbers]
# print(squared_numbers)

# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(i) for i in list_of_strings]
# result = [i for i in numbers if i%2 == 0]
# print(result)

# with open("file1.txt",mode = 'r') as f:
#     file_one = f.readlines()
# with open("file2.txt", mode ='r') as f:
#     file_two = f.readlines()
#
# result = [int(i) for i in file_one if i in file_two]
#
# print(result)

# Without split method
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# li =[]
# new_word = ""
# for i in range(len(sentence)):
#     if sentence[i] == " ":
#         li.append(new_word)
#         new_word = ""
#     else:
#         new_word += sentence[i]
# li.append(new_word)
# result = {i:len(i) for i in li}
# print(result)

# with split method
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#
# weather_f = {k:((val*9/5) +32) for (k,val) in weather_c.items()}
#
# print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    print(row.score)
    #Access row.student or row.score
    pass


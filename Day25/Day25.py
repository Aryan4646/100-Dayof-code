# with open("weather_data.csv",mode = 'r') as f:
#     data = f.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for i in data:
#         print(i)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# temp_data = data["temp"]
# print(temp_data)

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(data_dict)
temperature = data["temp"].to_list()
print(temperature)

# temperature average
# temp = 0
# for i in temperature:
#     temp += i
# print(f"Average temperature: {temp/len(temperature)}")

# using pandas
# aver = data["temp"].mean()
# print(aver)
# # max element in temp
# print(data["temp"].max())
#
# # get data in column
# print(data["condition"])
# print(data.condition)
#
# # get row data
# print(data[data.day == "Monday"])

# maximum temperature row data
# print(data[data["temp"]== data["temp"].max()])

# create a dataframe from scratch

dict_on = {
    "students": ["Aryan", "Akshay", "Aditya"],
    "marks": [46,41,50]
}

new_data = pandas.DataFrame(dict_on)
print(new_data)
# if want to save in csv
new_data.to_csv("new_Data.csv")

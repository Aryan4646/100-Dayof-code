import pandas

sq_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250804.csv")
list_sq = sq_data["Primary Fur Color"].to_list()
print(list_sq)
sq_dict = {}
for i in list_sq:
    if i == "Gray":
        sq_dict[i] = sq_dict.get(i, 0) + 1
    elif i == "Cinnamon":
        sq_dict[i] = sq_dict.get(i, 0) + 1
    elif i == "Black":
        sq_dict[i] = sq_dict.get(i, 0) + 1
    else:
        sq_dict["Unknown color"] = sq_dict.get("Unknown color", 0) + 1
print(sq_dict)
new_csv = pandas.DataFrame({"Fur Color": list(sq_dict.keys()),
                            "Count": list(sq_dict.values())}
)
print(new_csv)
new_csv.to_csv("new_Data.csv")
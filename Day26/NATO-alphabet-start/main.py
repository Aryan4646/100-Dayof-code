import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

df = pandas.read_csv("nato_phonetic_alphabet.csv")
# out_dict = {}
# for index,row in df.iterrows():
#     out_dict[row.letter] = row.code
# print(out_dict)

out_dict = {row.letter:row.code for (index,row) in df.iterrows()}
print(out_dict)

input_str = input("Enter the string whose phonetic code you want: ").upper()
list = [out_dict[i] for i in input_str ]
print(list)



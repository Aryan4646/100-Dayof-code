import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width =500 , height= 300)


# Label
# my_label = tkinter.Label(text="I am a label", font=("Ariel",24,"bold"))
# my_label.pack()
#
# # Button
# def button_click():
#     print("I got clicked")
#     my_label["text"] = "Button Got Clicked"
#
# button = tkinter.Button(text= "Click Me",command= button_click)
# button.pack()
#
# # Entry
# input = tkinter.Entry(width = 10)
# input.pack()
# entry = input.get()
# print(entry)

# my_label = tkinter.Label(text="I am a label", font=("Ariel",24,"bold"))
# my_label.place(x =0,y =0)
#
# # Button
# def button_click():
#     new_text = input.get()
#     # print(f"Hey {new_text}")
#     my_label["text"] = f"Hey {new_text}"
#
# # Entry
# input = tkinter.Entry(width = 10)
# input.pack()
# entry = input.get()
# print(entry)
#
# button = tkinter.Button(text= "Click Me",command= button_click)
# button.pack()

my_label = tkinter.Label(text="I am a label", font=("Ariel",24,"bold"))
my_label.grid(column=0,row =0)

# Button
def button_click():
    new_text = input.get()
    # print(f"Hey {new_text}")
    my_label["text"] = f"Hey {new_text}"

# Entry
input = tkinter.Entry(width = 10)
input.grid(column=1,row=1)
entry = input.get()
print(entry)

button = tkinter.Button(text= "Click Me",command= button_click)
button.grid(column=2,row=2)




window.mainloop()

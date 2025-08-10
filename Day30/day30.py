import tkinter
from tkinter import messagebox
import random
import pyperclip
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pass_box.delete(0, tkinter.END)
    pass_box.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_pass():
    email = email_box.get()
    passwo = pass_box.get()
    website = website_box.get()
    new_data = {website: {
        "email":email,
        "password":passwo
    }}

    if len(website) ==0 or len(passwo) == 0 :
        messagebox.showinfo(title="Error", message = "dont leave either of field empty.")
    else:
        is_ok = messagebox.askokcancel(title= website, message = f"These are the details entered:\n Email: {email}\n Password:{passwo}")
        if is_ok:
            try:
                with open("file.json",mode= 'r') as f:
                    data = json.load(f)
            except FileNotFoundError:
                with open("file.json",mode= 'w') as f:
                    json.dump(data,f,indent= 4)
            else:
                data.update(new_data)
                with open("file.json",mode= 'w') as f:
                    json.dump(data,f,indent= 4)
            finally:
                website_box.delete(0,tkinter.END)
                pass_box.delete(0,tkinter.END)
                website_box.focus()
def search_web():
    website = website_box.get()
    try:
        with open("file.json",mode ='r') as f:
            db = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title= "Error", message= "Data file not found error")
    else:
        if website in db:
            email = db[website]["email"]
            password = db[website]["password"]
            messagebox.showinfo(title= website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title= "error", message= f"No details of {website} exists.")


    # ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(pady=50,padx=50)

canvas = tkinter.Canvas(height=200,width =200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100,image= logo_img)
canvas.grid(column = 1, row = 0)

website_label = tkinter.Label(text= "Website:")
website_label.grid(column = 0, row = 1)

email_label = tkinter.Label(text= "Email/Username:")
email_label.grid(column = 0, row =2)

pass_label = tkinter.Label(text= "Password:")
pass_label.grid(column = 0, row =3)

website_box = tkinter.Entry(width= 21)
website_box.grid(column=1,row=1)
website_box.focus()

email_box = tkinter.Entry(width =35)
email_box.grid(column=1,row = 2, columnspan=2)
email_box.insert(0,"youremail@gmail.com")

pass_box = tkinter.Entry(width=21)
pass_box.grid(column=1,row=3)

add_button = tkinter.Button(text= "Add",width=36,command= add_pass)
add_button.grid(column= 1,row= 4,columnspan= 2)

gen_pass = tkinter.Button(text= "Generate Password",command= gen_password)
gen_pass.grid(column=2,row=3)

search_button = tkinter.Button(text= "Search ",command= search_web)
search_button.grid(column=2 , row= 1)



window.mainloop()
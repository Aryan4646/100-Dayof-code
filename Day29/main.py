import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

website_box = tkinter.Entry(width= 35)
website_box.grid(column=1,row=1,columnspan=2)
website_box.focus()

email_box = tkinter.Entry(width =35)
email_box.grid(column=1,row = 2, columnspan=2)
email_box.insert(0,"youremail@gmail.com")

pass_box = tkinter.Entry(width=21)
pass_box.grid(column=1,row=3)

add_button = tkinter.Button(text= "Add",width=36)
add_button.grid(column= 1,row= 4,columnspan= 2)

gen_pass = tkinter.Button(text= "Generate Password")
gen_pass.grid(column=2,row=3)




window.mainloop()
import tkinter


window = tkinter.Tk()
window.title("Miles to km converter")
window.minsize(width = 300, height =100)
window.config(padx=40,pady=20)

is_equal = tkinter.Label(text ="is equal to")
is_equal.grid(column= 0 , row = 2)

mile_entry = tkinter.Entry(width =10)
mile_entry.grid(column = 1, row = 1)

milelabel = tkinter.Label(text="Miles")
milelabel.grid(column = 2, row = 1)

kmlabel = tkinter.Label(text="Kms")
kmlabel.grid(column = 2, row = 2)

km_entry = tkinter.Label(text= "0")
km_entry.grid(column=1 , row = 2)

def action():
    mile = mile_entry.get()
    new_km = 1.6*int(mile)
    km_entry.config(text = f"{new_km}")

button = tkinter.Button(text="Calculate", command=action)
button.grid(column=1,row =3)


window.mainloop()
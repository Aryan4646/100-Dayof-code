from pandas.core.interchange.dataframe_protocol import DataFrame

BACKGROUND_COLOR = "#B1DDC6"

import tkinter
import pandas
import random
current_card ={}
data_dict = {}


try:
    data = pandas.read_csv("./data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    data_dict = original_data.to_dict(orient= "records")
else:
    data_dict = data.to_dict(orient= "records")


def new_Word():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text= "French",fill = "black")
    canvas.itemconfig(card_word, text= current_card["French"],fill = "black")
    canvas.itemconfig(canavs_background, image = flash_card_front_img)
    flip_timer= window.after(3000,func = flipcard)

#-----FLIP CARD -----#
def flipcard():
    canvas.itemconfig(card_title, text= "English",fill = "white")
    canvas.itemconfig(card_word,text = current_card["English"],fill = "white")
    canvas.itemconfig(canavs_background, image = flash_car_back_img)

def is_known():
    data_dict.remove(current_card)
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("./data/word_to_learn.csv",index= False)
    new_Word()

#------- Ui Setup -----#
window = tkinter.Tk()
window.title("Flashy")
window.config(padx= 50 , pady=50,bg= BACKGROUND_COLOR)

flip_timer = window.after(3000,func = flipcard)

tick_Image = tkinter.PhotoImage(file= "./images/right.png")
wrong_Image = tkinter.PhotoImage(file= "./images/wrong.png")

canvas = tkinter.Canvas(height= 526, width= 800)
flash_card_front_img = tkinter.PhotoImage(file= "./images/card_front.png")
flash_car_back_img = tkinter.PhotoImage(file="./images/card_back.png")

canavs_background = canvas.create_image(400,263 ,image= flash_card_front_img)
canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
card_title= canvas.create_text(400,150,text= "", font= ("Ariel",40,"italic"))
card_word= canvas.create_text(400,263,text="",font= ("Ariel",60,"bold"))
canvas.grid(column =0, row= 0, columnspan= 2 )

tick_button = tkinter.Button(image= tick_Image,command= is_known, highlightthickness= 0)
tick_button.grid(column= 1, row= 1)
wrong_button = tkinter.Button(image= wrong_Image,command= new_Word, highlightthickness=0)
wrong_button.grid(column=0, row= 1)

new_Word()


window.mainloop()


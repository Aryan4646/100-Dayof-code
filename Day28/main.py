import tkinter
from tkinter import PhotoImage
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer =None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text= "00:00")
    timer_label.config(text = "TIMER")
    check_mark.config(text= "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="BREAK", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="WORK", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text= f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,countdown,count-1)
    else:
        start_timer()
        mark = ""
        work_session = reps//2
        for i in range(work_session):
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg =YELLOW)

timer_label = tkinter.Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
timer_label.grid(column=1,row=0)

start_button = tkinter.Button(text="Start",command= start_timer,highlightthickness= 0)
start_button.grid(column=0,row=2)

reset_button = tkinter.Button(text="Reset",highlightthickness= 0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_mark = tkinter.Label(fg=GREEN,bg=YELLOW)
check_mark.grid(column=1,row=3)


canvas = tkinter.Canvas(width=200 ,height =223,bg =YELLOW,highlightthickness= 0)
x = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(102,112,image = x)
timer_text = canvas.create_text(101,130,text="00:00", fill="white",font =(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


window.mainloop()
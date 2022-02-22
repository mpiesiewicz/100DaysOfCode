import tkinter
from tkinter import Tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
RED = "#ff99a3"
BLUE = "#2B2D42"
WHITE = "#ffe5e8"
GREEN = '#60d394'
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
ticks = str()
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer
    global ticks
    global reps

    if timer is not None:
        window.after_cancel(timer)
        label.config(text='Timer')
        canvas.itemconfig(timer_text, text='00:00')
        ticks = str()
        check_label.config(text=str())
        tick_counter.config(text='0')
        reps = 0
        timer = None


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        label.config(text='Looong break!', fg=GREEN)
        count_down(LONG_BREAK_MIN*60)
    elif reps % 2 == 0:
        label.config(text='Short break.', fg=GREEN)
        count_down(SHORT_BREAK_MIN*60)
    else:
        label.config(text='Work hard now!', fg=RED)
        count_down(WORK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global ticks
    global timer

    count_min = math.floor(count/60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f'{count_min:02}:{count_sec:02}')
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            ticks += '✓'
            # ticks += '🍅'
            check_label.config(text=ticks)
            tick_counter.config(text=len(ticks))
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomidorrro')
# window.minsize(width=500, height=500)
window.config(padx=50, pady=50, bg=WHITE)
window.resizable(width=False, height=False)

canvas = tkinter.Canvas(width=220, height=224, bg=WHITE, highlightthickness=False)
background_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(103, 112, image=background_img)
timer_text = canvas.create_text(103, 130, text='00:00', fill=WHITE, font=(FONT_NAME, 15, 'bold'))
canvas.grid(column=1, row=1)

label = tkinter.Label(text='Timer', fg=RED, bg=WHITE, font=(FONT_NAME, 15, 'bold'))
label.grid(column=1, row=0)

start_button = tkinter.Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = tkinter.Label(bg=WHITE, fg=GREEN, font=(FONT_NAME, 20, 'bold'))
check_label.grid(column=1, row=3)

tick_counter = tkinter.Label(text=len(ticks), bg=WHITE, fg=BLUE, font=(FONT_NAME, 8, 'bold'))
tick_counter.grid(column=1, row=2)

window.mainloop()

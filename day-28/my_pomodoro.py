import math
from tkinter import *
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
work_reps = 0
checkmark = ''
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer', fg=GREEN)
    checkmark_label.config(text='')
    canvas.itemconfig(timer_pict, image=work_png)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps, work_reps
    reps += 1

    # work_sec = WORK_MIN*60
    # short_break_sec = SHORT_BREAK_MIN*60
    # long_break_sec = LONG_BREAK_MIN*60

    work_sec = 0.1*60
    short_break_sec = 0.1*60
    long_break_sec = 0.1*60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text='Break', fg=RED)
        canvas.itemconfig(timer_pict, image=rest_png)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text='Break', fg=PINK)
        canvas.itemconfig(timer_pict, image=rest_png)
    else:
        count_down(work_sec)
        timer_label.config(text='Work', fg=GREEN)
        canvas.itemconfig(timer_pict, image=work_png)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            global checkmark
            checkmark += '✔️'
            checkmark_label.config(text=checkmark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
work_png = PhotoImage(file='work.png')
rest_png = PhotoImage(file='rest.png')
timer_pict = canvas.create_image(100, 112, image=work_png)
timer_text = canvas.create_text(100, 90, text='00:00', fill='white',
                                font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)


timer_label = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
timer_label.grid(row=0, column=1)

checkmark_label = Label(text='', fg=GREEN, bg=YELLOW)
checkmark_label.grid(row=3, column=1)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()

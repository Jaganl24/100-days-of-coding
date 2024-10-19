from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 3
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps = 0
current_time = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(current_time)
    canvas.itemconfig(timer, text="00:00")
    timer_logo.config(text="Timer", font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
    check.config(text='')






# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    print(reps)
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    # if its 1st/3rd/5th/7th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_logo.config(text="Break", fg=RED, font=(FONT_NAME, 35), bg=YELLOW)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_logo.config(text="Break", fg=PINK, font=(FONT_NAME, 35), bg=YELLOW)

    else:
        count_down(work_sec)
        timer_logo.config(text="Work", fg=GREEN, font=(FONT_NAME, 35), bg=YELLOW)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = (f"0{count_sec}")
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global current_time
        current_time = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_mark = "✔"*int((reps/2))
            check.config(text=check_mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# tomato and timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# after calls a function after an amount of time that is specified

# timer logo
timer_logo = Label(text="Timer", font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
timer_logo.grid(column=1, row=0)
# Start Button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
# Reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)
# checkmarks
check = Label( bg=YELLOW, fg=GREEN)
check.grid(column=1, row=3)



window.mainloop()
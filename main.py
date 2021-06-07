from tkinter import *
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
REPS = 0
CHECK_MARK_LIST = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global CHECK_MARK_LIST, REPS

    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    REPS = 0
    CHECK_MARK_LIST = ""
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60


    if REPS % 2 > 0:
        print("work")
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_secs)
    elif REPS == 8:
        print("long break")
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break_secs)
    else:
        print("short break")
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(number):
    count_minute = math.floor(number / 60)
    count_seconds = number % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")

    if number > 0:
        global timer
        timer = canvas.after(1, count_down, number - 1)
    else:
        if REPS % 2 > 0:
            global CHECK_MARK_LIST
            CHECK_MARK_LIST += "✔"
            check_mark.config(text=CHECK_MARK_LIST)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1)

start_button = Button(height=1, width=6, text="Start", font=(FONT_NAME, 12), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(height=1, width=6, text="Reset", font=(FONT_NAME, 12), command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(bg=YELLOW, fg=RED, font=20)
check_mark.grid(row=3, column=1)

window.mainloop()

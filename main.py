"""
Pomodoro

Author: Alan
Date: September 15th 2024

This script generates a window with the Pomodoro timer.
It sets a timer that lasts a couple of minutes depending on what you should do based on the Pomodoro work-style.
Each repetition will encourage you to work, then take short breaks.
"""

from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def reset_timer():
    try:
        # Pauses the timer
        window.after_cancel(timer)

        # Reset timer
        canvas.itemconfig(timer_text, text="00:00")

        # Reset label
        timer_label.config(text="Timer", fg=GREEN)

        # Reset markers
        checkmark_label.config(text="")

        global reps
        reps = 0

    except ValueError:
        pass

def start_timer():
    """
    Calls the function count_down with a specific amount of time
    :return:
    """

    # In case the user inputs the timer, it'll end the last timer
    try:
        # Pauses the timer
        window.after_cancel(timer)
    except ValueError:
        pass

    global reps
    reps += 1

    # Set the minutes in seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Based on the rep, will have different timer
    # It goes: Work, break, work, break, work, break, work and then long break
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

def count_down(count_time):
    """
    Shows a count_down of a specific time
    :param count_time: Integer with the seconds
    """

    # Get time in minutes and seconds
    count_minute = count_time // 60
    count_second = count_time % 60

    # Change format of minutes to correctly set it
    if count_minute < 10:
        count_minute = f"0{count_minute}"

    # Change format of seconds to correctly set it
    if count_second < 10:
        count_second = f"0{count_second}"

    # Set time in the GUI
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")

    # If the time is larger than 0, it'll call this function again, else, it'll do the next rep of start_timer()
    if count_time > 0:
        global timer
        timer = window.after(1000, count_down, count_time - 1)
    else:

        start_timer()

        marks = ""

        # Checks the amount of work_sessions
        work_sessions = reps // 2

        # For each work_session, we will add a checkmark
        for _ in range(work_sessions):
            marks += "✔"

        checkmark_label.config(text=marks)

window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# New label with the text Timer
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW, highlightthickness=0)
timer_label.grid(column=1, row=0)

# Reads the data of a photographic image
tomato_img = PhotoImage(file="tomato.png")

# New canvas for image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Creates an image using the data
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_label = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
checkmark_label.grid(column=1, row=3)

# Keeps the window in the screen
window.mainloop()
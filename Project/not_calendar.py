import sys
import subprocess
from tkinter import *

# --- functions --- #

def delete():
    before_answer.delete(0, 'end')
    latest_answer.delete(0, 'end')

def submit():
    time_before = before_answer.get()
    time_latest = latest_answer.get()
    print("before " + time_before)
    print("latest " + time_latest)
    submitButton.after(0, delete)

def go_back():
    subprocess.Popen(['Python', 'settings.py'])
    sys.exit(0)

# -------------------------------------------------------------------------------------------------------------- #
# --- background interface --- #

calendar = Tk()
calendar.geometry("800x480")
calendar.config(background='grey')
#background.attributes('-fullscreen', True)

# -------------------------------------------------------------------------------------------------------------- #
# --- divider --- #

before_question = Label(calendar, text="\n", background="grey", foreground="white", font=("BloomSpeak Body", 5))
before_question.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #
# --- alarm time before first meeting --- #

before_question = Label(calendar, text="How long before your first meeting do you want to wake up?\n(HH:MM)", background="grey", foreground="white", font=("BloomSpeak Body", 15))
before_question.pack(anchor="center")
before_answer = Entry(calendar)
before_answer.config(font=("BloomSpeak Body", 25), width=40)
before_answer.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #
# --- divider --- #

before_question = Label(calendar, text="\n", background="grey", foreground="white", font=("BloomSpeak Body", 5))
before_question.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #
# --- latest alarm time --- #

latest_question = Label(calendar, text="What is the latest moment the Alarm should go off?\n(HH:MM)", background="grey", foreground="white", font=("BloomSpeak Body", 15))
latest_question.pack(anchor="center")
latest_answer = Entry(calendar)
latest_answer.config(font=("BloomSpeak Body", 25), width=40)
latest_answer.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #
# --- divider --- #

before_question = Label(calendar, text="\n", background="grey", foreground="white", font=("BloomSpeak Body", 5))
before_question.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #
# --- delete and submit input -- #

deleteButton = Button(calendar, text="delete", command=delete, font=("BloomSpeak Body", 25), width= 25)
deleteButton.pack(anchor="center")

submitButton = Button(calendar, text="submit", command=submit, font=("BloomSpeak Body", 25), width= 25)
submitButton.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #
# --- divider --- #

before_question = Label(calendar, text="\n", background="grey", foreground="white", font=("BloomSpeak Body", 5))
before_question.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #
# --- back to settings --- #

goBack = Button(calendar, text="go back", command=go_back, font=("BloomSpeak Body", 25), width= 25)
goBack.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #

calendar.mainloop()
import sys
import subprocess
from tkinter import *

# --- functions --- #

def delete():
    answer.delete(0, 'end')

def submit():
    city = answer.get()
    return city

def go_back():
    subprocess.Popen(['Python', 'settings.py'])
    sys.exit(0)

# -------------------------------------------------------------------------------------------------------------- #
# --- background interface --- #

weather = Tk()
weather.geometry("800x480")
weather.config(background='grey')
#weather.attributes('-fullscreen', True)

# -------------------------------------------------------------------------------------------------------------- #
# --- divider --- #

before_question = Label(weather, text="\n", background="grey", foreground="white", font=("BloomSpeak Body", 5))
before_question.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #
# --- city for weather --- #

question = Label(weather, text="Off which city do you want to know the weather?", background="grey", foreground="white", font=("BloomSpeak Body", 20))
question.pack(anchor="center")
answer = Entry(weather)
answer.config(font=("BloomSpeak Body", 25), width=40)
answer.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #
# --- divider --- #

before_question = Label(weather, text="\n", background="grey", foreground="white", font=("BloomSpeak Body", 5))
before_question.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #
# --- delete and submit input -- #

deleteButton = Button(weather, text="delete", command=delete, font=("BloomSpeak Body", 25), width= 25)
deleteButton.pack(anchor="center")

submitButton = Button(weather, text="submit", command=submit, font=("BloomSpeak Body", 25), width= 25)
submitButton.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #
# --- divider --- #

before_question = Label(weather, text="\n", background="grey", foreground="white", font=("BloomSpeak Body", 5))
before_question.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #
# --- back to settings --- #

goBack = Button(weather, text="go back", command=go_back, font=("BloomSpeak Body", 25), width= 25)
goBack.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #

weather.mainloop()
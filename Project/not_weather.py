from distutils.command import clean
import sys
import atexit
import subprocess
from tkinter import *

# --- functions --- #

def delete():
    answer.delete(0, 'end')

def submit():
    city = answer.get()
    if (city != ''):
        city__weather = open("/home/slimmewekker/Documenten/Project/textDocs/City_Weather.txt", 'w')
        city__weather.write(city)
        city__weather.close()
    submitButton.after(0, delete)

def go_back():
    weather.destroy()
    subprocess.call(['python', '/home/slimmewekker/Documenten/Project/settings.py'])

# -------------------------------------------------------------------------------------------------------------- #
# --- background interface --- #

weather = Tk()
weather.config(background='grey')
weather.attributes('-fullscreen', True)

# -------------------------------------------------------------------------------------------------------------- #
# --- city for weather --- #

question = Label(weather, text="Stad voor het weerbericht", background="grey", foreground="white", font=("BloomSpeak Body", 20))
question.place(x=15, y=10)
answer = Entry(weather)
answer.config(font=("BloomSpeak Body", 20), width=45)
answer.place(x=15, y=60)

# -------------------------------------------------------------------------------------------------------------- #
# --- delete and submit input -- #

deleteButton = Button(weather, text="verwijderen", command=delete, font=("BloomSpeak Body", 15), width= 10)
deleteButton.place(x=310, y=110)

submitButton = Button(weather, text="bevestigen", command=submit, font=("BloomSpeak Body", 15), width= 10)
submitButton.place(x=310,y=150)

# -------------------------------------------------------------------------------------------------------------- #
# --- back to settings --- #

goBack = Button(weather, text="ga terug", command=go_back, font=("BloomSpeak Body", 15), width= 10)
goBack.place(x=310,y=230)

# -------------------------------------------------------------------------------------------------------------- #

weather.mainloop()
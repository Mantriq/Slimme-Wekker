from cProfile import label
from cgitb import text
import sys
import subprocess
from tkinter import *
from time import strftime
from turtle import back

# --- functions --- #

def open_calender():
    subprocess.Popen(['Python', 'calendar.py'])
    sys.exit(0)

def open_weather():
    subprocess.Popen(['Python', 'weather.py'])
    sys.exit(0)

def go_back():
    subprocess.Popen(['Python', 'interface.py'])
    sys.exit(0)

def live_time():
    time = strftime('%H:%M')
    clock.config(text=time)
    clock.after(1000, live_time)

# -------------------------------------------------------------------------------------------------------------- #
# --- background interface --- #

settings = Tk()
settings.geometry("800x480")
settings.config(background="grey")
#settings.attributes('-fullscreen', True)

# -------------------------------------------------------------------------------------------------------------- #
# --- setting buttons --- #

calendarButton = Button(settings, text=("Calender"), font=("BloomSpeak Body", 33), width=10, command=open_calender, justify="left")
calendarButton.place(anchor="nw")

weatherButton = Button(settings, text=("Weather"), font=("BloomSpeak Body", 33), width=10, command=open_weather)
weatherButton.place(x=265, anchor="nw")

backButton = Button(settings, text=("Go back"), font=("BloomSpeak Body", 33), width=10, command=go_back)
backButton.place(x=530, anchor="nw")

# -------------------------------------------------------------------------------------------------------------- #
# --- clock --- #

clock = Label(settings, font=("BloomSpeak Body", 140), background="grey", foreground="white")
clock.place(x=200, y=150, anchor="nw")
live_time()

# -------------------------------------------------------------------------------------------------------------- #

settings.mainloop()
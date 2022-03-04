from tkinter import *
from time import strftime
from turtle import back

background = Tk()
background.geometry("800x480")
background.config(background="grey")
#background.attributes('-fullscreen', True)

def open_calender():
    exec(open("calendar.py").read())

calender_button = Button(background, text=("Calender"), font=("BloomSpeak Body", 50), width=10, command=open_calender)
calender_button.pack(anchor="w")

def open_weather():
    exec(open("weather.py").read())

weather_button = Button(background, text=("Weather"), font=("BloomSpeak Body", 50), width=10, command=open_weather)
weather_button.pack(anchor="w")

def open_interface():
    exec(open("interface.py").read())

back_button = Button(background, text=("Go back"), font=("BloomSpeak Body", 50), width=10, command=open_interface)
back_button.pack(anchor="w")

mainloop()
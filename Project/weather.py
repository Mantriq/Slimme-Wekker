from tkinter import *
from types import CoroutineType

background = Tk()
background.geometry("800x480")
background.config(background='grey')
#background.attributes('-fullscreen', True)

question = Label(background, text="Off which city do you want to know the weather", background="grey", foreground="white", font=("BloomSpeak Body", 25))
question.pack(anchor="w")
answer = Entry(background)
answer.config(font=("BloomSpeak Body", 50), width=10)
answer.pack(anchor="w")

def submit():
    city = answer.get()
    print("City " + city)

before_submit = Button(background, text="submit", command=submit, font=("BloomSpeak Body", 25))
before_submit.pack(anchor="w")

def open_weather_API():
    exec(open("weather_API.py").read())

before_submit = Button(background, text="weather", command=open_weather_API, font=("BloomSpeak Body", 25))
before_submit.pack(anchor="w")

mainloop()
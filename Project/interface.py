from tkinter import *
from time import strftime
from turtle import back

background = Tk()
background.geometry("800x480")
background.config(background='grey')
#background.attributes('-fullscreen', True)

def open_settings():
    exec(open(file="settings.py").read())

setting_image = PhotoImage(file="Settings_LOGO.png").subsample(7,7)
settings_button = Button(background, image=setting_image, command=open_settings)
settings_button.pack(anchor="nw")

def live_time():
    time = strftime('%H:%M')
    clock.config(text=time)
    clock.after(1000, live_time)

clock = Label(background, font=("BloomSpeak Body", 180), background="grey", foreground="white")
clock.pack()
live_time()

mainloop()
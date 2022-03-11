from msilib.schema import File
import sys
import subprocess
from tkinter import *
from time import strftime
from turtle import back

interface = Tk()
interface.geometry("800x480")
interface.config(background='grey')
#interface.attributes('-fullscreen', True)

def open_settings():
    subprocess.Popen(['Python', 'settings.py'])
    sys.exit(0)

setting_image = PhotoImage(file="Settings_LOGO.png").subsample(7,7)
settings_button = Button(interface, image=setting_image, command=open_settings)
settings_button.pack(anchor="nw")

def live_time():
    time = strftime('%H:%M')
    clock.config(text=time)
    clock.after(1000, live_time)

clock = Label(interface, font=("BloomSpeak Body", 180), background="grey", foreground="white")
clock.pack()
live_time()

interface.mainloop()
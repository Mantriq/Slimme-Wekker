from tkinter import *
from time import strftime

root = Tk()
#root.attributes('-fullscreen', True)

def live_time():
    time = strftime('%H:%M')
    clock.config(text=time)
    clock.after(1000, live_time)

def settings():
    exec(open("settings.py").read())

background_interface = Canvas(root, width=800, height=480, background="grey")
background_interface.pack()

settings_img = PhotoImage(file=r"C:\Users\marti\Documents\Thomas More - SCHOOL\Practice Enterprice\Settings_LOGO.png").subsample(7,7)
settings_button = Button(background_interface, image=settings_img, command=settings)
settings_button.place(x=0, y=0)

clock = Label(background_interface, font=("BloomSpeak Body", 200), background="grey", foreground="white")
clock.place(x=140, y=75)
live_time()

mainloop()
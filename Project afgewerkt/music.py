import sys
import subprocess
import os
from pytube import YouTube
from os.path import exists
from tkinter import *
from tkinter import filedialog, Text

# --- functions --- #

# --- keuze tussen youtube of gedownloade muziek --- music.py --- #
def choice():
    test = var.get()
    if (test == 1):
        musicButton.place(x=310,y=150)
        yt.place_forget()
        ytAnswer.place_forget()
        deleteButton.place_forget()
        submitButton.place_forget()
    elif (test == 2):
        yt.place(x=15, y=100)
        ytAnswer.place(x=15, y=140)
        deleteButton.place(x=310, y=200)
        submitButton.place(x=310, y=238)
        musicButton.place_forget()
    
# --- bestand kiezen --- music.py --- #
def choose_file():
    filename = filedialog.askopenfilename(initialdir="/home/slimmewekker/Documenten/Project/Alarm", title="choose music", filetypes=(("mp3", "*.mp3"), ("wma", "*.wma"), ("wav", "*.wav"), ("all files", "*.*")))
    if (exists("/home/slimmewekker/Documenten/Project/textDocs/youtube.txt") == True):
        os.remove("/home/slimmewekker/Documenten/Project/textDocs/youtube.txt")
    file = open("/home/slimmewekker/Documenten/Project/textDocs/music.txt", 'w')
    if (filename == ()):
        file.write("/home/slimmewekker/Documenten/Project/Alarm/Alarm_1.mp3")
    else:
        file.write(filename)
    file.close()

def delete():
    ytAnswer.delete(0, 'end')

def submit():
    yt = ytAnswer.get()
    if (yt != ''):
        file = open("/home/slimmewekker/Documenten/Project/textDocs/youtube.txt", 'w')
        file.write(yt)
        file.close()
        if (exists("/home/slimmewekker/Documenten/Project/textDocs/music.txt") == True):
            os.remove("/home/slimmewekker/Documenten/Project/textDocs/music.txt")
    submitButton.after(0, delete)

def go_back():
    music.destroy()
    subprocess.call(['python', '/home/slimmewekker/Documenten/Project/settings.py'])

# -------------------------------------------------------------------------------------------------------------- #
# --- background interface --- #

music = Tk()
music.config(background='grey')
music.attributes('-fullscreen', True)

# -------------------------------------------------------------------------------------------------------------- #
# --- radio --- #

var = IntVar()
radioDownloaded = Radiobutton(music, text='Gedownloade muziek',font=("BloomSpeak Body", 15), width= 20 , variable=var, value=1, command=choice)
radioDownloaded.place(x=250)
radioYoutube = Radiobutton(music, text='YouTube muziek',font=("BloomSpeak Body", 15), width= 20 , variable=var, value=2, command=choice)
radioYoutube.place(x=250,y=30)

# -------------------------------------------------------------------------------------------------------------- #
# --- choose music -- #

musicButton = Button(music, text="muziek", command=choose_file, font=("BloomSpeak Body", 15), width= 10)

# -------------------------------------------------------------------------------------------------------------- #
# --- yt link --- #

yt = Label(music, text="zet hier de link naar een video", background="grey", foreground="white", font=("BloomSpeak Body", 20))
ytAnswer = Entry(music)
ytAnswer.config(font=("BloomSpeak Body", 20), width=45)

# -------------------------------------------------------------------------------------------------------------- #
# --- delete and submit input -- #

deleteButton = Button(music, text="verwijderen", command=delete, font=("BloomSpeak Body", 15), width= 10)

submitButton = Button(music, text="bevestigen", command=submit, font=("BloomSpeak Body", 15), width= 10)

# -------------------------------------------------------------------------------------------------------------- #
# --- back to settings --- #

goBack = Button(music, text="ga terug", command=go_back, font=("BloomSpeak Body", 15), width= 10)
goBack.place(x=310,y=300)

# -------------------------------------------------------------------------------------------------------------- #

music.mainloop()
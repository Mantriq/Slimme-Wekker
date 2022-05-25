import sys
import subprocess
import os
from tkinter import *
from tkinter import filedialog, Text

# --- functions --- #

def choice():
    test = var.get()
    if (test == 1):
        musicButton.place(y=100)
        yt.pack_forget()
        ytAnswer.place_forget()
        deleteButton.place_forget()
        submitButton.place_forget()
    elif (test == 2):
        yt.pack()
        ytAnswer.place(y=200)
        deleteButton.place(y=250)
        submitButton.place(y=300)
        musicButton.place_forget()
    

def choose_file():
    filename = filedialog.askopenfilename(initialdir="/", title="choose music", filetypes=(("mp3", "*.mp3"), ("wma", "*.wma"), ("wav", "*.wav"), ("all files", "*.*")))
    file = open("textDocs/music.txt", 'w')
    file.write(filename)
    file.close()
    os.remove('textDocs/youtube.txt')

def delete():
    ytAnswer.delete(0, 'end')

def submit():
    ytube = ytAnswer.get()
    youtube = open('textDocs/youtube.txt', 'w')
    youtube.write(ytube)
    youtube.close()
    submitButton.after(0, delete)
    os.remove("textDocs/music.txt")

def go_back():
    subprocess.Popen(['Python', 'settings.py'])
    sys.exit(0)

# -------------------------------------------------------------------------------------------------------------- #
# --- background interface --- #

music = Tk()
music.geometry("800x480")
music.config(background='grey')
#background.attributes('-fullscreen', True)

# -------------------------------------------------------------------------------------------------------------- #
# --- radio --- #

var = IntVar()
radioDownloaded = Radiobutton(music, text='Downloaded music', variable=var, value=1, command=choice)
radioDownloaded.pack(anchor='center')
radioYoutube = Radiobutton(music, text='YouTube music', variable=var, value=2, command=choice)
radioYoutube.pack(anchor='center')

# -------------------------------------------------------------------------------------------------------------- #
# --- divider --- #

before_question = Label(music, text="\n", background="grey", foreground="white", font=("BloomSpeak Body", 5))
before_question.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #
# --- choose music -- #

musicButton = Button(music, text="music", command=choose_file, font=("BloomSpeak Body", 25), width= 25)

# -------------------------------------------------------------------------------------------------------------- #
# --- divider --- #

before_question = Label(music, text="\n", background="grey", foreground="white", font=("BloomSpeak Body", 5))
before_question.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #
# --- latest alarm time --- #

yt = Label(music, text="zet hier de link naar een video", background="grey", foreground="white", font=("BloomSpeak Body", 15))
ytAnswer = Entry(music)
ytAnswer.config(font=("BloomSpeak Body", 25), width=40)

# -------------------------------------------------------------------------------------------------------------- #
# --- divider --- #

before_question = Label(music, text="\n", background="grey", foreground="white", font=("BloomSpeak Body", 5))
before_question.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #
# --- delete and submit input -- #

deleteButton = Button(music, text="delete", command=delete, font=("BloomSpeak Body", 25), width= 25)

submitButton = Button(music, text="submit", command=submit, font=("BloomSpeak Body", 25), width= 25)

# -------------------------------------------------------------------------------------------------------------- #
# --- divider --- #

before_question = Label(music, text="\n", background="grey", foreground="white", font=("BloomSpeak Body", 5))
before_question.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #
# --- back to settings --- #

goBack = Button(music, text="go back", command=go_back, font=("BloomSpeak Body", 25), width= 25)
goBack.place(y=450)

# -------------------------------------------------------------------------------------------------------------- #

music.mainloop()
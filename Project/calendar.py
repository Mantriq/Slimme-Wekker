from tkinter import *

background = Tk()
background.geometry("800x480")
background.config(background='grey')
#background.attributes('-fullscreen', True)

before_question = Label(background, text="How long before your first meeting do you want to wake up?\n(HH:MM)", background="grey", foreground="white", font=("BloomSpeak Body", 25))
before_question.pack(anchor="w")
before_answer = Entry(background)
before_answer.config(font=("BloomSpeak Body", 50), width=10)
before_answer.pack(anchor="w")

latest_question = Label(background, text="What is the latest moment the Alarm should go off?\n(HH:MM)", background="grey", foreground="white", font=("BloomSpeak Body", 25))
latest_question.pack(anchor="w")
latest_answer = Entry(background)
latest_answer.config(font=("BloomSpeak Body", 50), width=10)
latest_answer.pack(anchor="w")

def submit():
    time_latest = latest_answer.get()
    time_before = before_answer.get()
    print("before " + time_before)
    print("latest " + time_latest)

before_submit = Button(background, text="submit", command=submit, font=("BloomSpeak Body", 25))
before_submit.pack(anchor="w")

def open_calendar_API():
    exec(open("calendar_API.py").read())

before_submit = Button(background, text="calendar", command=open_calendar_API, font=("BloomSpeak Body", 25))
before_submit.pack(anchor="w")

mainloop()
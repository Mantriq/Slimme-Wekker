from cProfile import label
import sys
import subprocess
from turtle import color
import webbrowser
import os
import os.path
from tkinter import *
from os.path import exists

# --- functions --- #

def delete_before():
    before_answer.delete(0, 'end')

def submit_before():
    time_before = before_answer.get()
    if (exists("textDocs/times.txt") == True):
        times = open('textDocs/times.txt', 'r')
        time_latest = times.readlines()[1]
        times.close()
    times = open('textDocs/times.txt', 'w')
    times.write(time_before + '\n' + time_latest)
    times.close()
    submitBeforeButton.after(0, delete_before)

def delete_latest():
    latest_answer.delete(0, 'end')

def submit_latest():
    time_latest = latest_answer.get()
    if (exists("textDocs/times.txt") == True):
        times = open('textDocs/times.txt', 'r')
        time_before = times.readlines()[0]
        times.close()
    times = open('textDocs/times.txt', 'w')
    times.write(time_before + time_latest)
    times.close()
    submitLatestButton.after(0, delete_latest)

def delete_calendarId():
    calendarID_answer.delete(0, 'end')

def submit_calendarId():
    CalendarId = calendarID_answer.get()
    Id = open('textDocs/calendarId.txt', 'w')
    Id.write(CalendarId)
    Id.close()
    submitCalendarIdButton.after(0, delete_calendarId)
    
def calendarId():
    webbrowser.open('https://www.sociablekit.com/get-find-google-calendar-id/')

def reset_token():
    if (exists('token.json') == True):
        os.remove('token.json')
        subprocess.call(['Python', 'calendar_API.py'])

def delete_all():
    before_answer.delete(0, 'end')
    latest_answer.delete(0, 'end')
    calendarID_answer.delete(0, 'end')

def submit_all():
    time_before = before_answer.get()
    time_latest = latest_answer.get()
    CalendarId = calendarID_answer.get()
    Id = open('textDocs/calendarId.txt', 'w')
    Id.write(CalendarId)
    Id.close()
    times = open('textDocs/times.txt', 'w')
    times.write(time_before + '\n' + time_latest)
    times.close()
    submitAllButton.after(0, delete_all)


def go_back():
    if (exists('textDocs/calendarId.txt') == False or exists('textDocs/times.txt') == False):
        problem.place(x=5, y=400)
    else:
        problem.place_forget()
        subprocess.Popen(['Python', 'settings.py'])
        sys.exit(0)

# -------------------------------------------------------------------------------------------------------------- #
# --- background interface --- #

calendar = Tk()
calendar.geometry("800x480")
calendar.config(background='grey')
#background.attributes('-fullscreen', True)

# -------------------------------------------------------------------------------------------------------------- #
# --- alarm time before first meeting --- #

before_question = Label(calendar, text="How long before your first meeting do you want to wake up?\n(HH:MM)", background="grey", foreground="white", font=("BloomSpeak Body", 10))
before_question.pack(anchor="center")

before_answer = Entry(calendar)
before_answer.config(font=("BloomSpeak Body", 15), width=5)
before_answer.pack(anchor="center")

deleteBeforeButton = Button(calendar, text="delete", command=delete_before, font=("BloomSpeak Body", 10), width= 10)
deleteBeforeButton.place(x=5,y=140)

submitBeforeButton = Button(calendar, text="submit", command=submit_before, font=("BloomSpeak Body", 10), width= 10)
submitBeforeButton.place(x=5,y=70)

# -------------------------------------------------------------------------------------------------------------- #
# --- latest alarm time --- #

latest_question = Label(calendar, text="What is the latest moment the Alarm should go off?\n(HH:MM)", background="grey", foreground="white", font=("BloomSpeak Body", 15))
latest_question.pack(anchor="center")

latest_answer = Entry(calendar)
latest_answer.config(font=("BloomSpeak Body", 25), width=40)
latest_answer.pack(anchor="center")

deleteLatestButton = Button(calendar, text="delete", command=delete_latest, font=("BloomSpeak Body", 10), width= 10)
deleteLatestButton.place(x=50,y=140)

submitLatestButton = Button(calendar, text="submit", command=submit_latest, font=("BloomSpeak Body", 10), width= 10)
submitLatestButton.place(x=50,y=70)

# -------------------------------------------------------------------------------------------------------------- #
# --- calendarid --- #

calendarId_question = Label(calendar, text="calendarID", background="grey", foreground="white", font=("BloomSpeak Body", 15))
calendarId_question.pack(anchor="center")

calendarID_answer = Entry(calendar)
calendarID_answer.config(font=("BloomSpeak Body", 25), width=40)
calendarID_answer.pack(anchor="center")

deleteCalendarIdButton = Button(calendar, text="delete", command=delete_calendarId, font=("BloomSpeak Body", 10), width= 10)
deleteCalendarIdButton.place(x=105,y=140)

submitCalendarIdButton = Button(calendar, text="submit", command=submit_calendarId, font=("BloomSpeak Body", 10), width= 10)
submitCalendarIdButton.place(x=105,y=70)

CalendarIdButton = Button(calendar, text="How to get", command=calendarId, font=("BloomSpeak Body", 10), width= 10)
CalendarIdButton.place(x=105,y=210)

resetToken = Button(calendar, text="reset Token", command=reset_token, font=("BloomSpeak Body", 10), width= 10)
resetToken.place(x=105,y=280)

# -------------------------------------------------------------------------------------------------------------- #
# --- delete and submit all -- #

deleteAllButton = Button(calendar, text="delete", command=delete_all, font=("BloomSpeak Body", 5), width= 5)
deleteAllButton.pack(anchor="center")

submitAllButton = Button(calendar, text="submit", command=submit_all, font=("BloomSpeak Body", 5), width= 5)
submitAllButton.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #
# --- delete and submit all -- #

problem = Label(calendar, text="Not everything is filled in", font=("BloomSpeak Body", 15), background='grey', foreground='red')

# -------------------------------------------------------------------------------------------------------------- #
# --- back to settings --- #

goBack = Button(calendar, text="go back", command=go_back, font=("BloomSpeak Body", 25), width= 25)
goBack.pack(anchor="center")

# -------------------------------------------------------------------------------------------------------------- #

calendar.mainloop()
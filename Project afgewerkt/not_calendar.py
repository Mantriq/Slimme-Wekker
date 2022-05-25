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
    if (time_before != ''):
        if (exists("/home/slimmewekker/Documenten/Project/textDocs/times.txt") == True):
            times = open('/home/slimmewekker/Documenten/Project/textDocs/times.txt', 'r')
            time_latest = times.readlines()[1]
            times.close()
        else:
            time_latest = '1'
        times = open('/home/slimmewekker/Documenten/Project/textDocs/times.txt', 'w')
        times.write(time_before + '\n' + time_latest)
        times.close()
    submitBeforeButton.after(0, delete_before)

def delete_latest():
    latest_answer.delete(0, 'end')

def submit_latest():
    time_latest = latest_answer.get()
    if (time_latest != ''):
        if (exists("/home/slimmewekker/Documenten/Project/textDocs/times.txt") == True):
            times = open('/home/slimmewekker/Documenten/Project/textDocs/times.txt', 'r')
            time_before = times.readlines()[0]
            times.close()
        else:
            time_before = '\n'
        times = open('/home/slimmewekker/Documenten/Project/textDocs/times.txt', 'w')
        times.write(time_before + time_latest)
        times.close()
    submitLatestButton.after(0, delete_latest)

def delete_calendarId():
    calendarID_answer.delete(0, 'end')

def submit_calendarId():
    CalendarId = calendarID_answer.get()
    if (CalendarId != ''):
        Id = open('/home/slimmewekker/Documenten/Project/textDocs/calendarId.txt', 'w')
        Id.write(CalendarId)
        Id.close()
    submitCalendarIdButton.after(0, delete_calendarId)
    
def calendarId():
    webbrowser.get('firefox').open('https://www.sociablekit.com/get-find-google-calendar-id/')

def reset_token():
    if (exists('/home/slimmewekker/Documenten/Project/token.json') == True):
        os.remove('/home/slimmewekker/Documenten/Project/token.json')
    subprocess.call(['python', '/home/slimmewekker/Documenten/Project/calendar_API.py'])

def delete_all():
    before_answer.delete(0, 'end')
    latest_answer.delete(0, 'end')
    calendarID_answer.delete(0, 'end')

def submit_all():
    time_before = before_answer.get()
    time_latest = latest_answer.get()
    CalendarId = calendarID_answer.get()
    if (time_before != '' and time_latest != ''):
        times = open('/home/slimmewekker/Documenten/Project/textDocs/times.txt', 'w')
        times.write(time_before + '\n' + time_latest)
        times.close()
    if (CalendarId != ''):
        Id = open('/home/slimmewekker/Documenten/Project/textDocs/calendarId.txt', 'w')
        Id.write(CalendarId)
        Id.close()
    submitAllButton.after(0, delete_all)


def go_back():
    if (exists('/home/slimmewekker/Documenten/Project/textDocs/times.txt') == True):
        times = open('/home/slimmewekker/Documenten/Project/textDocs/times.txt', 'r')
        time = times.read().splitlines()
        time_before = time[0]
        time_latest = time[1]
        times.close()
    else:
        time_before = ''
        time_latest = '1'
    if (exists('/home/slimmewekker/Documenten/Project/textDocs/calendarId.txt') == False or time_before == '' or time_latest == '1'):
        problem.place(x=15, y=320)
    else:
        problem.place_forget()
        calendar.destroy()
        subprocess.call(['python', '/home/slimmewekker/Documenten/Project/settings.py'])

# -------------------------------------------------------------------------------------------------------------- #
# --- background interface --- #

calendar = Tk()
calendar.config(background='grey')
calendar.attributes('-fullscreen', True)

# -------------------------------------------------------------------------------------------------------------- #
# --- alarm time before first meeting --- #

before_question = Label(calendar, text="Aantal uur/uren voor de eerste afspraak dat\nuw alarm moet afgaan.  (HH:MM)", background="grey", foreground="white", font=("BloomSpeak Body", 20), width=45, anchor="w")
before_question.place(x=15, y=15)
before_answer = Entry(calendar)
before_answer.config(font=("BloomSpeak Body", 20), width=27)
before_answer.place(x=15, y=85)

deleteBeforeButton = Button(calendar, text="verwijderen", command=delete_before, font=("BloomSpeak Body", 15), width=10)
deleteBeforeButton.place(x=640,y=85)
submitBeforeButton = Button(calendar, text="bevestigen", command=submit_before, font=("BloomSpeak Body", 15), width= 10)
submitBeforeButton.place(x=480,y=85)

# -------------------------------------------------------------------------------------------------------------- #
# --- latest alarm time --- #

latest_question = Label(calendar, text="Het uur waartegen het alarm zeker moet af gaan.\n(HH:MM)", background="grey", foreground="white", font=("BloomSpeak Body", 20), anchor="w")
latest_question.place(x=15, y=125)
latest_answer = Entry(calendar)
latest_answer.config(font=("BloomSpeak Body", 20), width=27)
latest_answer.place(x=15, y=195)

deleteLatestButton = Button(calendar, text="verwijderen", command=delete_latest, font=("BloomSpeak Body", 15), width= 10)
deleteLatestButton.place(x=640,y=195)
submitLatestButton = Button(calendar, text="bevestigen", command=submit_latest, font=("BloomSpeak Body", 15), width= 10)
submitLatestButton.place(x=480,y=195)

# -------------------------------------------------------------------------------------------------------------- #
# --- calendarid --- #

calendarId_question = Label(calendar, text="calendarID", background="grey", foreground="white", font=("BloomSpeak Body", 20), anchor="w")
calendarId_question.place(x=15, y=235)
calendarID_answer = Entry(calendar)
calendarID_answer.config(font=("BloomSpeak Body", 20), width=27)
calendarID_answer.place(x=15, y=275)

deleteCalendarIdButton = Button(calendar, text="verwijderen", command=delete_calendarId, font=("BloomSpeak Body", 15), width= 10)
deleteCalendarIdButton.place(x=640,y=275)
submitCalendarIdButton = Button(calendar, text="bevestigen", command=submit_calendarId, font=("BloomSpeak Body", 15), width= 10)
submitCalendarIdButton.place(x=480,y=275)
CalendarIdButton = Button(calendar, text="Waar haal je ID", command=calendarId, font=("BloomSpeak Body", 15), width= 10)
CalendarIdButton.place(x=640,y=315)
resetToken = Button(calendar, text="nieuwe Token", command=reset_token, font=("BloomSpeak Body", 15), width= 10)
resetToken.place(x=480,y=315)

# -------------------------------------------------------------------------------------------------------------- #
# --- delete and submit all -- #

deleteAllButton = Button(calendar, text="verwijder alles", command=delete_all, font=("BloomSpeak Body", 15), width= 23)
deleteAllButton.place(x=480, y=440)
submitAllButton = Button(calendar, text="bevestig alles", command=submit_all, font=("BloomSpeak Body", 15), width= 23)
submitAllButton.place(x=480, y=400)

# -------------------------------------------------------------------------------------------------------------- #
# --- probleem -- #

problem = Label(calendar, text="Er ontbreken nog wat onderdelen\nom de wekker te laten werken", font=("BloomSpeak Body", 20), background='grey', foreground='red')

# -------------------------------------------------------------------------------------------------------------- #
# --- back to settings --- #

goBack = Button(calendar, text="ga terug", command=go_back, font=("BloomSpeak Body", 30), width= 10)
goBack.place(y=418)

# -------------------------------------------------------------------------------------------------------------- #

calendar.mainloop()
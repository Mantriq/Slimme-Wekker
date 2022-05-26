from tracemalloc import start
import requests
import sys
import subprocess
from tkinter import *
from time import strftime
from os.path import exists
from multiprocessing import Process, Queue
import datetime
import pygame.mixer
import webbrowser

# --- functions --- #

def open_settings():
    interface.destroy()
    subprocess.call(["python", "/home/slimmewekker/Documenten/Project/settings.py"])

# --- icoontje geven afhankelijk van het weer --- interface.py --- #
def live_weather_icon():
    if (exists("/home/slimmewekker/Documenten/Project/textDocs/City_Weather.txt") == True):
        city_weather = open("/home/slimmewekker/Documenten/Project/textDocs/City_Weather.txt", 'r')
        city = city_weather.read()
        user_input = city
        city_weather.close()

        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID=9e0cc0262cd61c5a77a4cdaaf5fb209e")

        weather = weather_data.json()['weather'][0]['main']

        #https://openweathermap.org/weather-conditions
        if (weather == 'Clear'):
            icon = "/home/slimmewekker/Documenten/Project/Weather_Icons/Clear_Icon.png"
        elif (weather == 'Clouds'):
            icon = "/home/slimmewekker/Documenten/Project/Weather_Icons/Clouds_Icon.png"
        elif (weather == 'Snow'):
            icon = "/home/slimmewekker/Documenten/Project/Weather_Icons/Snow_Icon.png"
        elif (weather == 'Rain'):
            icon = "/home/slimmewekker/Documenten/Project/Weather_Icons/Rain_Icon.png"
        elif (weather == 'Drizzle'):
            icon = "/home/slimmewekker/Documenten/Project/Weather_Icons/Drizzle_Icon.png"
        elif (weather == 'Thunderstorm'):
            icon = "/home/slimmewekker/Documenten/Project/Weather_Icons/Thunderstorm_Icon.png"
        else:
            icon = "/home/slimmewekker/Documenten/Project/Weather_Icons/Blank_Icon.png"
    else:
            icon = "/home/slimmewekker/Documenten/Project/Weather_Icons/Blank_Icon.png"
        
    icon_weather.config(file=icon)
    image_weather.after(1000, live_weather_icon)

# --- temperatuur geven dat het op de locatie is --- interface.py --- #
def live_weather_temp():
    if (exists("/home/slimmewekker/Documenten/Project/textDocs/City_Weather.txt") == True):
        city_weather = open("/home/slimmewekker/Documenten/Project/textDocs/City_Weather.txt", 'r')
        city = city_weather.read()
        city_weather.close()

        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID=9e0cc0262cd61c5a77a4cdaaf5fb209e")

        temperature = weather_data.json()['main']['temp']
        temperature = int(temperature)
        temperature = str(temperature) + '°'
    else:
        temperature = 'N/A'

    temp_weather.config(text=temperature)
    temp_weather.after(1000, live_weather_temp)

def live_time():
    time = strftime('%H:%M')
    clock.config(text=time)
    clock.after(1000, live_time)

# --- alarm geluid --- #
def alarm():
    if (exists("/home/slimmewekker/Documenten/Project/textDocs/music.txt") == True):
        musicFile = open("/home/slimmewekker/Documenten/Project/textDocs/music.txt", 'r')
        music = musicFile.read()
        musicFile.close()
        pygame.mixer.init()
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)
        
        time = open("/home/slimmewekker/Documenten/Project/textDocs/alarmtime.txt", "r")
        alarm_time = time.read()
        time.close()

        alarmMinutes = alarm_time[3:5]
        alarmMinutes = int(alarmMinutes)
        alarmMinutes = alarmMinutes - 1
        alarmMinutes = str(alarmMinutes)

        alarmHours = alarm_time[0:2]
        alarmSeconds = alarm_time[6:8]
        alarm_time = alarmHours + ":" + alarmMinutes + ":" + alarmSeconds

        time = open("/home/slimmewekker/Documenten/Project/textDocs/alarmtime.txt", "w")
        time.write(alarm_time)
        time.close()    
    elif (exists("/home/slimmewekker/Documenten/Project/textDocs/youtube.txt") == True):
        musicFile = open("/home/slimmewekker/Documenten/Project/textDocs/youtube.txt", 'r')
        music = musicFile.read()
        musicFile.close()
        
        webbrowser.get('firefox').open(music)
        
        time = open("/home/slimmewekker/Documenten/Project/textDocs/alarmtime.txt", "r")
        alarm_time = time.read()
        time.close()

        alarmMinutes = alarm_time[3:5]
        alarmMinutes = int(alarmMinutes)
        alarmMinutes = alarmMinutes - 1
        alarmMinutes = str(alarmMinutes)

        alarmHours = alarm_time[0:2]
        alarmSeconds = alarm_time[6:8]
        alarm_time = alarmHours + ":" + alarmMinutes + ":" + alarmSeconds

        time = open("/home/slimmewekker/Documenten/Project/textDocs/alarmtime.txt", "w")
        time.write(alarm_time)
        time.close()

# --- ziet wanneer alarm moet af gaan --- interface.py --- #
def startAlarm():
    time = open("/home/slimmewekker/Documenten/Project/textDocs/alarmtime.txt", "r")
    alarm_time = time.read()
    time.close()
    alarm_hours = alarm_time[0:2]
    alarm_minutes = alarm_time[3:5]

    current_hour = strftime('%H')
    current_min = strftime('%M')

    alarmStartButton.after(1000, startAlarm)

    if alarm_hours == current_hour:
        if alarm_minutes == current_min:
                
            alarmStartButton.place(anchor="nw", y=413, x=200)
            alarmSnoozeButton.place(anchor="nw", y=413, x=400)
            alarm()

# --- stopt het alarm --- #
def stopAlarm():
    alarmStartButton.place_forget()
    alarmSnoozeButton.place_forget()
    pygame.mixer.music.stop()

# --- stopt het alarm en laat het 5 minuten later terug afgaan --- #
def snoozeAlarm():
    time = open("/home/slimmewekker/Documenten/Project/textDocs/alarmtime.txt", "r")
    alarm_time = time.read()
    time.close()

    alarmMinutes = alarm_time[3:5]
    alarmMinutes = int(alarmMinutes)
    alarmMinutes = alarmMinutes + 6
    alarmMinutes = str(alarmMinutes)

    alarmHours = alarm_time[0:2]
    alarmSeconds = alarm_time[6:8]
    alarm_time = alarmHours + ":" + alarmMinutes + ":" + alarmSeconds

    time = open("/home/slimmewekker/Documenten/Project/textDocs/alarmtime.txt", "w")
    time.write(alarm_time)
    time.close()

    alarmStartButton.place_forget()
    alarmSnoozeButton.place_forget()
    pygame.mixer.music.stop()

    

# -------------------------------------------------------------------------------------------------------------- #
# --- background interface --- #

interface = Tk()
interface.config(background='grey')
interface.attributes('-fullscreen', True)

# -------------------------------------------------------------------------------------------------------------- #
# --- settings button --- #

setting_image = PhotoImage(file="/home/slimmewekker/Documenten/Project/images/Settings_LOGO.png").subsample(7,7)
settings_button = Button(interface, image=setting_image, borderwidth=0, command=open_settings)
settings_button.place(anchor="nw")

# -------------------------------------------------------------------------------------------------------------- #
# --- weather --- #

icon_weather = PhotoImage()
image_weather = Label(interface, image=icon_weather, borderwidth=0)
image_weather.place(anchor="nw", x=560)
live_weather_icon()

temp_weather = Label(interface, font=("BloomSpeak Body", 40), background="grey", foreground="white")
temp_weather.place(anchor="nw", x=680, y=30)
live_weather_temp()

# -------------------------------------------------------------------------------------------------------------- #
# --- clock --- #

clock = Label(interface, font=("BloomSpeak Body", 180), background="grey", foreground="white")
clock.place(anchor="nw", x=50, y=100)
live_time()

# -------------------------------------------------------------------------------------------------------------- #
# --- Alarm button --- #

alarmStartButton = Button(interface, text=("Stop"), font=("BloomSpeak Body", 20), width=10, command=stopAlarm)
alarmSnoozeButton = Button(interface, text=("Snooze"), font=("BloomSpeak Body", 20), width=10, command=snoozeAlarm)
startAlarm()

# -------------------------------------------------------------------------------------------------------------- #

interface.mainloop()
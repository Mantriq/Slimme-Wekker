import requests
import sys
import subprocess
from tkinter import *
from time import strftime
from os.path import exists

# --- functions --- #

def open_calender():
    settings.destroy()
    subprocess.call(["python", "/home/slimmewekker/Documenten/Project/not_calendar.py"])

def open_weather():
    settings.destroy()
    subprocess.call(["python", "/home/slimmewekker/Documenten/Project/not_weather.py"])

def open_music():
    settings.destroy()
    subprocess.call(["python", "/home/slimmewekker/Documenten/Project/music.py"])

def go_back():
    settings.destroy()
    subprocess.call(["python", "/home/slimmewekker/Documenten/Project/interface.py"])
    
def exit():
    settings.destroy()

def weather_type():
    if (exists("/home/slimmewekker/Documenten/Project/textDocs/City_Weather.txt") == True):
        city_weather = open("/home/slimmewekker/Documenten/Project/textDocs/City_Weather.txt", 'r')
        city = city_weather.read()
        city_weather.close()

        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID=9e0cc0262cd61c5a77a4cdaaf5fb209e")

        weather = weather_data.json()['weather'][0]['main']
    else: 
        weather = "N/A"

    return weather

def weather_temperature():
    if (exists("/home/slimmewekker/Documenten/Project/textDocs/City_Weather.txt") == True):
        city_weather = open("/home/slimmewekker/Documenten/Project/textDocs/City_Weather.txt", 'r')
        city = city_weather.read()
        city_weather.close()

        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID=9e0cc0262cd61c5a77a4cdaaf5fb209e")

        temperature = weather_data.json()['main']['temp']
    else:
        temperature = "N/A"

    return temperature

def live_weather_icon():
    weather = weather_type()
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
        
    icon_weather.config(file=icon)
    image_weather.after(1000, live_weather_icon)
    image_weather.after(1000, weather_type)


def live_weather_temp():
    temperature = weather_temperature()
    if (temperature != "N/A"):
        temperature = int(temperature)
        temperature = str(temperature)
        temperature = temperature + '°'

    temp_weather.config(text=temperature)
    temp_weather.after(1000, live_weather_temp)
    temp_weather.after(1000, weather_temperature)

# --- gedetailleerd weerbericht --- settings.py --- #
def live_details():
    weather = weather_type()
    if (weather == 'Clear'):
        weather = "helder"
    elif (weather == 'Clouds'):
        weather = "bewolkt"
    elif (weather == 'Snow'):
        weather = "sneeuw"
    elif (weather == 'Rain'):
        weather = "regen"
    elif (weather == 'Drizzle'):
        weather = "drassig"
    elif (weather == 'Thunderstorm'):
        weather = "onweer"
    else:
        weather = "N/A"

    if (exists("/home/slimmewekker/Documenten/Project/textDocs/City_Weather.txt") == True):
        city_weather = open("/home/slimmewekker/Documenten/Project/textDocs/City_Weather.txt", 'r')
        city = city_weather.read()
        city_weather.close()
    else:
        city = "N/A"

    day = strftime('%w')
    day = int(day)
    if (day == 0):
        day = "zondag"
    elif (day == 1):
        day = "maandag"
    elif (day == 2):
        day = "dinsdag"
    elif (day == 3):
        day = "woensdag"
    elif (day == 4):
        day = "donderdag"
    elif (day == 5):
        day = "vrijdag"
    elif (day == 6):
        day = "zaterdag"
    else:
        day = "N/A"
        
    detail = weather + ', ' + city + ', ' + day
    detailed_info.config(text=detail)
    detailed_info.after(1000,live_details)

def live_time():
    time = strftime('%H:%M')
    clock.config(text=time)
    clock.after(1000, live_time)

# -------------------------------------------------------------------------------------------------------------- #
# --- background interface --- #

settings = Tk()
settings.config(background="grey")
settings.attributes('-fullscreen', True)

# -------------------------------------------------------------------------------------------------------------- #
# --- setting buttons --- #

calendarButton = Button(settings, text=("kalender"), font=("BloomSpeak Body", 20), width=10, command=open_calender)
calendarButton.place(anchor="nw")

weatherButton = Button(settings, text=("weer"), font=("BloomSpeak Body", 20), width=10, command=open_weather)
weatherButton.place(x=200)

musicButton = Button(settings, text=("muziek"), font=("BloomSpeak Body", 20), width=10, command=open_music)
musicButton.place(x=400)

backButton = Button(settings, text=("home"), font=("BloomSpeak Body", 20), width=10, command=go_back)
backButton.place(x=600)

exitButton = Button(settings, text=("sluiten"), font=("BloomSpeak Body", 20), width=10, command=exit)
exitButton.place(x=600, y=432)

# -------------------------------------------------------------------------------------------------------------- #
# --- weather --- #

icon_weather = PhotoImage()
image_weather = Label(settings, image=icon_weather, borderwidth=0)
image_weather.place(anchor="nw", y=320)
live_weather_icon()

temp_weather = Label(settings, font=("BloomSpeak Body", 40), background="grey", foreground="white")
temp_weather.place(anchor="nw", x=120, y=350)
live_weather_temp()

# -------------------------------------------------------------------------------------------------------------- #
# --- detailed description --- #

detailed_info = Label(settings, font=("BloomSpeak Body", 30), background="grey", foreground="white")
detailed_info.place(anchor="nw", x=15, y=425)
live_details()

# -------------------------------------------------------------------------------------------------------------- #
# --- clock --- #

clock = Label(settings, font=("BloomSpeak Body", 140), background="grey", foreground="white")
clock.place(x=120, y=100, anchor="nw")
live_time()

# -------------------------------------------------------------------------------------------------------------- #

settings.mainloop()
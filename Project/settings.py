import requests
import sys
import subprocess
from tkinter import *
from time import strftime
from os.path import exists


# --- functions --- #

def open_calender():
    subprocess.Popen(['Python', 'not_calendar.py'])
    sys.exit(0)

def open_weather():
    subprocess.Popen(['Python', 'not_weather.py'])
    sys.exit(0)

def go_back():
    subprocess.Popen(['Python', 'interface.py'])
    sys.exit(0)

def weather_type():
    if (exists("City_Weather.txt") == True):
        city_weather = open("City_Weather.txt", 'r')
        city = city_weather.read()
        city_weather.close()

        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID=9e0cc0262cd61c5a77a4cdaaf5fb209e")

        weather = weather_data.json()['weather'][0]['main']
    else: 
        weather = "N/A"

    return weather

def weather_temperature():
    if (exists("City_Weather.txt") == True):
        city_weather = open("City_Weather.txt", 'r')
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
        icon = "Weather_Icons/Clear_Icon.png"
    elif (weather == 'Clouds'):
        icon = "Weather_Icons/Clouds_Icon.png"
    elif (weather == 'Snow'):
        icon = "Weather_Icons/Snow_Icon.png"
    elif (weather == 'Rain'):
        icon = "Weather_Icons/Rain_Icon.png"
    elif (weather == 'Drizzle'):
        icon = "Weather_Icons/Drizzle_Icon.png"
    elif (weather == 'Thunderstorm'):
        icon = "Weather_Icons/Thunderstorm_Icon.png"
    else:
        icon = "Weather_Icons/Blank_Icon.png"
        
    icon_weather.config(file=icon)
    image_weather.after(1000, live_weather_icon)


def live_weather_temp():
    temperature = weather_temperature()
    if (temperature != "N/A"):
        temperature = int(temperature)
        temperature = str(temperature)
        temperature = temperature + '°'

    temp_weather.config(text=temperature)
    temp_weather.after(1000, live_weather_temp)

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

    if (exists("City_Weather.txt") == True):
        city_weather = open("City_Weather.txt", 'r')
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
settings.geometry("800x480")
settings.config(background="grey")
#settings.attributes('-fullscreen', True)

# -------------------------------------------------------------------------------------------------------------- #
# --- setting buttons --- #

calendarButton = Button(settings, text=("Calender"), font=("BloomSpeak Body", 33), width=10, command=open_calender)
calendarButton.place(anchor="nw")

weatherButton = Button(settings, text=("Weather"), font=("BloomSpeak Body", 33), width=10, command=open_weather)
weatherButton.place(x=265, anchor="nw")

backButton = Button(settings, text=("Go back"), font=("BloomSpeak Body", 33), width=10, command=go_back)
backButton.place(x=530, anchor="nw")

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
clock.place(x=160, y=140, anchor="nw")
live_time()

# -------------------------------------------------------------------------------------------------------------- #

settings.mainloop()
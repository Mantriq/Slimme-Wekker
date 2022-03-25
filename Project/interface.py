import requests
import sys
import subprocess
from tkinter import *
from time import strftime
from os.path import exists

# --- functions --- #

def open_settings():
    subprocess.Popen(['Python', 'settings.py'])
    sys.exit(0)

def live_weather_icon():
    if (exists("City_Weather.txt") == True):
        city_weather = open("City_Weather.txt", 'r')
        city = city_weather.read()
        user_input = city
        city_weather.close()

        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID=9e0cc0262cd61c5a77a4cdaaf5fb209e")

        weather = weather_data.json()['weather'][0]['main']

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
    if (exists("City_Weather.txt") == True):
        city_weather = open("City_Weather.txt", 'r')
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

# -------------------------------------------------------------------------------------------------------------- #
# --- background interface --- #

interface = Tk()
interface.geometry("800x480")
interface.config(background='grey')
#interface.attributes('-fullscreen', True)

# -------------------------------------------------------------------------------------------------------------- #
# --- settings button --- #

setting_image = PhotoImage(file="Settings_LOGO.png").subsample(7,7)
settings_button = Button(interface, image=setting_image, borderwidth=0, command=open_settings)
settings_button.place(anchor="nw")

# -------------------------------------------------------------------------------------------------------------- #
# --- weather --- #

icon_weather = PhotoImage()
image_weather = Label(interface, image=icon_weather, borderwidth=0)
image_weather.place(anchor="nw", x=590)
live_weather_icon()

temp_weather = Label(interface, font=("BloomSpeak Body", 40), background="grey", foreground="white")
temp_weather.place(anchor="nw", x=710, y=30)
live_weather_temp()

# -------------------------------------------------------------------------------------------------------------- #
# --- clock --- #

clock = Label(interface, font=("BloomSpeak Body", 180), background="grey", foreground="white")
clock.place(anchor="nw", x=100, y=100)
live_time()

# -------------------------------------------------------------------------------------------------------------- #

interface.mainloop()
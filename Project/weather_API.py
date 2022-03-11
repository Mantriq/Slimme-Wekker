import requests
from not_weather import submit


api_key = "9e0cc0262cd61c5a77a4cdaaf5fb209e"

user_input = submit

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

print(weather_data)

weer = weather_data.json()['weather'][0]['main']
temp = weather_data.json()['main']['temp']


print(weer, temp)
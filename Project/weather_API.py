import requests


api_key = "9e0cc0262cd61c5a77a4cdaaf5fb209e"

city_weather = open("City_Weather.txt", 'r')
city = city_weather.read()
user_input = city

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID=9e0cc0262cd61c5a77a4cdaaf5fb209e")

weer = weather_data.json()['weather'][0]['main']
temp = weather_data.json()['main']['temp']


print(weer, temp)
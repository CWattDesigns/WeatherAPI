import datetime as dt
import requests
from datetime import timezone

# Need to fetch the API key from the Openweathmap.org
API_KEY = "************************"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
city = input("Enter a city name: \n")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url).json()

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'], timezone.utc)
sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'], timezone.utc)

print(f"\nTemperature in {city}: {temp_celsius:.2f}C or {temp_fahrenheit:.2f}F")
print(f"Temperature in {city} feels like: {feels_like_celsius:.2f}C or {feels_like_fahrenheit:.2f}F")
print(f"Humidity in {city}: {humidity}%")
print(f"Wind Speed in {city}: {wind_speed}m/s")
print(f"General Weather in {city}: {description}")
print(f"Sun rises in {city} at {sunrise_time} UTC.")
print(f"Sun sets in {city} at {sunset_time} UTC.")

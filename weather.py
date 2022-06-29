from turtle import speed
import requests
import json

from yarl import URL
API_key="aebc970628b8d843435b3ad3a22e3012"
city_name= input("Enter your city name:")
URL= f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"

res =requests.get(URL)
json_data= json.loads(res.text)
weather=json_data["weather"][0]["description"]
temprature=json_data["main"]["temp"]
humidity=json_data["main"]["humidity"]
wind_speed=json_data["wind"]["speed"]

print(f"weather:{weather}")
print(f"temprature:{temprature}")
print(f"humidity:{humidity}")
print(f"wind_speed:{wind_speed}")

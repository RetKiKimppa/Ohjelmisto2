import requests
import json


apikey ="88faf3a8a3b1ba95a7d7c4f7e10fd621"
city_name = input("City: ")

request = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={apikey}&units=metric"
response = requests.get(request).json()

print(response["weather"][0]["main"])
print(f"{response['main']['temp']} °C")


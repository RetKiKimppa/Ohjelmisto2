import requests
import json


apikey ="input ur key here"
city_name = input("City: ")

request = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={apikey}&units=metric"
response = requests.get(request).json()

print(response["weather"][0]["main"])
print(f"{response['main']['temp']} °C")


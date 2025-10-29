import requests
import json


apikey ="22cad3a7f5cb97a3610bd42ddd60b0a3"
city_name = input("City: ")

request = f"https://api.openweathermap.org/data/2.5/weather?q=${city_name}&appid=${apikey}&units=metric"
response = requests.get(request).json()
print(json.dumps(response, indent=4))


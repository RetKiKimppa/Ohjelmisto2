import json
import requests

word = input("Anna hakusana: ")

request = "https://api.tvmaze.com/search/shows?q=" + word


try:
    response = requests.get(request)

    if not response.ok:
        print("jokin meni pieleen")

    shows = response.json()

    if len(shows)==0:
        print("Ei tuloksia")

    for sarja in shows:
        print(sarja["show"]["name"])

except requests.exceptions.RequestException as e:
    print(f"Virheilmoitus: Haussa")
except Exception as e:
    print(e)
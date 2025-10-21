from classes.auto import Auto

auto1 = Auto("ABC-321", 249)

print(f"""
Rekisteritunnus: {auto1.rekkari}
Huippunopeus: {auto1.huippunopeus} km/h
Hetkellinen nopeus: {auto1.nopeus} km/h
Matka: {auto1.matka} km
""")
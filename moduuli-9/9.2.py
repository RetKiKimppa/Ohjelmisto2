from classes.auto import Auto

autot = []

auto1 = Auto("ABC-321", 249)
auto2 = Auto("LSJ-222", 300)
auto3 = Auto("SFS-132", 150)
auto4 = Auto("DKD-416", 400)

autot.append(auto1)
autot.append(auto2)
autot.append(auto3)
autot.append(auto4)

for auto in autot:
    print(f"""
    Rekisteritunnus: {auto.rekkari}
    Huippunopeus: {auto.huippunopeus} km/h
    Hetkellinen nopeus: {auto.nopeus} km/h
    Matka: {auto.matka} km
    """)
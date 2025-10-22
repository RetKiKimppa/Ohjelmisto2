from classes.auto import Auto

auto1 = Auto("ABC-321", 249)

print(f"""
Rekisteritunnus: {auto1.rekkari}
Huippunopeus: {auto1.huippunopeus} km/h
Hetkellinen nopeus: {auto1.nopeus} km/h
Matka: {auto1.matka} km
""")

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
auto1.kulje(1.5)

print(f"""
Hetkellinen nopeus: {auto1.nopeus} km/h
Matka: {auto1.matka} km
""")

auto1.kiihdyta(-200)

print(f"""
Hetkellinen nopeus: {auto1.nopeus} km/h
Matka: {auto1.matka} km
""")

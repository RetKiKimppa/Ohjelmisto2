from classes.auto import Auto
import random

autot = []

for i in range(1, 11):
    huippunopeus = random.randint(100, 200)
    autot.append(Auto("ABC-" + str(i), huippunopeus))

autokilpailu = True
while autokilpailu:
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)
        auto.kulje(1)

    for auto in autot:
        if auto.matka >= 10000:
            autokilpailu = False



for a in autot:
    print(f"{a.rekkari} {a.matka} km")




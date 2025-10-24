import random
from classes.kilpailu import Kilpailu
from classes.auto import Auto


autot = []

for i in range(1, 11):
    huippunopeus = random.randint(100, 200)
    autot.append(Auto("ABC-" + str(i), huippunopeus))

suuriromuralli = Kilpailu("Suuri Romuralli", 8000, autot)


kulununeet_tunnit = 0
while not suuriromuralli.kilpailu_ohi():
    suuriromuralli.tunti_kuluu()
    kulununeet_tunnit += 1
    if kulununeet_tunnit % 10 == 0:
        print(f"Kilpailua kulunut {kulununeet_tunnit} tuntia.")
        suuriromuralli.tulosta_tilanne()

print(f"Kilpailu on ohi! Kilpailu kesti {kulununeet_tunnit} tuntia.\nLopputilanne:")
suuriromuralli.tulosta_tilanne()

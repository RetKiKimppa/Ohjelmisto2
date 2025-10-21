from classes.auto import Auto
import random


autot = []

for i in range(1, 11):
    #arvo huippunopeus 100-200
    huippunopeus = random.randint(100, 200)
    autot.append(Auto("ABC-" + str(i), huippunopeus))

kokonaismatka = 0
while kokonaismatka < 10000:
    for auto in autot:
        #arvo nopeuden muutos
        #kutsu kiihdytä
        auto.kulje(1)
        #hae matkan arvo, jos yli 10000, lopeta kisa asettamalla autonmatka kokonaismatkaksi


#googlaa joku talukkokirjasto tulostamiseen, python table libary
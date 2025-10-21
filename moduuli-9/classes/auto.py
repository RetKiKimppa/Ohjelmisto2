class Auto:
    def __init__(self, rekkari:str, huippunopeus:int):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, arvo:int):
        if arvo > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif arvo < 0:
            self.nopeus = 0
        else:
            self.nopeus = arvo

    def kulje(self, aika:int):
        if aika >= 0:
            self.matka = aika * self.nopeus
        else:
            print("Anna positiivinen tuntimäärä")



        #laske kuinka paljon auto on kulkenut annetussa ajassa tietyllä nopeudella
        #lisää kuljettu matka kokonais matkaan

        #ehkä metodi, joka palauttaa ominaisuudet sanakirjana.
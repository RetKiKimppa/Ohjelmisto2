class Auto:
    def __init__(self, rekkari:str, huippunopeus:int):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, arvo:int):
        self.nopeus += arvo
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0
        else:
            return

    def kulje(self, aika:int):
        if aika >= 0:
            self.matka += aika * self.nopeus
        else:
            return "Anna positiivinen tuntimäärä"


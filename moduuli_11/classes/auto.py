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

    def kulje(self, aika:int):
        if aika >= 0:
            self.matka += aika * self.nopeus
        else:
            return "Anna positiivinen tuntimäärä"

class Sähköauto(Auto):
    def __init__(self, rekkari:str, huippunopeus:int, akkukapasiteetti:float):
        super().__init__(rekkari, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekkari:str, huippunopeus:int, tankin_koko:float):
        super().__init__(rekkari, huippunopeus)
        self.tankin_koko = tankin_koko

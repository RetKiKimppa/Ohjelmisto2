class Julkaisu:
    def __init__(self, nimi:str):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi:str, kirjoittaja:str, sivumaara:int):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}, sivumäärä: {self.sivumaara}, kirjoittaja: {self.kirjoittaja}")

class Lehti(Julkaisu):
    def __init__(self, nimi:str, paatoimittaja:str):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}, päätoimittaja: {self.paatoimittaja}")


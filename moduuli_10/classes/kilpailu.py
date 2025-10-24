import random
from prettytable import PrettyTable

class Kilpailu:
    def __init__(self,kilpailu_nimi:str, kilpailu_pituus:int, autot:list):
        self.kilpailu_nimi = kilpailu_nimi
        self.kilpailu_pituus = kilpailu_pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        table = PrettyTable()
        table.field_names = ["Rekisterinumero", "Huippunopeus", "Hetkellinen nopeus", "Kuljettu matka"]
        for auto in self.autot:
            table.add_row(
                [auto.rekkari, str(auto.huippunopeus) + "km/h", str(auto.nopeus) + "km/h", str(auto.matka) + "km"])
        print(table)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.kilpailu_pituus:
                return True
        return False



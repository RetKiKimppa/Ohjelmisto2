import textwrap

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros

    def kerros_ylos(self):
        self.kerros += 1
        print(f" Olet kerroksessa numero: {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f" Olet kerroksessa numero: {self.kerros}")

    def siirry_kerrokseen(self, new_kerros:int):
        if new_kerros > self.ylin_kerros or new_kerros < self.alin_kerros:
            print(textwrap.dedent(f"""
                Väärä syöte
                Hissin alin kerros on: {self.alin_kerros}
                Hissin ylin kerros on: {self.ylin_kerros}
                Syötä tältä väliltä
                  """))
            return
        while self.kerros != new_kerros:
            if new_kerros > self.kerros:
                self.kerros_ylos()
            elif new_kerros < self.kerros:
                self.kerros_alas()

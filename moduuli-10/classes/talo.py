from .hissi import Hissi

class Talo:
    def __init__(self,alin_kerros:int, ylin_kerros:int, hissien_lkm:int):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for i in range(hissien_lkm):
            self.hissit.append(Hissi(self.alin_kerros, self.ylin_kerros))

    def aja_hissiä(self, hissi_numero:int, kerros_numero:int):
        print(f"Ajetaan hissiä... [{hissi_numero}] ")
        self.hissit[hissi_numero - 1].siirry_kerrokseen(kerros_numero)


    def palohalytys(self):
        print("Palo hälytys käynnistetty!")
        for i, hissi in enumerate (self.hissit, start=1):
            print(f"Siirretään hissiä... [{i}] ")
            hissi.siirry_kerrokseen(self.alin_kerros)
        print("Kaikki hissit ovat nyt alimmassa kerroksessa.")



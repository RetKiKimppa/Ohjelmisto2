from classes.hissi import Hissi

h = Hissi(1, 12)

print(f""" 
alin kerros: {h.alin_kerros}
ylin kerros: {h.ylin_kerros}
kerros: {h.kerros}
""")


h.siirry_kerrokseen(5)

h.siirry_kerrokseen(12)

h.siirry_kerrokseen(1)
h.siirry_kerrokseen(13)
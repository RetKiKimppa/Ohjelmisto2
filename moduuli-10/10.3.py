from classes.talo import Talo

t = Talo(1, 12, 3)

t.aja_hissiä(2, 24)
t.aja_hissiä(1, 12)
t.aja_hissiä(1, 11)
t.aja_hissiä(2,5)
t.aja_hissiä(3, 7)

for i, hissi in enumerate(t.hissit, start=1):
    print(f"Hissi {i} on kerroksessa: {hissi.kerros}")
print("--------------------------------------")

t.palohalytys()
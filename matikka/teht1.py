from matikka.func import valilyonti
import numpy as np
import math

# Tehtävä 1:

# 1.
a = 2.493
b = 0.911

print(f"a) {np.degrees(a)}degrees")
print(f"b) {np.degrees(b)}degrees")
valilyonti()

# 2.
c = 137.7
d = 62.3

print(f"a) {np.radians(c)}rad")
print(f"b) {np.radians(d)}rad")
valilyonti()

# 3.
asteet = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
rad = np.deg2rad(asteet)

for a, r in zip(asteet, rad):
    print(f"{a}° = {r:.4f} rad")
valilyonti()

# Tehtävä 2:

kateetti_a = 1.6
kateetti_b = 2.3
hypotenuusa = np.sqrt((kateetti_a ** 2) + (kateetti_b ** 2))

print(f"Hypotenuusa: {hypotenuusa:.2f} m")


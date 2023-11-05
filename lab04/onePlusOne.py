import numpy as np
import matplotlib.pyplot as plt
import random
import math

wsp_przyrostu = 1.1
l_iteracji = 100
zakres_zmiennosci = [0, 100]
rozrzut = 10

def funkcja_przystosowania(x):
    return math.sin(x / 10.0) * math.sin(x / 200)

x_range = np.linspace(zakres_zmiennosci[0], zakres_zmiennosci[1], 100)
y_range = [funkcja_przystosowania(val) for val in x_range]

x = random.uniform(zakres_zmiennosci[0], zakres_zmiennosci[1])
y = funkcja_przystosowania(x)
print(x)

for i in range(l_iteracji):
    x_pot = x + random.uniform(-rozrzut, rozrzut)

    if x_pot < zakres_zmiennosci[0]:
        x_pot = zakres_zmiennosci[0]
    elif x_pot > zakres_zmiennosci[1]:
        x_pot = zakres_zmiennosci[1]

    y_pot = funkcja_przystosowania(x_pot)

    if y_pot >= y:
        x = x_pot
        y = y_pot
        rozrzut *= wsp_przyrostu
    elif y_pot < y:
        rozrzut /= wsp_przyrostu

    plt.plot(x_range, y_range, label="Funkcja")
    plt.scatter(x, y, c='red', label="Aktualny punkt")
    plt.xlabel("x")
    plt.ylabel("Wartość funkcji przystosowania")
    plt.legend()
    plt.title(f'Iteracja {i}')
    plt.show()
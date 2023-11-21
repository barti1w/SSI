import sys
import numpy as np
import math
import matplotlib.pyplot as plt

znak_wzorcowy_1 = np.array([
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1]
])

znak_wzorcowy_2 = np.array([
    [0, 1, 1, 1],
    [1, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
])

znak_wzorcowy_3 = np.array([
    [1, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 0]
])

znak_testowy_1 = np.array([
    [0, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1]
])

znak_testowy_2 = np.array([
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1]
])

znak_testowy_3 = np.array([
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 1]
])

wzor = [[znak_wzorcowy_1, 'znak_wzorcowy_1'], [znak_wzorcowy_2, 'znak_wzorcowy_2'], [znak_wzorcowy_3, 'znak_wzorcowy_3']]
test = [[znak_testowy_1, 'znak_testowy_1'], [znak_testowy_2, 'znak_testowy_2'], [znak_testowy_3, 'znak_testowy_3']]

def miara_podobienstwa(BA, BB):
    miara = 0
    indexBA = 0
    for pointBA in np.nditer(BA):
        indexBB = 0
        indexBA += 1
        if pointBA:
            odl_min = sys.maxsize
            for pointBB in np.nditer(BB):
                indexBB += 1
                if pointBB:
                    odl_akt = math.dist((indexBA%BA.shape[1], int(indexBA/BA.shape[1])), (int(indexBB%BB.shape[1]), int(indexBB/BB.shape[1])))
                    odl_min = min(odl_akt, odl_min)
            miara = miara + odl_min
    return miara

similar = [[], [], []]
index = -1
for ts in test:
    index = index + 1
    miara = sys.maxsize
    wzor_matrix = ''
    for wz in wzor:
        if (miara_podobienstwa(wz[0], ts[0]) + miara_podobienstwa(ts[0], wz[0])) < miara:
            miara = (miara_podobienstwa(wz[0], ts[0]) + miara_podobienstwa(ts[0], wz[0]))
            similar[index] = [wz[1], ts[1], miara_podobienstwa(wz[0], ts[0]) + miara_podobienstwa(ts[0], wz[0])]

print(similar)

plt.figure(figsize=(14, 7))

plt.subplot(2, 3, 1)
plt.imshow(znak_wzorcowy_1, cmap='binary')
plt.title('znak_wzorcowy_1')

plt.subplot(2, 3, 2)
plt.imshow(znak_wzorcowy_2, cmap='binary')
plt.title('znak_wzorcowy_2')

plt.subplot(2, 3, 3)
plt.imshow(znak_wzorcowy_3, cmap='binary')
plt.title('znak_wzorcowy_3')

plt.subplot(2, 3, 4)
plt.imshow(znak_testowy_1, cmap='binary')
plt.title('znak_testowy_1')

plt.subplot(2, 3, 5)
plt.imshow(znak_testowy_2, cmap='binary')
plt.title('znak_testowy_2')

plt.subplot(2, 3, 6)
plt.imshow(znak_testowy_3, cmap='binary')
plt.title('znak_testowy_3')

plt.show()








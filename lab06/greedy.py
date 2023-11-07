import sys
import numpy as np
import math

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
    indexBA = -1
    for pointBA in np.nditer(BA):
        indexBB = -1
        indexBA += 1
        if pointBA:
            odl_min = sys.maxsize
            for pointBB in np.nditer(BB):
                if pointBB:
                    indexBB += 1
                    # print(indexBA, indexBA%BA.shape[0], int(indexBA/BA.shape[1]))
                    odl_akt = math.dist((int(indexBA/BA.shape[1]), indexBA%BA.shape[0]), (int(indexBB/BB.shape[1]), indexBB%BB.shape[0]))
                    odl_min = min(odl_akt, odl_min)
            # print(odl_min)
            miara = miara + odl_min
        # print(miara)
    return miara

similar = [[], [], []]

for ts in test:
    index = 0
    miara = sys.maxsize
    wzor_matrix = ''
    for wz in wzor:
        print(wz[1], ts[1])
        print('miara niepodobienstwa', miara_podobienstwa(wz[0], ts[0]))
        print('miara podobienstwa obustronnego', -(miara_podobienstwa(wz[0], ts[0]) + miara_podobienstwa(ts[0], wz[0])))

        if -(miara_podobienstwa(wz[0], ts[0]) + miara_podobienstwa(ts[0], wz[0])) < miara:
            similar[index] = [wz[1], ts[1], -(miara_podobienstwa(wz[0], ts[0]) + miara_podobienstwa(ts[0], wz[0]))]
        index += 1

for x in range(len(similar)):
    print(similar[x])










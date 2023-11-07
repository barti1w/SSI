import random
import sys

import numpy as np
import math
import matplotlib.pyplot as plt

values = np.loadtxt("spirala.txt", skiprows=0, dtype='double')

m = 5
iters = 100
random_indexed = random.sample(range(values.shape[0]), m)
V = values[random_indexed]
colors = [[np.round(np.random.rand(), 1) for _ in range(3)] for _ in range(m)]

groups = {key: np.array([]).reshape(0, 2) for key in range(m)}

for _ in range(iters):
    for s in range(len(values)):
        min_distance = sys.maxsize
        for middle_point_index in range(len(V)):
            distance = math.dist(values[s], V[middle_point_index])
            if distance < min_distance:
                min_distance = distance
                u = middle_point_index
        groups[u] = np.vstack([groups[u], values[s]])
    for i in range(m):
        plt.scatter(groups[i][:, 0], groups[i][:, 1], color=colors[i])
        plt.scatter(V[i][0], V[i][1], color=colors[i], marker='d', edgecolors='black')

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("K - means")
    plt.show()

    for j in range(m):
        if len(groups[j]) > 0:
            V[j][0] = np.mean(groups[j][:, 0])
            V[j][1] = np.mean(groups[j][:, 1])
    groups = {key: np.array([]).reshape(0, 2) for key in range(m)}

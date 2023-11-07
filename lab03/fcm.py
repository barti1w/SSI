import numpy as np
import math
import matplotlib.pyplot as plt

values = np.loadtxt("spirala.txt", dtype='double')

m = 3  # Number of clusters
M = len(values)  # Number of samples
n = 2  # Number of attributes
iters = 10  # Number of iterations
fcm_m = 2  # fuzziness

D = np.random.rand(m, M)
U = np.random.rand(m, M)
V = np.random.rand(m, n)

def calculate_new_centers(U, data):
    new_centers = []
    for i in range(U.shape[0]):
        denominator = np.sum(U[i, :] ** fcm_m)
        numerator = np.sum((U[i, :, np.newaxis] ** fcm_m) * data, axis=0)
        new_center = numerator / denominator
        new_centers.append(new_center)
    return np.array(new_centers)


for i in range(iters):
    for x in range(m):
        for y in range(M):
            D[x, y] = math.dist(V[x], values[y])
            if D[x, y] < 1e-10:
                D[x, y] = 1e-10

    for x in range(m):
        for y in range(M):
            U[x, y] = 1 / np.sum((D[x, y] / D[:, y]) ** (2 / (fcm_m - 1)))


    #sum of memberships is equal to 1
    assert np.allclose(np.sum(U, axis=0), 1.0)

    V = calculate_new_centers(U, values)



    plt.scatter(V[0][0], V[0][1], marker='d', color='red', label='Cluster 1')
    plt.scatter(V[1][0], V[1][1], marker='d', color='green',label='Cluster 2')
    plt.scatter(V[2][0], V[2][1], marker='d', color='blue',label='Cluster 3')
    for i in range(len(values)):
        plt.scatter(values[i, 0], values[i, 1], c=(U[0][i], U[1][i], U[2][i]), alpha=0.5)
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title('FCM Clustering')
    plt.show()

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

points_x = [-1, 0, 1]
points_y = [1, 0, 1]

sin_x = np.arange(-1, 1.1, 0.1)
sin_y = sin_x * sin_x - 1

x = np.arange(-4, 4.5, 0.5)
y = np.arange(-4, 4.5, 0.5)

a, b = np.meshgrid(x, y)

C = a ** 2 + b ** 2

cs = plt.contour(a, b, C, [4], colors = 'red')
red = mpatches.Patch(color = 'red', label='lamane')
yellow = mpatches.Patch(color = 'yellow', label='sin')
red_dot = mpatches.Patch(color = 'blue', label='punkty')


plt.plot(points_x, points_y, 'bo')
plt.plot(sin_x, sin_y, 'y')

plt.axis((-2, 2, -3, 3))
plt.grid(True)
plt.legend(handles=[red, yellow, red_dot])

patches = [
    plt.plot([],[], marker='_', ms=10, ls="", mec=None, color='r', label="lamane")[0],
    plt.plot([],[], marker=".", ms=10, ls="", mec=None, color='b', label="punkty")[0],
    plt.plot([],[], marker='_', ms=10, ls="", mec=None, color='y', label="sin")[0],
           ]
plt.legend(handles=patches, loc='upper right', numpoints=1)

plt.show()
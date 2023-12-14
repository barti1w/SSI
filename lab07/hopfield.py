wzor1 = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0]
]

wzor2 = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1]
]

wzor3 = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]

test1 = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0]
]

test2 = [
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1]
]

test3 = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

test4 = [
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1]
]

import numpy as np
import matplotlib.pyplot as plt

def plot_array(ax, array, title):
    ax.imshow(array, cmap='gray', interpolation='nearest')
    ax.set_title(title)

class HopfieldNetwork:

    def __init__(self, size):
        self.size = size
        self.weights = np.zeros((size, size))

    def train_image(self, image):
        image = np.array(image)
        image[image == 0] = -1
        for i in range(self.size):
            for j in range(self.size):
                if i != j:
                    self.weights[i, j] += (1 / self.size) * image[i % 5, int(i/5)] * image[j % 5, int(j/5)]

    def recognize_image(self, image):
        image = np.array(image)
        image[image == 0] = -1
        for _ in range(100):
            for i in range(self.size):
                net_input = 0
                for j in range(self.size):
                    net_input += image[j % 5, int(j/5)] * self.weights[i, j]
                if(net_input >= 0):
                    image[i % 5, int(i / 5)] = 1
                else:
                    image[i % 5, int(i / 5)] = -1
        image[image == -1] = 0
        return image


hopfield_net = HopfieldNetwork(25)

hopfield_net.train_image(wzor1)
hopfield_net.train_image(wzor2)
hopfield_net.train_image(wzor3)

test_patterns = [test1, test2, test3, test4]

index = 0
for test_pattern in test_patterns:
    index += 1
    fig, axs = plt.subplots(1, 5, figsize=(12, 4))
    plot_array(axs[0], wzor1, 'Wzor1')
    plot_array(axs[1], wzor2, 'Wzor2')
    plot_array(axs[2], wzor3, 'Wzor3')

    restored_image = hopfield_net.recognize_image(test_pattern)
    plot_array(axs[3], test_pattern, f'Test {index}')
    plot_array(axs[4], restored_image, 'Wynik')

    plt.tight_layout()
    plt.show()
import numpy as np
import matplotlib.pyplot as plt

a = np.ones((40, 40)) #white block
b = np.zeros((40, 40)) #black block

c = np.block([[a, b],[b, a]])
d = np.block([[b, b],[a, a]])

A = 10 * (c + d)
M = c * d
S = c - d
D = c / 4


titles = ["c", "d", "A = 10*(c+d)", "M = c*d", "S = c-d", "D = c/4"]
matrices = [c, d, A, M, S, D]

fig = plt.figure(figsize=(8, 10))
for i, (mat, title) in enumerate(zip(matrices, titles), 1):
    plt.subplot(3, 2, i)
    plt.imshow(mat, cmap="gray")
    plt.title(title)
    plt.axis("off")

fig.set_facecolor("yellow")
plt.show()
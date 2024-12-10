import numpy as np
import random
from time import time
from matplotlib import pyplot as plt

def step(matrix):
    N = len(matrix)
    M = len(matrix[0])

    next_matrix = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            neighbours = sum(
                matrix[k][l]
                for k in ((i - 1) % N, i, (i + 1) % N)
                for l in ((j - 1) % M, j, (j + 1) % M)
                if k != i and l != j
            )

            next_matrix[i][j] = int((neighbours == 2 and arr[i][j]) or neighbours == 3)

    return next_matrix


def step_numpy(matrix):
    matrix = np.array(matrix)
    N, M = matrix.shape

    padded_matrix = np.pad(matrix, pad_width=1, mode="wrap")

    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

    neighbours = np.convolve(
        padded_matrix.flatten(), kernel.flatten(), mode="same"
    ).reshape(N + 2, M + 2)

    neighbours = neighbours[1 : N + 1, 1 : M + 1]
    next_matrix = ((neighbours == 2) & (matrix == 1)) | (neighbours == 3)
    return next_matrix.astype(int)


N = M = 128
arr = [[random.randint(0, 1) for _ in range(M)] for _ in range(N)]
arr_numpy = np.array(arr)

start_time = time()

for _ in range(128):
    arr = step(arr)

end_time = time()

t1 = end_time - start_time

start_time = time()

for _ in range(128):
    arr_numpy = step_numpy(arr_numpy)

end_time = time()

t2 = end_time - start_time
assert not np.array_equal(np.array(arr), arr_numpy)

print(t1)
print(t2)
plt.bar(("Обычный массив", "numpy"), (t1, t2))
plt.show()

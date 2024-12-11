import numpy as np
import random
from time import time
from matplotlib import pyplot as plt

def step(matrix, next_matrix):
    N = len(matrix)
    M = len(matrix[0])

    for i in range(N):
        for j in range(M):
            neighbours = sum(
                matrix[k][l]
                for k in ((i - 1) % N, i, (i + 1) % N)
                for l in ((j - 1) % M, j, (j + 1) % M)
                if k != i and l != j
            )

            next_matrix[i][j] = int((neighbours == 2 and arr[i][j]) or neighbours == 3)

def step_numpy_vectorization(matrix):
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

next_arr = [[0] * M for _ in range(N)]
for _ in range(128):
    step(arr, next_arr)
    arr = next_arr

end_time = time()

t1 = end_time - start_time

start_time = time()

next_arr_numpy = np.zeros((M, N))
for _ in range(128):
    step(arr, next_arr_numpy)
    arr_numpy = next_arr_numpy

end_time = time()
t2 = end_time - start_time

start_time = time()

for _ in range(128):
    arr_numpy = step_numpy_vectorization(arr_numpy)

end_time = time()
t3 = end_time - start_time

assert not np.array_equal(np.array(arr), arr_numpy)

print(t1)
print(t2)
print(t3)
plt.bar(("Обычный массив", "numpy", "numpy с векторизацией"), (t1, t2, t3))
plt.show()

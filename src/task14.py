import numpy as np
import random
from time import time
from matplotlib import pyplot as plt

run_time = []


def print_time(func):
    def wrapper(*args, **kwargs):
        start = time()

        result = func()
        end = time()
        print(end - start)
        run_time.append(end - start)

        return result

    return wrapper


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

            next_matrix[i][j] = int(
                (neighbours == 2 and matrix[i][j]) or neighbours == 3
            )


def step_numpy_vectorization(matrix):
    matrix = np.array(matrix)
    N, M = matrix.shape

    padded_matrix = np.pad(matrix, pad_width=1, mode="wrap")

    kernel = np.array(
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]
    )

    neighbours = np.convolve(
        padded_matrix.flatten(), kernel.flatten(), mode="same"
    ).reshape(N + 2, M + 2)

    neighbours = neighbours[1 : N + 1, 1 : M + 1]
    next_matrix = ((neighbours == 2) & (matrix == 1)) | (neighbours == 3)
    return next_matrix.astype(int)


N = M = 128
DATA = [[random.randint(0, 1) for _ in range(M)] for _ in range(N)]


@print_time
def run_list():
    arr = list(DATA)
    next_arr = [[0] * M for _ in range(N)]

    for _ in range(128):
        step(arr, next_arr)
        arr, next_arr = next_arr, arr


@print_time
def run_numpy():
    arr = np.array(DATA)
    next_arr = np.zeros((M, N))

    for _ in range(128):
        step(arr, next_arr)
        arr, next_arr = next_arr, arr

    return arr


@print_time
def run_numpy_vectorization():
    arr = np.array(DATA)

    for _ in range(128):
        arr = step_numpy_vectorization(arr)

    return arr


r1 = run_list()
r2 = run_numpy()
r3 = run_numpy_vectorization()
assert not np.array_equal(np.array(r1), r2) or not np.array_equal(r2, r3)

plt.bar(("Обычный массив", "numpy", "numpy с векторизацией"), run_time)
plt.show()

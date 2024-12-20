import threading
from time import time

queue = []
lock = threading.Lock()


def matrix_mult(a, b):
    N = len(a)
    M = len(a[0])
    K = len(b[0])

    c = [[0] * K for _ in range(N)]

    for i in range(N):
        for j in range(K):
            for k in range(M):
                c[i][j] += a[i][k] * b[k][j]

    return c


def producer_run(count):
    with lock:
        for i in range(25, 25 + count + 1):
            queue.append((i, 20, 10))


def consumer_run():
    with lock:
        size, value, times = queue.pop()

    main_matrix = [[value ** (i + j) for j in range(size)] for i in range(size)]
    matrix = [[value ** (i + j) for j in range(size)] for i in range(size)]

    for _ in range(times):
        main_matrix = matrix_mult(main_matrix, matrix)

    return sum(sum(i) for i in main_matrix)


for i in range(1, 21):
    start = time()

    producer_run(i)

    threads = [threading.Thread(target=consumer_run) for _ in range(i)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end = time()
    print(i, end - start)


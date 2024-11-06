def format_table(benchmarks: list[str], algos: list[str], results: list[list]):
    def get(i: int, j: int) -> str:
        if i == 0 and j == 0:
            return "Benchmark"

        if i == 0:
            return algos[j - 1]

        if j == 0:
            return benchmarks[i - 1]

        return results[i - 1][j - 1]

    N = len(benchmarks) + 1
    M = len(algos) + 1

    results = [[str(j) for j in i] for i in results]

    length = [0] * M

    for i in range(N):
        for j in range(M):
            length[j] = max(length[j], len(get(i, j)))

    for i in range(N):
        print("|", end="")
        for j in range(M):
            print(f" {get(i,j):<{length[j]}} |", end="")

        print()
        if i == 0:
            print(f"|{"-" * (sum(length) + 3 * M - 1)}|")

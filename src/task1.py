from math import floor, log2


def int_bit_count(n: int) -> int:
    if n == 0:
        return 0

    count = int(n < 0)

    bit_len = floor(log2(abs(n))) + 1
    for _ in range(bit_len):
        count += n & 1
        n >>= 1

    return count

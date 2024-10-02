def int_bit_count(n: int) -> int:
    count = 0

    while n > 0:
        count += (n & 1)
        n >>= 1

    return count


print(int_bit_count(int(input())))

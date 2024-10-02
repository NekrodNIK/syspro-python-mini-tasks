def int_bit_count(n: int) -> int:
    count = 0
    while n > 0:
        if (n & 1) == 1:
            count += 1

        n >>= 1

    return count


print(int_bit_count(int(input())))

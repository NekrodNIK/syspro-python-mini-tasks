def int_bit_count(n: int) -> int:
    count = 0

    if n != abs(n):
        count += 1

    while n not in (-1, 0):
        count += n & 1
        n >>= 1

    return count


print(int_bit_count(int(input())))

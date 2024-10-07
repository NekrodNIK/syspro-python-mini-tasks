from src.task1 import int_bit_count


def _bin_2s_complement(n: int) -> str:
    """
        Returns the binary representation of the number in 2's compliment
        format: s_n
        s is sign, n is significant bits
        
        example: -16 -> 1_10000
    """
    len_ = n.bit_length()+1
    bits = n & (2**len_ - 1)

    result = f"{bits:b}".zfill(len_)
    return "".join((result[0], "_", result[1:]))

def test_positive():
    for number in range(0, 10**5):
        result = int_bit_count(number)
        expected = _bin_2s_complement(number).count("1")

        assert result == expected


def test_negative():
    for number in range(-1, -10**5, -1):
        result = int_bit_count(number)
        expected = _bin_2s_complement(number).count("1")

        assert result == expected

from src.task3 import parse


def test_example():
    assert parse("1 2 | 3 4") == [[1.0, 2.0], [3.0, 4.0]]


def test_general():
    matrix = [[1.1, 1.2, 1.3], [2.1, 2.2, 2.3], [3.1, 3.2, 3.3]]

    lines = [" ".join(str(i) for i in line) for line in matrix]
    str_ = " | ".join(lines)

    assert parse(str_) == matrix

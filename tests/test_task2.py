from src.task2 import my_zip


def test_example():
    expected = list(zip([1, 2, 3], ["a", "b"]))
    result = my_zip([1, 2, 3], ["a", "b"])

    assert result == expected


def test_general():
    a = [i for i in range(1000)]
    b = [chr(j) for j in range(1000)]

    assert my_zip(a, b) == list(zip(a, b))
